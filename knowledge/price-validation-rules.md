# Price Validation Rules SiTukang

## Tujuan

Dokumen ini berisi aturan validasi harga untuk Agentic RAG SiTukang. AI harus menggunakan aturan ini ketika mengevaluasi apakah harga jasa atau harga material yang dimasukkan worker termasuk wajar, perlu klarifikasi, atau tidak wajar.

## Prinsip Utama

- Jika knowledge base memiliki `harga_patokan`, AI harus menggunakan harga patokan tunggal.
- AI tidak boleh menjawab dengan kisaran jika harga patokan tersedia.
- Harga worker boleh berbeda dari harga patokan jika ada alasan yang masuk akal seperti lokasi kota besar, worker senior, verified, emergency, material tambahan, atau tingkat kesulitan tinggi.
- Jika informasi tidak lengkap, AI tidak boleh langsung menolak. AI harus memberi status `perlu_klarifikasi`.
- Jika layanan atau material tidak relevan dengan order, AI harus memberi `item_tidak_relevan`.

## Format Jawaban Harga

Jika user bertanya harga layanan atau material:

> Harga patokan [nama layanan/material] adalah Rp[harga_patokan] per [unit].

Contoh:

> Harga patokan cuci AC Split 0.5–2 PK adalah Rp90.000 per unit.

## Rule Harga Jasa

| Kondisi | Decision | Risk Flag | Severity | Clarification |
|---|---|---|---|---|
| harga_input <= harga_patokan x 1.3 | wajar | tidak ada | none | tidak perlu |
| harga_input > harga_patokan x 1.3 dan <= harga_patokan x 1.7 | perlu_klarifikasi | harga_tidak_wajar | medium | tanyakan apakah termasuk material, emergency, lokasi jauh, atau pekerjaan tambahan |
| harga_input > harga_patokan x 1.7 | tidak_wajar | harga_tidak_wajar | high | tanyakan alasan kenaikan harga secara rinci |
| harga_input < harga_patokan x 0.5 | perlu_klarifikasi | data_tidak_lengkap | medium | tanyakan apakah harga hanya DP, belum termasuk jasa, atau salah satuan |
| satuan tidak jelas | perlu_klarifikasi | data_tidak_lengkap | medium | tanyakan satuan harga |
| layanan tidak sesuai order | tidak_wajar | item_tidak_relevan | high | tanyakan relevansi layanan terhadap order |
| alasan tidak ada | perlu_klarifikasi | alasan_tidak_lengkap | medium | tanyakan alasan kebutuhan layanan/material |
| layanan yang sama sudah tercatat sebelumnya | perlu_klarifikasi | duplikat | medium | tanyakan apakah input tambahan atau duplikasi |

## Rule Toleransi Worker

Harga worker dapat dianggap masih wajar walaupun di atas harga patokan jika memenuhi salah satu kondisi berikut:

| Kondisi Worker | Toleransi Tambahan |
|---|---:|
| Kota besar | +30% |
| Worker senior verified | +35% |
| Worker specialist | +50% |
| Emergency malam/hari libur | +50% |
| Akses sulit/berisiko | +40% |
| Termasuk material | sesuai nilai material |
| Pekerjaan kompleks atau scope bertambah | berdasarkan klarifikasi |

## Rule Decision Akhir

### Decision: wajar

Gunakan jika:
- Harga sama dengan harga patokan.
- Harga masih dalam toleransi.
- Layanan/material relevan dengan order.
- Satuan dan alasan jelas.

### Decision: perlu_klarifikasi

Gunakan jika:
- Harga lebih mahal dari patokan tetapi mungkin punya alasan.
- Satuan belum jelas.
- Jumlah belum jelas.
- Apakah termasuk material belum jelas.
- Ada kemungkinan duplikasi.
- Alasan worker kurang detail.

### Decision: tidak_wajar

Gunakan jika:
- Harga jauh melebihi harga patokan tanpa alasan.
- Layanan/material tidak relevan dengan order.
- Harga input tidak masuk akal untuk satuan yang disebutkan.
- Worker memasukkan item yang tidak berhubungan dengan masalah user.

## Template Clarification Question

### Harga terlalu tinggi

> Harga yang dimasukkan lebih tinggi dari harga patokan. Apakah harga tersebut sudah termasuk material, biaya emergency, akses sulit, atau pekerjaan tambahan?

### Satuan tidak jelas

> Harga tersebut dihitung per apa? Per unit, per titik, per meter, per m2, per kunjungan, atau per pekerjaan?

### Item tidak relevan

> Mengapa item atau layanan tersebut diperlukan untuk order ini?

### Data jumlah tidak lengkap

> Berapa jumlah item yang dibeli dan satuannya apa?

### Dugaan duplikat

> Apakah ini pembelian tambahan atau duplikasi dari pembelian yang sudah dicatat sebelumnya?

## Instruksi untuk AI

Jika konteks berisi `harga_patokan`, jangan gunakan kata:
- kisaran
- sekitar
- mulai dari
- kurang lebih

Gunakan:
- harga patokan
- berdasarkan knowledge base
- harga input
- selisih harga
- keputusan
- risk flag
