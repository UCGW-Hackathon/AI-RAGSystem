# Knowledge Base Harga Jasa Tukang Indonesia 2025–2026 untuk SiTukang

## Status Data

Dataset ini adalah estimasi harga pasar jasa tukang rumah tangga di Indonesia untuk kebutuhan knowledge base SiTukang. Harga bukan harga resmi nasional dan dapat berubah berdasarkan lokasi, tingkat kesulitan, pengalaman worker, rating, jam kerja, kondisi lapangan, serta apakah material termasuk atau tidak.

Dataset ini dibuat agar AI SiTukang dapat:

* mengecek kewajaran harga jasa,
* membandingkan harga worker dengan harga referensi pasar,
* mendeteksi harga tidak wajar,
* memberi risk flag,
* membuat pertanyaan klarifikasi,
* membantu user memahami alasan variasi harga antar-worker.

---

## Prinsip Umum Harga

Harga jasa tukang tidak boleh dianggap tunggal. Pada kategori dan layanan yang sama, worker berbeda dapat memiliki harga berbeda karena beberapa faktor:

1. Lokasi kerja: kota besar biasanya lebih mahal daripada kabupaten.
2. Pengalaman worker: senior dan specialist biasanya lebih mahal.
3. Rating dan reputasi: worker dengan rating tinggi dan completed jobs banyak dapat memiliki harga premium.
4. Verifikasi: worker verified dapat mengenakan harga lebih tinggi karena tingkat kepercayaan lebih tinggi.
5. Tingkat kesulitan: pekerjaan di area tinggi, sempit, bocor parah, atau risiko listrik biasanya lebih mahal.
6. Waktu kerja: malam, hari libur, dan emergency dapat menambah biaya.
7. Material: harga jasa saja harus dibedakan dari harga jasa plus material.
8. Sistem kerja: per kunjungan, per titik, per unit, per meter, per m2, per hari, per paket, atau per pekerjaan.

---

## Faktor Penyesuaian Lokasi dan Kondisi

| Faktor                                       | Multiplier / Tambahan | Catatan                                                                |
| -------------------------------------------- | --------------------: | ---------------------------------------------------------------------- |
| Kabupaten / kota kecil                       |           0.85x–1.05x | Cocok untuk worker lokal, biaya operasional lebih rendah               |
| Kota sedang                                  |           1.00x–1.20x | Harga pasar normal                                                     |
| Kota besar: Jakarta, Surabaya, Bandung, Bali |           1.15x–1.40x | Biaya transport, demand, dan operasional lebih tinggi                  |
| Worker junior                                |      -10% sampai -25% | Biasanya untuk pekerjaan ringan                                        |
| Worker mid                                   |        0% sampai +15% | Harga mendekati median pasar                                           |
| Worker senior verified                       |      +10% sampai +30% | Reputasi dan pengalaman lebih tinggi                                   |
| Worker specialist                            |      +25% sampai +50% | Untuk AC inverter, listrik panel, kebocoran kompleks, CCTV, smart home |
| Emergency malam / hari libur                 |      +20% sampai +50% | Untuk respons cepat di luar jam normal                                 |
| Area sulit akses / berisiko                  |      +15% sampai +40% | Contoh: atap tinggi, plafon tinggi, listrik berisiko, pipa tersembunyi |
| Jasa plus material                           |     +30% sampai +200% | Tergantung jenis material                                              |

---

## Ringkasan Kategori Harga Referensi

| Kategori | Layanan Umum | Harga Minimum | Harga Maksimum | Satuan Umum | Catatan |
|---|---:|---:|---|---|
| Tukang AC | Cuci, tambah freon, isi freon, bongkar pasang | 75000 | 750000 | per unit / per pekerjaan | Freon dan sparepart sering dihitung terpisah |
| Tukang listrik | Pasang titik, saklar, MCB, inspeksi | 75000 | 750000 | per titik / per pekerjaan | Material kabel dan komponen biasanya terpisah |
| Tukang pipa / ledeng | Bocor, mampet, keran, wastafel, shower | 75000 | 1250000 | per pekerjaan / per titik | Mampet berat lebih mahal |
| Tukang bangunan umum | Harian, plester, aci, bata, cor kecil | 100000 | 300000 | per hari / per m2 | Upah berbeda untuk kuli, tukang, mandor |
| Tukang cat | Interior, exterior, plafon, pagar | 18000 | 60000 | per m2 | Cat bisa termasuk atau tidak |
| Tukang plafon | Gypsum, PVC, GRC, list, bongkar | 50000 | 250000 | per m2 / per meter | Plus material jauh lebih mahal |
| Tukang keramik | Lantai, dinding, granit, bongkar, nat | 45000 | 175000 | per m2 | Ukuran besar dan granit lebih mahal |
| Tukang kayu / furniture | Pintu, engsel, rak, lemari, laci | 75000 | 2500000 | per pekerjaan / per paket | Custom furniture sangat bervariasi |
| Tukang pintu dan kunci | Buka kunci, silinder, handle, smart lock | 75000 | 900000 | per pekerjaan | Emergency malam lebih mahal |
| Tukang atap / genteng | Bocor, genteng, talang, waterproofing | 100000 | 2500000 | per pekerjaan / per m2 | Akses tinggi menaikkan harga |
| Tukang kanopi / baja ringan | Kanopi, spandek, polycarbonate, rangka | 125000 | 800000 | per m2 / per pekerjaan | Material dominan dalam biaya |
| Tukang pompa air | Kapasitor, otomatis, jet pump, pasang pompa | 100000 | 900000 | per pekerjaan | Sparepart biasanya terpisah |
| Tukang water heater | Instalasi, service, safety valve, flushing | 150000 | 1200000 | per pekerjaan | Unit dan pipa material terpisah |
| Tukang CCTV / smart home | CCTV per titik, DVR, WiFi cam, smart switch | 100000 | 1500000 | per titik / per paket | Setting jaringan menaikkan harga |
| Tukang taman / kebun | Potong rumput, taman kecil, tanaman, koral | 75000 | 2500000 | per kunjungan / per m2 | Tanaman dan dekorasi terpisah |
| Tukang las | Pagar, engsel, teralis, bracket, railing | 100000 | 2500000 | per pekerjaan | Besi dan cat biasanya terpisah |
| Tukang aluminium / kaca | Kusen, kaca, sliding, sealant | 100000 | 2500000 | per pekerjaan / per m2 | Kaca dan aluminium sangat memengaruhi harga |
| Tukang sanitasi / kamar mandi | Closet, shower, wastafel, floor drain | 100000 | 1500000 | per pekerjaan | Sanitary ware biasanya terpisah |
| Tukang renovasi kecil | Dapur kecil, kamar kecil, finishing, bongkar | 250000 | 7500000 | per paket / per pekerjaan | Sangat tergantung scope |
| Survey / inspeksi | Survey, RAB, inspeksi teknis | 50000 | 500000 | per kunjungan | Dapat gratis jika lanjut pekerjaan |

---

# Service Price Reference

## Tukang AC

| Kode   | Nama Layanan           | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi       | Catatan                              |
| ------ | ---------------------- | --------: | --------: | ------------- | ----------------- | --------- | ------------ | ------------------------------------ |
| AC-001 | Cuci AC split 0.5–2 PK |     75000 |    150000 | per unit      | Tidak             | Ringan    | 45–90 menit  | Harga naik untuk akses outdoor sulit |
| AC-002 | Cuci AC inverter       |    120000 |    225000 | per unit      | Tidak             | Sedang    | 60–120 menit | Butuh teknisi lebih teliti           |
| AC-003 | Tambah freon R22       |    150000 |    300000 | per unit      | Ya                | Sedang    | 30–60 menit  | Tergantung tekanan freon             |
| AC-004 | Tambah freon R32/R410A |    200000 |    375000 | per unit      | Ya                | Sedang    | 30–60 menit  | Lebih mahal dari R22                 |
| AC-005 | Isi ulang freon kosong |    350000 |    600000 | per unit      | Ya                | Sedang    | 60–120 menit | Perlu cek kebocoran                  |
| AC-006 | Bongkar pasang AC      |    300000 |    750000 | per pekerjaan | Sebagian          | Berat     | 2–5 jam      | Tergantung jarak indoor-outdoor      |
| AC-007 | Instalasi AC baru      |    350000 |    850000 | per pekerjaan | Sebagian          | Berat     | 2–5 jam      | Pipa tambahan dihitung terpisah      |
| AC-008 | Ganti kapasitor AC     |    150000 |    350000 | per pekerjaan | Ya                | Sedang    | 30–90 menit  | Harga tergantung tipe kapasitor      |

## Tukang Listrik

| Kode   | Nama Layanan                | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi      | Catatan                          |
| ------ | --------------------------- | --------: | --------: | ------------- | ----------------- | --------- | ----------- | -------------------------------- |
| EL-001 | Inspeksi listrik ringan     |     75000 |    175000 | per kunjungan | Tidak             | Ringan    | 30–90 menit | Untuk cek awal masalah           |
| EL-002 | Pasang titik lampu          |    100000 |    275000 | per titik     | Tidak             | Sedang    | 1–2 jam     | Kabel dan pipa biasanya terpisah |
| EL-003 | Pasang stop kontak          |    125000 |    300000 | per titik     | Tidak             | Sedang    | 1–2 jam     | Tanam tembok lebih mahal         |
| EL-004 | Pasang saklar               |    100000 |    250000 | per titik     | Tidak             | Ringan    | 30–90 menit | Saklar ganda bisa lebih mahal    |
| EL-005 | Pasang MCB                  |    150000 |    450000 | per pekerjaan | Tidak             | Sedang    | 1–3 jam     | MCB tidak selalu termasuk        |
| EL-006 | Perbaikan korsleting ringan |    150000 |    600000 | per pekerjaan | Tidak             | Berat     | 1–4 jam     | Risiko tinggi, perlu klarifikasi |
| EL-007 | Penambahan jalur listrik    |    250000 |    750000 | per pekerjaan | Tidak             | Berat     | 2–6 jam     | Tergantung panjang kabel         |
| EL-008 | Pasang exhaust fan          |    150000 |    350000 | per titik     | Tidak             | Sedang    | 1–3 jam     | Bobok tembok menaikkan biaya     |

## Tukang Pipa / Ledeng / Plumbing

| Kode   | Nama Layanan                | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi      | Catatan                          |
| ------ | --------------------------- | --------: | --------: | ------------- | ----------------- | --------- | ----------- | -------------------------------- |
| PL-001 | Inspeksi kebocoran          |     75000 |    200000 | per kunjungan | Tidak             | Ringan    | 30–90 menit | Bisa jadi biaya survey           |
| PL-002 | Perbaikan pipa bocor ringan |    100000 |    300000 | per titik     | Tidak             | Sedang    | 1–3 jam     | Material pipa terpisah           |
| PL-003 | Ganti pipa PVC pendek       |    150000 |    500000 | per pekerjaan | Sebagian          | Sedang    | 1–4 jam     | Tergantung panjang pipa          |
| PL-004 | Pasang / ganti keran        |     75000 |    250000 | per pekerjaan | Tidak             | Ringan    | 30–90 menit | Keran biasanya dibeli terpisah   |
| PL-005 | Perbaikan wastafel / sink   |    175000 |    450000 | per pekerjaan | Tidak             | Sedang    | 1–3 jam     | Bisa melibatkan pipa dan sealant |
| PL-006 | Saluran mampet ringan       |    250000 |    600000 | per pekerjaan | Tidak             | Sedang    | 1–3 jam     | Alat khusus bisa menambah biaya  |
| PL-007 | Kloset mampet berat         |    500000 |   1250000 | per pekerjaan | Tidak             | Berat     | 2–5 jam     | Bisa perlu alat spiral           |
| PL-008 | Pasang shower               |    150000 |    450000 | per pekerjaan | Tidak             | Sedang    | 1–3 jam     | Shower set tidak termasuk        |

## Tukang Bangunan Umum

| Kode   | Nama Layanan             | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi    | Catatan                         |
| ------ | ------------------------ | --------: | --------: | ------------- | ----------------- | --------- | --------- | ------------------------------- |
| BG-001 | Kuli harian              |     90000 |    150000 | per hari      | Tidak             | Ringan    | 1 hari    | Tergantung lokasi               |
| BG-002 | Tukang bangunan standar  |    120000 |    200000 | per hari      | Tidak             | Sedang    | 1 hari    | Untuk pekerjaan umum            |
| BG-003 | Tukang finishing         |    175000 |    275000 | per hari      | Tidak             | Sedang    | 1 hari    | Lebih mahal karena presisi      |
| BG-004 | Kepala tukang            |    175000 |    250000 | per hari      | Tidak             | Sedang    | 1 hari    | Koordinasi pekerjaan            |
| BG-005 | Mandor                   |    200000 |    350000 | per hari      | Tidak             | Sedang    | 1 hari    | Untuk pekerjaan lebih besar     |
| BG-006 | Plester aci              |     45000 |     90000 | per m2        | Tidak             | Sedang    | Fleksibel | Tergantung ketebalan dan bidang |
| BG-007 | Bongkar dinding ringan   |     75000 |    175000 | per m2        | Tidak             | Berat     | Fleksibel | Buangan material terpisah       |
| BG-008 | Cor kecil / tambal beton |    250000 |    900000 | per pekerjaan | Tidak             | Berat     | 1–2 hari  | Material dihitung terpisah      |

## Tukang Cat

| Kode   | Nama Layanan           | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi    | Catatan                     |
| ------ | ---------------------- | --------: | --------: | ------------- | ----------------- | --------- | --------- | --------------------------- |
| CT-001 | Cat interior jasa saja |     18000 |     30000 | per m2        | Tidak             | Ringan    | Fleksibel | Harga tergantung luas       |
| CT-002 | Cat exterior jasa saja |     21000 |     40000 | per m2        | Tidak             | Sedang    | Fleksibel | Akses luar lebih sulit      |
| CT-003 | Cat plafon jasa saja   |     18000 |     35000 | per m2        | Tidak             | Sedang    | Fleksibel | Posisi kerja lebih sulit    |
| CT-004 | Pengerokan cat lama    |     15000 |     35000 | per m2        | Tidak             | Sedang    | Fleksibel | Tambahan sebelum cat ulang  |
| CT-005 | Plamir dinding         |     20000 |     45000 | per m2        | Tidak             | Sedang    | Fleksibel | Butuh permukaan rata        |
| CT-006 | Cat pagar besi         |     75000 |    250000 | per pekerjaan | Tidak             | Sedang    | 2–6 jam   | Tergantung panjang pagar    |
| CT-007 | Cat anti bocor         |     25000 |     60000 | per m2        | Sebagian          | Sedang    | Fleksibel | Material bisa termasuk      |
| CT-008 | Cat pintu / kusen      |     75000 |    250000 | per unit      | Tidak             | Sedang    | 2–5 jam   | Finishing halus lebih mahal |

## Tukang Plafon

| Kode   | Nama Layanan                       | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi    | Catatan                            |
| ------ | ---------------------------------- | --------: | --------: | ------------- | ----------------- | --------- | --------- | ---------------------------------- |
| PF-001 | Pasang plafon gypsum jasa saja     |     50000 |     90000 | per m2        | Tidak             | Sedang    | Fleksibel | Material terpisah                  |
| PF-002 | Pasang plafon gypsum plus material |    150000 |    220000 | per m2        | Ya                | Sedang    | Fleksibel | Tergantung merek gypsum            |
| PF-003 | Pasang plafon PVC plus material    |    175000 |    275000 | per m2        | Ya                | Sedang    | Fleksibel | Motif dan rangka memengaruhi harga |
| PF-004 | Pasang plafon GRC plus material    |    170000 |    300000 | per m2        | Ya                | Berat     | Fleksibel | Bobot lebih berat                  |
| PF-005 | Pasang list plafon                 |     15000 |     40000 | per meter     | Sebagian          | Ringan    | Fleksibel | Model list memengaruhi harga       |
| PF-006 | Bongkar plafon lama                |     25000 |     60000 | per m2        | Tidak             | Sedang    | Fleksibel | Pembuangan material terpisah       |
| PF-007 | Perbaikan plafon bocor             |    150000 |    750000 | per pekerjaan | Tidak             | Sedang    | 2–6 jam   | Sumber bocor perlu dicek           |
| PF-008 | Finishing compound plafon          |     30000 |     75000 | per m2        | Tidak             | Sedang    | Fleksibel | Butuh ketelitian                   |

## Tukang Keramik

| Kode   | Nama Layanan                       | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi    | Catatan                    |
| ------ | ---------------------------------- | --------: | --------: | ------------- | ----------------- | --------- | --------- | -------------------------- |
| KR-001 | Pasang keramik lantai 40x40        |     50000 |     90000 | per m2        | Tidak             | Sedang    | Fleksibel | Tenaga saja                |
| KR-002 | Pasang keramik lantai 60x60        |     60000 |    110000 | per m2        | Tidak             | Sedang    | Fleksibel | Lebih presisi              |
| KR-003 | Pasang granit besar                |     90000 |    175000 | per m2        | Tidak             | Berat     | Fleksibel | Butuh alat dan presisi     |
| KR-004 | Pasang keramik dinding kamar mandi |     75000 |    150000 | per m2        | Tidak             | Berat     | Fleksibel | Area vertikal lebih sulit  |
| KR-005 | Bongkar keramik lama               |     25000 |     75000 | per m2        | Tidak             | Sedang    | Fleksibel | Buangan terpisah           |
| KR-006 | Nat ulang keramik                  |     15000 |     45000 | per m2        | Sebagian          | Ringan    | Fleksibel | Cocok untuk kamar mandi    |
| KR-007 | Perbaikan keramik kopong           |    100000 |    500000 | per pekerjaan | Tidak             | Sedang    | 1–4 jam   | Perlu cek area             |
| KR-008 | Pasang backsplash dapur            |    100000 |    250000 | per m2        | Tidak             | Berat     | Fleksibel | Potongan kecil lebih rumit |

## Tukang Kayu / Furniture

| Kode   | Nama Layanan          | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi      | Catatan                  |
| ------ | --------------------- | --------: | --------: | ------------- | ----------------- | --------- | ----------- | ------------------------ |
| KY-001 | Perbaikan pintu kayu  |    100000 |    450000 | per pekerjaan | Tidak             | Sedang    | 1–4 jam     | Tergantung kerusakan     |
| KY-002 | Pasang engsel pintu   |     75000 |    250000 | per pekerjaan | Tidak             | Ringan    | 30–90 menit | Engsel terpisah          |
| KY-003 | Serut pintu seret     |    100000 |    300000 | per pekerjaan | Tidak             | Ringan    | 1–2 jam     | Cocok pintu memuai       |
| KY-004 | Pasang rak dinding    |    100000 |    350000 | per pekerjaan | Tidak             | Ringan    | 1–3 jam     | Bracket terpisah         |
| KY-005 | Perbaikan lemari      |    150000 |    750000 | per pekerjaan | Tidak             | Sedang    | 2–6 jam     | Sparepart terpisah       |
| KY-006 | Perbaikan laci macet  |    100000 |    350000 | per pekerjaan | Tidak             | Ringan    | 1–3 jam     | Rel laci terpisah        |
| KY-007 | Finishing politur     |    150000 |    800000 | per pekerjaan | Tidak             | Sedang    | 1–2 hari    | Tergantung ukuran        |
| KY-008 | Kitchen set sederhana |   1500000 |   7500000 | per paket     | Sebagian          | Berat     | 3–10 hari   | Custom sangat bervariasi |

## Tukang Pintu dan Kunci

| Kode   | Nama Layanan          | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi       | Catatan                              |
| ------ | --------------------- | --------: | --------: | ------------- | ----------------- | --------- | ------------ | ------------------------------------ |
| KN-001 | Buka pintu terkunci   |    100000 |    400000 | per pekerjaan | Tidak             | Ringan    | 15–60 menit  | Emergency malam lebih mahal          |
| KN-002 | Ganti silinder kunci  |    100000 |    350000 | per pekerjaan | Tidak             | Ringan    | 30–90 menit  | Silinder terpisah                    |
| KN-003 | Pasang handle pintu   |    100000 |    300000 | per unit      | Tidak             | Ringan    | 30–90 menit  | Handle terpisah                      |
| KN-004 | Perbaikan kunci macet |     75000 |    250000 | per pekerjaan | Tidak             | Ringan    | 30–90 menit  | Tergantung kerusakan                 |
| KN-005 | Pasang smart lock     |    250000 |    900000 | per unit      | Tidak             | Sedang    | 1–3 jam      | Setting aplikasi bisa menambah biaya |
| KN-006 | Ganti engsel pintu    |    100000 |    300000 | per pekerjaan | Tidak             | Ringan    | 30–120 menit | Engsel terpisah                      |
| KN-007 | Serut pintu seret     |    100000 |    300000 | per pekerjaan | Tidak             | Ringan    | 1–2 jam      | Mirip tukang kayu                    |
| KN-008 | Pasang door closer    |    150000 |    400000 | per unit      | Tidak             | Sedang    | 1–2 jam      | Door closer terpisah                 |

## Tukang Atap / Genteng

| Kode   | Nama Layanan                 | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi       | Catatan                     |
| ------ | ---------------------------- | --------: | --------: | ------------- | ----------------- | --------- | ------------ | --------------------------- |
| AT-001 | Inspeksi kebocoran atap      |    100000 |    300000 | per kunjungan | Tidak             | Sedang    | 30–120 menit | Akses tinggi lebih mahal    |
| AT-002 | Ganti genteng pecah          |    150000 |    600000 | per pekerjaan | Tidak             | Sedang    | 1–3 jam      | Genteng terpisah            |
| AT-003 | Perbaikan nok bocor          |    300000 |   1500000 | per pekerjaan | Sebagian          | Berat     | 1–2 hari     | Area luas lebih mahal       |
| AT-004 | Pasang talang air            |     75000 |    200000 | per meter     | Tidak             | Sedang    | Fleksibel    | Material talang terpisah    |
| AT-005 | Bersihkan talang             |    150000 |    500000 | per pekerjaan | Tidak             | Sedang    | 1–4 jam      | Tinggi bangunan memengaruhi |
| AT-006 | Waterproofing dak kecil      |     50000 |    150000 | per m2        | Sebagian          | Sedang    | Fleksibel    | Material memengaruhi harga  |
| AT-007 | Tambal bocor darurat         |    200000 |    900000 | per pekerjaan | Sebagian          | Sedang    | 1–4 jam      | Emergency fee mungkin ada   |
| AT-008 | Perbaikan rangka atap ringan |    500000 |   2500000 | per pekerjaan | Tidak             | Berat     | 1–3 hari     | Butuh inspeksi struktur     |

## Tukang Kanopi / Baja Ringan

| Kode   | Nama Layanan                | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi    | Catatan                    |
| ------ | --------------------------- | --------: | --------: | ------------- | ----------------- | --------- | --------- | -------------------------- |
| KP-001 | Pasang kanopi spandek       |    250000 |    550000 | per m2        | Ya                | Berat     | Fleksibel | Tergantung rangka          |
| KP-002 | Pasang kanopi polycarbonate |    300000 |    700000 | per m2        | Ya                | Berat     | Fleksibel | Material lebih mahal       |
| KP-003 | Perbaikan kanopi bocor      |    150000 |    750000 | per pekerjaan | Tidak             | Sedang    | 1–4 jam   | Sealant / baut terpisah    |
| KP-004 | Ganti atap kanopi           |    200000 |    600000 | per m2        | Ya                | Berat     | Fleksibel | Tergantung bahan           |
| KP-005 | Pasang rangka baja ringan   |    150000 |    350000 | per m2        | Tidak             | Berat     | Fleksibel | Tenaga saja                |
| KP-006 | Las rangka ringan           |    150000 |    600000 | per pekerjaan | Tidak             | Sedang    | 1–4 jam   | Elektroda dan cat terpisah |
| KP-007 | Cat ulang rangka            |     50000 |    150000 | per m2        | Tidak             | Sedang    | Fleksibel | Cat terpisah               |
| KP-008 | Bongkar kanopi lama         |     75000 |    200000 | per m2        | Tidak             | Berat     | Fleksibel | Buangan terpisah           |

## Tukang Pompa Air

| Kode   | Nama Layanan                  | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi       | Catatan                   |
| ------ | ----------------------------- | --------: | --------: | ------------- | ----------------- | --------- | ------------ | ------------------------- |
| PA-001 | Inspeksi pompa air            |    100000 |    250000 | per kunjungan | Tidak             | Ringan    | 30–90 menit  | Untuk diagnosis awal      |
| PA-002 | Pancing pompa                 |    100000 |    300000 | per pekerjaan | Tidak             | Ringan    | 30–120 menit | Jika pompa masuk angin    |
| PA-003 | Ganti kapasitor pompa         |    150000 |    350000 | per pekerjaan | Ya                | Sedang    | 30–90 menit  | Tergantung tipe kapasitor |
| PA-004 | Ganti otomatis pompa          |    175000 |    450000 | per pekerjaan | Sebagian          | Sedang    | 1–2 jam      | Pressure switch terpisah  |
| PA-005 | Perbaikan pompa tidak menyala |    200000 |    700000 | per pekerjaan | Tidak             | Sedang    | 1–4 jam      | Bisa perlu sparepart      |
| PA-006 | Pasang pompa baru             |    300000 |    900000 | per pekerjaan | Tidak             | Berat     | 2–6 jam      | Pompa tidak termasuk      |
| PA-007 | Bongkar pasang pompa          |    250000 |    700000 | per pekerjaan | Tidak             | Sedang    | 2–5 jam      | Jalur pipa memengaruhi    |
| PA-008 | Setting pressure switch       |    100000 |    300000 | per pekerjaan | Tidak             | Ringan    | 30–90 menit  | Untuk tekanan air         |

## Tukang Water Heater

| Kode   | Nama Layanan                   | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi  | Catatan                 |
| ------ | ------------------------------ | --------: | --------: | ------------- | ----------------- | --------- | ------- | ----------------------- |
| WH-001 | Instalasi water heater listrik |    250000 |    800000 | per pekerjaan | Tidak             | Sedang    | 2–5 jam | Unit dan pipa terpisah  |
| WH-002 | Instalasi water heater gas     |    300000 |   1000000 | per pekerjaan | Tidak             | Berat     | 3–6 jam | Perlu jalur gas aman    |
| WH-003 | Service water heater           |    150000 |    450000 | per pekerjaan | Tidak             | Sedang    | 1–3 jam | Tergantung kerusakan    |
| WH-004 | Ganti safety valve             |    150000 |    450000 | per pekerjaan | Sebagian          | Sedang    | 1–2 jam | Valve bisa terpisah     |
| WH-005 | Water heater tidak panas       |    200000 |    700000 | per pekerjaan | Tidak             | Sedang    | 1–4 jam | Elemen pemanas terpisah |
| WH-006 | Flushing tangki                |    200000 |    600000 | per pekerjaan | Tidak             | Sedang    | 1–3 jam | Untuk kerak tangki      |
| WH-007 | Ganti selang / pipa            |    150000 |    500000 | per pekerjaan | Sebagian          | Sedang    | 1–3 jam | Tergantung panjang      |
| WH-008 | Bongkar water heater           |    150000 |    400000 | per pekerjaan | Tidak             | Ringan    | 1–2 jam | Tidak termasuk disposal |

## Tukang CCTV / Smart Home

| Kode   | Nama Layanan             | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi      | Catatan                    |
| ------ | ------------------------ | --------: | --------: | ------------- | ----------------- | --------- | ----------- | -------------------------- |
| CV-001 | Pasang kamera CCTV       |    150000 |    400000 | per titik     | Tidak             | Sedang    | 1–2 jam     | Kamera dan kabel terpisah  |
| CV-002 | Tarik kabel CCTV         |     10000 |     30000 | per meter     | Tidak             | Sedang    | Fleksibel   | Jalur sulit lebih mahal    |
| CV-003 | Setting DVR / NVR        |    150000 |    500000 | per pekerjaan | Tidak             | Sedang    | 1–3 jam     | Tergantung jumlah kamera   |
| CV-004 | Pasang kamera WiFi       |    100000 |    300000 | per titik     | Tidak             | Ringan    | 30–90 menit | Perlu koneksi WiFi stabil  |
| CV-005 | Setting remote view      |    150000 |    450000 | per pekerjaan | Tidak             | Sedang    | 1–3 jam     | Aplikasi dan router        |
| CV-006 | Perbaikan kamera offline |    150000 |    500000 | per pekerjaan | Tidak             | Sedang    | 1–3 jam     | Bisa masalah adaptor/kabel |
| CV-007 | Pasang smart doorbell    |    150000 |    450000 | per unit      | Tidak             | Sedang    | 1–2 jam     | Perlu pairing aplikasi     |
| CV-008 | Pasang smart switch      |    150000 |    500000 | per titik     | Tidak             | Sedang    | 1–3 jam     | Harus cek netral listrik   |

## Tukang Taman / Kebun

| Kode   | Nama Layanan            | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi    | Catatan                      |
| ------ | ----------------------- | --------: | --------: | ------------- | ----------------- | --------- | --------- | ---------------------------- |
| TM-001 | Perawatan taman ringan  |     75000 |    250000 | per kunjungan | Tidak             | Ringan    | 1–3 jam   | Tergantung luas              |
| TM-002 | Potong rumput           |     75000 |    300000 | per kunjungan | Tidak             | Ringan    | 1–3 jam   | Area luas lebih mahal        |
| TM-003 | Pangkas tanaman         |    100000 |    400000 | per kunjungan | Tidak             | Sedang    | 1–4 jam   | Pohon tinggi lebih mahal     |
| TM-004 | Tanam rumput gajah mini |     35000 |     90000 | per m2        | Sebagian          | Sedang    | Fleksibel | Material bisa termasuk       |
| TM-005 | Pembersihan halaman     |    100000 |    500000 | per pekerjaan | Tidak             | Sedang    | 1–5 jam   | Sampah tanaman terpisah      |
| TM-006 | Pembuatan taman kecil   |    750000 |   2500000 | per paket     | Sebagian          | Berat     | 1–3 hari  | Tanaman dan koral bervariasi |
| TM-007 | Pasang batu koral       |     50000 |    150000 | per m2        | Sebagian          | Sedang    | Fleksibel | Koral memengaruhi harga      |
| TM-008 | Ganti media tanam       |     50000 |    200000 | per pekerjaan | Sebagian          | Ringan    | 1–3 jam   | Media tanam bisa terpisah    |

## Tukang Las

| Kode   | Nama Layanan          | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi       | Catatan                 |
| ------ | --------------------- | --------: | --------: | ------------- | ----------------- | --------- | ------------ | ----------------------- |
| LS-001 | Las pagar ringan      |    150000 |    800000 | per pekerjaan | Tidak             | Sedang    | 1–5 jam      | Besi dan cat terpisah   |
| LS-002 | Perbaikan engsel besi |    100000 |    350000 | per pekerjaan | Tidak             | Ringan    | 30–120 menit | Tergantung akses        |
| LS-003 | Las teralis           |    250000 |   1500000 | per pekerjaan | Tidak             | Sedang    | 1–2 hari     | Material terpisah       |
| LS-004 | Las kanopi            |    250000 |   2000000 | per pekerjaan | Tidak             | Berat     | 1–3 hari     | Area tinggi lebih mahal |
| LS-005 | Las rak besi          |    200000 |   1200000 | per pekerjaan | Tidak             | Sedang    | 1–2 hari     | Custom ukuran           |
| LS-006 | Potong besi           |     75000 |    300000 | per pekerjaan | Tidak             | Ringan    | 30–120 menit | Tergantung ketebalan    |
| LS-007 | Perbaikan railing     |    200000 |   1500000 | per pekerjaan | Tidak             | Sedang    | 1–2 hari     | Finishing cat terpisah  |
| LS-008 | Las darurat panggilan |    200000 |    900000 | per pekerjaan | Tidak             | Sedang    | 1–4 jam      | Emergency fee berlaku   |

## Tukang Aluminium / Kaca

| Kode   | Nama Layanan               | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi      | Catatan                    |
| ------ | -------------------------- | --------: | --------: | ------------- | ----------------- | --------- | ----------- | -------------------------- |
| AK-001 | Pasang kusen aluminium     |    150000 |    600000 | per titik     | Tidak             | Sedang    | 2–5 jam     | Bahan aluminium terpisah   |
| AK-002 | Pasang pintu aluminium     |    250000 |   1000000 | per unit      | Tidak             | Sedang    | 2–6 jam     | Daun pintu terpisah        |
| AK-003 | Ganti kaca jendela         |    100000 |    600000 | per pekerjaan | Sebagian          | Sedang    | 1–3 jam     | Tergantung jenis kaca      |
| AK-004 | Pasang kaca kamar mandi    |    300000 |   1500000 | per pekerjaan | Sebagian          | Berat     | 2–6 jam     | Tempered lebih mahal       |
| AK-005 | Pasang sliding door        |    500000 |   2500000 | per pekerjaan | Sebagian          | Berat     | 1–2 hari    | Rel dan roda penting       |
| AK-006 | Perbaikan rel sliding      |    150000 |    500000 | per pekerjaan | Tidak             | Sedang    | 1–3 jam     | Roda bisa diganti          |
| AK-007 | Sealant kaca bocor         |    100000 |    400000 | per pekerjaan | Sebagian          | Ringan    | 1–2 jam     | Tergantung panjang sealant |
| AK-008 | Perbaikan handle aluminium |    100000 |    350000 | per pekerjaan | Tidak             | Ringan    | 30–90 menit | Handle terpisah            |

## Tukang Sanitasi / Kamar Mandi

| Kode   | Nama Layanan                 | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi      | Catatan               |
| ------ | ---------------------------- | --------: | --------: | ------------- | ----------------- | --------- | ----------- | --------------------- |
| SN-001 | Pasang closet duduk          |    300000 |    900000 | per pekerjaan | Tidak             | Berat     | 2–6 jam     | Closet tidak termasuk |
| SN-002 | Pasang closet jongkok        |    250000 |    800000 | per pekerjaan | Tidak             | Berat     | 2–6 jam     | Bisa perlu bongkar    |
| SN-003 | Ganti shower                 |    100000 |    350000 | per pekerjaan | Tidak             | Ringan    | 30–90 menit | Shower terpisah       |
| SN-004 | Ganti jet shower             |     75000 |    250000 | per pekerjaan | Tidak             | Ringan    | 30–90 menit | Part terpisah         |
| SN-005 | Pasang wastafel              |    200000 |    600000 | per pekerjaan | Tidak             | Sedang    | 1–4 jam     | Wastafel terpisah     |
| SN-006 | Ganti flexible hose          |     75000 |    200000 | per pekerjaan | Tidak             | Ringan    | 30–60 menit | Hose terpisah         |
| SN-007 | Ganti floor drain            |    100000 |    350000 | per pekerjaan | Tidak             | Sedang    | 1–3 jam     | Bisa perlu bobok      |
| SN-008 | Perbaikan rembes kamar mandi |    300000 |   1500000 | per pekerjaan | Sebagian          | Berat     | 1–3 hari    | Perlu inspeksi        |

## Tukang Renovasi Kecil

| Kode   | Nama Layanan               | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi       | Catatan                      |
| ------ | -------------------------- | --------: | --------: | ------------- | ----------------- | --------- | ------------ | ---------------------------- |
| RN-001 | Survey renovasi            |    100000 |    300000 | per kunjungan | Tidak             | Ringan    | 30–120 menit | Bisa jadi gratis jika lanjut |
| RN-002 | Perbaikan kamar kecil      |   1000000 |   5000000 | per paket     | Sebagian          | Berat     | 2–7 hari     | Scope harus jelas            |
| RN-003 | Renovasi dapur kecil       |   1500000 |   7500000 | per paket     | Sebagian          | Berat     | 3–10 hari    | Material dominan             |
| RN-004 | Tambal dinding retak       |    250000 |   1500000 | per pekerjaan | Sebagian          | Sedang    | 1–3 hari     | Tergantung panjang retak     |
| RN-005 | Perbaikan lantai           |    500000 |   3000000 | per pekerjaan | Sebagian          | Sedang    | 1–5 hari     | Tergantung material lantai   |
| RN-006 | Perbaikan plafon kecil     |    500000 |   2500000 | per pekerjaan | Sebagian          | Sedang    | 1–3 hari     | Area bocor perlu dicek       |
| RN-007 | Bongkar pasang ringan      |    300000 |   2000000 | per pekerjaan | Tidak             | Sedang    | 1–3 hari     | Buangan terpisah             |
| RN-008 | Paket setengah hari tukang |    250000 |    600000 | per paket     | Tidak             | Sedang    | 4–5 jam      | Cocok pekerjaan kecil        |

## Survey / Inspeksi / Kunjungan

| Kode   | Nama Layanan              | Harga Min | Harga Max | Satuan        | Termasuk Material | Kesulitan | Durasi       | Catatan                  |
| ------ | ------------------------- | --------: | --------: | ------------- | ----------------- | --------- | ------------ | ------------------------ |
| SV-001 | Survey ringan             |     50000 |    150000 | per kunjungan | Tidak             | Ringan    | 15–60 menit  | Untuk pekerjaan kecil    |
| SV-002 | Survey detail             |    150000 |    350000 | per kunjungan | Tidak             | Sedang    | 1–2 jam      | Dengan pengecekan teknis |
| SV-003 | Estimasi RAB sederhana    |    150000 |    500000 | per dokumen   | Tidak             | Sedang    | 1–3 hari     | Untuk renovasi kecil     |
| SV-004 | Inspeksi kebocoran        |    100000 |    300000 | per kunjungan | Tidak             | Sedang    | 30–120 menit | Atap/pipa/dak            |
| SV-005 | Inspeksi listrik          |    100000 |    350000 | per kunjungan | Tidak             | Sedang    | 30–120 menit | Risiko listrik           |
| SV-006 | Inspeksi AC               |     75000 |    200000 | per unit      | Tidak             | Ringan    | 30–60 menit  | Bisa lanjut service      |
| SV-007 | Biaya kunjungan normal    |     50000 |    150000 | per kunjungan | Tidak             | Ringan    | Fleksibel    | Bisa digabung ke invoice |
| SV-008 | Biaya kunjungan emergency |    150000 |    400000 | per kunjungan | Tidak             | Sedang    | Fleksibel    | Malam/hari libur         |

---

# Worker Pricing Variatif

## Tukang AC

| Worker Code | Nama Worker               | Kota/Tier   | Experience | Rating | Completed Jobs | Positioning | Base Visit Fee | Adjustment | Alasan Harga                               |
| ----------- | ------------------------- | ----------- | ---------- | -----: | -------------: | ----------- | -------------: | ---------: | ------------------------------------------ |
| AC-KAB-001  | Budi Service AC           | Kabupaten   | Junior     |    4.3 |             48 | Budget      |          30000 |       -15% | Harga lebih murah untuk pekerjaan ringan   |
| AC-KSD-002  | Raka Teknik AC            | Kota Sedang | Mid        |    4.6 |            132 | Standard    |          50000 |         0% | Harga mengikuti median pasar               |
| AC-SBY-003  | Ahmad Cooling             | Kota Besar  | Senior     |    4.8 |            320 | Premium     |          75000 |       +25% | Senior, verified, banyak pekerjaan selesai |
| AC-JKT-004  | Dimas Inverter Specialist | Kota Besar  | Specialist |    4.9 |            410 | Premium     |          85000 |       +40% | Spesialis AC inverter dan freon            |
| AC-EMG-005  | Cepat Dingin 24 Jam       | Kota Besar  | Senior     |    4.7 |            280 | Emergency   |         100000 |       +50% | Layanan malam dan urgent                   |

| Worker Code | Service Name           | Base Price Min | Base Price Max | Worker Price Min | Worker Price Max | Unit     | Alasan Variasi        |
| ----------- | ---------------------- | -------------: | -------------: | ---------------: | ---------------: | -------- | --------------------- |
| AC-KAB-001  | Cuci AC split 0.5–2 PK |          75000 |         150000 |            75000 |           105000 | per unit | Kabupaten dan junior  |
| AC-KSD-002  | Cuci AC split 0.5–2 PK |          75000 |         150000 |            90000 |           130000 | per unit | Kota sedang standard  |
| AC-SBY-003  | Cuci AC split 0.5–2 PK |          75000 |         150000 |           120000 |           175000 | per unit | Kota besar dan senior |
| AC-JKT-004  | Cuci AC inverter       |         120000 |         225000 |           175000 |           315000 | per unit | Specialist inverter   |
| AC-EMG-005  | Cuci AC split 0.5–2 PK |          75000 |         150000 |           150000 |           250000 | per unit | Emergency 24 jam      |

## Tukang Listrik

| Worker Code | Nama Worker          | Kota/Tier   | Experience | Rating | Completed Jobs | Positioning | Base Visit Fee | Adjustment | Alasan Harga                   |
| ----------- | -------------------- | ----------- | ---------- | -----: | -------------: | ----------- | -------------: | ---------: | ------------------------------ |
| EL-KAB-001  | Joko Listrik Rumah   | Kabupaten   | Junior     |    4.2 |             35 | Budget      |          30000 |       -10% | Cocok pekerjaan kecil          |
| EL-KSD-002  | Taufik Elektro       | Kota Sedang | Mid        |    4.5 |            120 | Standard    |          50000 |         0% | Harga normal                   |
| EL-SBY-003  | Surya Instalasi      | Kota Besar  | Senior     |    4.8 |            260 | Premium     |          75000 |       +20% | Berpengalaman instalasi rumah  |
| EL-JKT-004  | Panel Aman Teknik    | Kota Besar  | Specialist |    4.9 |            360 | Premium     |         100000 |       +45% | Spesialis panel dan korsleting |
| EL-EMG-005  | Listrik Cepat 24 Jam | Kota Besar  | Senior     |    4.7 |            240 | Emergency   |         120000 |       +50% | Panggilan malam dan urgent     |

| Worker Code | Service Name                | Base Price Min | Base Price Max | Worker Price Min | Worker Price Max | Unit          | Alasan Variasi           |
| ----------- | --------------------------- | -------------: | -------------: | ---------------: | ---------------: | ------------- | ------------------------ |
| EL-KAB-001  | Pasang stop kontak          |         125000 |         300000 |           110000 |           220000 | per titik     | Budget kabupaten         |
| EL-KSD-002  | Pasang stop kontak          |         125000 |         300000 |           140000 |           275000 | per titik     | Standard kota sedang     |
| EL-SBY-003  | Pasang stop kontak          |         125000 |         300000 |           180000 |           350000 | per titik     | Senior kota besar        |
| EL-JKT-004  | Perbaikan korsleting ringan |         150000 |         600000 |           300000 |           850000 | per pekerjaan | Specialist risiko tinggi |
| EL-EMG-005  | Perbaikan korsleting ringan |         150000 |         600000 |           350000 |           950000 | per pekerjaan | Emergency malam          |

## Tukang Pipa / Ledeng

| Worker Code | Nama Worker           | Kota/Tier   | Experience | Rating | Completed Jobs | Positioning | Base Visit Fee | Adjustment | Alasan Harga            |
| ----------- | --------------------- | ----------- | ---------- | -----: | -------------: | ----------- | -------------: | ---------: | ----------------------- |
| PL-KAB-001  | Pak Slamet Ledeng     | Kabupaten   | Junior     |    4.2 |             52 | Budget      |          30000 |       -10% | Harga terjangkau        |
| PL-KSD-002  | Hendra Plumbing       | Kota Sedang | Mid        |    4.5 |            140 | Standard    |          50000 |         0% | Harga pasar normal      |
| PL-SBY-003  | Master Pipa Surabaya  | Kota Besar  | Senior     |    4.8 |            280 | Premium     |          75000 |       +25% | Cepat dan berpengalaman |
| PL-JKT-004  | Drain Specialist      | Kota Besar  | Specialist |    4.9 |            390 | Premium     |          90000 |       +45% | Spesialis mampet berat  |
| PL-EMG-005  | Ledeng Darurat 24 Jam | Kota Besar  | Senior     |    4.7 |            230 | Emergency   |         120000 |       +50% | Panggilan urgent        |

| Worker Code | Service Name                | Base Price Min | Base Price Max | Worker Price Min | Worker Price Max | Unit          | Alasan Variasi         |
| ----------- | --------------------------- | -------------: | -------------: | ---------------: | ---------------: | ------------- | ---------------------- |
| PL-KAB-001  | Perbaikan pipa bocor ringan |         100000 |         300000 |            90000 |           220000 | per titik     | Budget kabupaten       |
| PL-KSD-002  | Perbaikan pipa bocor ringan |         100000 |         300000 |           125000 |           300000 | per titik     | Standard               |
| PL-SBY-003  | Perbaikan pipa bocor ringan |         100000 |         300000 |           175000 |           400000 | per titik     | Senior kota besar      |
| PL-JKT-004  | Kloset mampet berat         |         500000 |        1250000 |           750000 |          1800000 | per pekerjaan | Specialist alat khusus |
| PL-EMG-005  | Saluran mampet ringan       |         250000 |         600000 |           450000 |          1000000 | per pekerjaan | Emergency              |

## Tukang Bangunan Umum

| Worker Code | Nama Worker         | Kota/Tier   | Experience | Rating | Completed Jobs | Positioning | Base Visit Fee | Adjustment | Alasan Harga                  |
| ----------- | ------------------- | ----------- | ---------- | -----: | -------------: | ----------- | -------------: | ---------: | ----------------------------- |
| BG-KAB-001  | Kuli Harian Pak Man | Kabupaten   | Junior     |    4.1 |             60 | Budget      |              0 |       -15% | Upah harian lokal             |
| BG-KSD-002  | Tukang Rapi Mandiri | Kota Sedang | Mid        |    4.5 |            145 | Standard    |              0 |         0% | Pekerjaan umum                |
| BG-SBY-003  | Finishing Jaya      | Kota Besar  | Senior     |    4.8 |            300 | Premium     |              0 |       +25% | Spesialis finishing           |
| BG-JKT-004  | Mandor Pro Renovasi | Kota Besar  | Specialist |    4.9 |            420 | Premium     |              0 |       +40% | Koordinasi pekerjaan kompleks |
| BG-EMG-005  | Tukang Cepat Harian | Kota Besar  | Senior     |    4.6 |            190 | Emergency   |          50000 |       +35% | Panggilan cepat               |

| Worker Code | Service Name               | Base Price Min | Base Price Max | Worker Price Min | Worker Price Max | Unit      | Alasan Variasi        |
| ----------- | -------------------------- | -------------: | -------------: | ---------------: | ---------------: | --------- | --------------------- |
| BG-KAB-001  | Tukang bangunan standar    |         120000 |         200000 |           110000 |           160000 | per hari  | Kabupaten             |
| BG-KSD-002  | Tukang bangunan standar    |         120000 |         200000 |           140000 |           200000 | per hari  | Standard              |
| BG-SBY-003  | Tukang finishing           |         175000 |         275000 |           220000 |           350000 | per hari  | Senior finishing      |
| BG-JKT-004  | Mandor                     |         200000 |         350000 |           300000 |           500000 | per hari  | Specialist kota besar |
| BG-EMG-005  | Paket setengah hari tukang |         250000 |         600000 |           350000 |           750000 | per paket | Cepat dan urgent      |

## Tukang Cat

| Worker Code | Nama Worker         | Kota/Tier   | Experience | Rating | Completed Jobs | Positioning | Base Visit Fee | Adjustment | Alasan Harga                      |
| ----------- | ------------------- | ----------- | ---------- | -----: | -------------: | ----------- | -------------: | ---------: | --------------------------------- |
| CT-KAB-001  | Cat Hemat Pak Narto | Kabupaten   | Junior     |    4.2 |             50 | Budget      |          30000 |       -10% | Harga rendah untuk luas kecil     |
| CT-KSD-002  | Warna Rapi          | Kota Sedang | Mid        |    4.5 |            130 | Standard    |          50000 |         0% | Harga normal                      |
| CT-SBY-003  | Finishing Paint Pro | Kota Besar  | Senior     |    4.8 |            290 | Premium     |          75000 |       +25% | Hasil rapi                        |
| CT-JKT-004  | Exterior Specialist | Kota Besar  | Specialist |    4.9 |            340 | Premium     |          90000 |       +40% | Spesialis exterior dan anti bocor |
| CT-EMG-005  | Cat Kilat 24 Jam    | Kota Besar  | Senior     |    4.6 |            170 | Emergency   |         100000 |       +35% | Deadline cepat                    |

| Worker Code | Service Name           | Base Price Min | Base Price Max | Worker Price Min | Worker Price Max | Unit      | Alasan Variasi      |
| ----------- | ---------------------- | -------------: | -------------: | ---------------: | ---------------: | --------- | ------------------- |
| CT-KAB-001  | Cat interior jasa saja |          18000 |          30000 |            16000 |            24000 | per m2    | Budget              |
| CT-KSD-002  | Cat interior jasa saja |          18000 |          30000 |            20000 |            32000 | per m2    | Standard            |
| CT-SBY-003  | Cat interior jasa saja |          18000 |          30000 |            26000 |            40000 | per m2    | Senior              |
| CT-JKT-004  | Cat exterior jasa saja |          21000 |          40000 |            35000 |            65000 | per m2    | Specialist exterior |
| CT-EMG-005  | Cat ulang kamar cepat  |         250000 |         900000 |           450000 |          1250000 | per paket | Deadline cepat      |

## Tukang Keramik

| Worker Code | Nama Worker          | Kota/Tier   | Experience | Rating | Completed Jobs | Positioning | Base Visit Fee | Adjustment | Alasan Harga             |
| ----------- | -------------------- | ----------- | ---------- | -----: | -------------: | ----------- | -------------: | ---------: | ------------------------ |
| KR-KAB-001  | Pasang Keramik Hemat | Kabupaten   | Junior     |    4.2 |             47 | Budget      |          30000 |       -10% | Pekerjaan standar        |
| KR-KSD-002  | Keramik Rapi         | Kota Sedang | Mid        |    4.6 |            150 | Standard    |          50000 |         0% | Harga normal             |
| KR-SBY-003  | Granit Presisi       | Kota Besar  | Senior     |    4.8 |            310 | Premium     |          75000 |       +25% | Presisi tinggi           |
| KR-JKT-004  | Tile Specialist      | Kota Besar  | Specialist |    4.9 |            360 | Premium     |          90000 |       +45% | Granit besar dan dinding |
| KR-EMG-005  | Keramik Cepat        | Kota Besar  | Senior     |    4.6 |            160 | Emergency   |         100000 |       +30% | Deadline cepat           |

| Worker Code | Service Name                | Base Price Min | Base Price Max | Worker Price Min | Worker Price Max | Unit          | Alasan Variasi |
| ----------- | --------------------------- | -------------: | -------------: | ---------------: | ---------------: | ------------- | -------------- |
| KR-KAB-001  | Pasang keramik lantai 40x40 |          50000 |          90000 |            45000 |            75000 | per m2        | Budget         |
| KR-KSD-002  | Pasang keramik lantai 40x40 |          50000 |          90000 |            55000 |            95000 | per m2        | Standard       |
| KR-SBY-003  | Pasang keramik lantai 60x60 |          60000 |         110000 |            85000 |           150000 | per m2        | Senior         |
| KR-JKT-004  | Pasang granit besar         |          90000 |         175000 |           140000 |           260000 | per m2        | Specialist     |
| KR-EMG-005  | Perbaikan keramik kopong    |         100000 |         500000 |           200000 |           750000 | per pekerjaan | Cepat          |

## Kategori Lain: Worker Variatif Ringkas

| Worker Code | Category               | Nama Worker           | Kota/Tier   | Experience | Rating | Completed Jobs | Positioning | Base Visit Fee | Adjustment | Layanan Contoh              | Worker Price Min | Worker Price Max | Unit          |
| ----------- | ---------------------- | --------------------- | ----------- | ---------- | -----: | -------------: | ----------- | -------------: | ---------: | --------------------------- | ---------------: | ---------------: | ------------- |
| PF-KAB-001  | tukang_plafon          | Plafon Hemat          | Kabupaten   | Junior     |    4.2 |             40 | Budget      |          30000 |       -10% | Plafon gypsum jasa saja     |            45000 |            75000 | per m2        |
| PF-KSD-002  | tukang_plafon          | Gypsum Rapi           | Kota Sedang | Mid        |    4.5 |            120 | Standard    |          50000 |         0% | Plafon gypsum plus material |           150000 |           220000 | per m2        |
| PF-SBY-003  | tukang_plafon          | PVC Premium           | Kota Besar  | Senior     |    4.8 |            260 | Premium     |          75000 |       +25% | Plafon PVC plus material    |           220000 |           350000 | per m2        |
| PF-JKT-004  | tukang_plafon          | GRC Specialist        | Kota Besar  | Specialist |    4.9 |            300 | Premium     |          90000 |       +40% | Plafon GRC plus material    |           250000 |           420000 | per m2        |
| PF-EMG-005  | tukang_plafon          | Plafon Cepat          | Kota Besar  | Senior     |    4.6 |            150 | Emergency   |         100000 |       +35% | Perbaikan plafon bocor      |           350000 |          1200000 | per pekerjaan |
| KY-KAB-001  | tukang_kayu            | Kayu Hemat            | Kabupaten   | Junior     |    4.1 |             38 | Budget      |          30000 |       -10% | Pasang engsel pintu         |            75000 |           180000 | per pekerjaan |
| KY-KSD-002  | tukang_kayu            | Kayu Rapi             | Kota Sedang | Mid        |    4.5 |            115 | Standard    |          50000 |         0% | Perbaikan pintu kayu        |           120000 |           450000 | per pekerjaan |
| KY-SBY-003  | tukang_kayu            | Furniture Pro         | Kota Besar  | Senior     |    4.8 |            240 | Premium     |          75000 |       +25% | Perbaikan lemari            |           250000 |           950000 | per pekerjaan |
| KY-JKT-004  | tukang_kayu            | Custom Interior       | Kota Besar  | Specialist |    4.9 |            310 | Premium     |         100000 |       +45% | Kitchen set sederhana       |          2500000 |         12000000 | per paket     |
| KY-EMG-005  | tukang_kayu            | Pintu Cepat           | Kota Besar  | Senior     |    4.6 |            140 | Emergency   |         100000 |       +35% | Serut pintu seret           |           200000 |           550000 | per pekerjaan |
| AT-KAB-001  | tukang_atap            | Genteng Lokal         | Kabupaten   | Junior     |    4.2 |             45 | Budget      |          30000 |       -10% | Ganti genteng pecah         |           125000 |           400000 | per pekerjaan |
| AT-KSD-002  | tukang_atap            | Atap Aman             | Kota Sedang | Mid        |    4.5 |            130 | Standard    |          50000 |         0% | Inspeksi kebocoran atap     |           100000 |           300000 | per kunjungan |
| AT-SBY-003  | tukang_atap            | Anti Bocor Pro        | Kota Besar  | Senior     |    4.8 |            260 | Premium     |          75000 |       +25% | Waterproofing dak kecil     |            75000 |           200000 | per m2        |
| AT-JKT-004  | tukang_atap            | Rangka Specialist     | Kota Besar  | Specialist |    4.9 |            320 | Premium     |         100000 |       +45% | Perbaikan rangka atap       |           900000 |          3500000 | per pekerjaan |
| AT-EMG-005  | tukang_atap            | Atap Darurat          | Kota Besar  | Senior     |    4.6 |            180 | Emergency   |         120000 |       +50% | Tambal bocor darurat        |           400000 |          1500000 | per pekerjaan |
| PA-KAB-001  | tukang_pompa_air       | Pompa Hemat           | Kabupaten   | Junior     |    4.2 |             50 | Budget      |          30000 |       -10% | Pancing pompa               |            90000 |           220000 | per pekerjaan |
| PA-KSD-002  | tukang_pompa_air       | Pompa Normal          | Kota Sedang | Mid        |    4.5 |            130 | Standard    |          50000 |         0% | Ganti kapasitor pompa       |           150000 |           350000 | per pekerjaan |
| PA-SBY-003  | tukang_pompa_air       | Jet Pump Pro          | Kota Besar  | Senior     |    4.8 |            250 | Premium     |          75000 |       +25% | Pasang pompa baru           |           450000 |          1200000 | per pekerjaan |
| PA-JKT-004  | tukang_pompa_air       | Pressure Specialist   | Kota Besar  | Specialist |    4.9 |            310 | Premium     |          90000 |       +40% | Setting pressure switch     |           180000 |           450000 | per pekerjaan |
| PA-EMG-005  | tukang_pompa_air       | Pompa Darurat         | Kota Besar  | Senior     |    4.6 |            170 | Emergency   |         120000 |       +50% | Pompa tidak menyala         |           400000 |          1200000 | per pekerjaan |
| CV-KAB-001  | tukang_cctv_smart_home | CCTV Hemat            | Kabupaten   | Junior     |    4.2 |             35 | Budget      |          30000 |       -10% | Pasang kamera WiFi          |            90000 |           240000 | per titik     |
| CV-KSD-002  | tukang_cctv_smart_home | CCTV Rapi             | Kota Sedang | Mid        |    4.5 |            115 | Standard    |          50000 |         0% | Pasang kamera CCTV          |           150000 |           400000 | per titik     |
| CV-SBY-003  | tukang_cctv_smart_home | Security Pro          | Kota Besar  | Senior     |    4.8 |            240 | Premium     |          75000 |       +25% | Setting DVR/NVR             |           250000 |           700000 | per pekerjaan |
| CV-JKT-004  | tukang_cctv_smart_home | Smart Home Specialist | Kota Besar  | Specialist |    4.9 |            300 | Premium     |         100000 |       +45% | Pasang smart switch         |           250000 |           800000 | per titik     |
| CV-EMG-005  | tukang_cctv_smart_home | CCTV Darurat          | Kota Besar  | Senior     |    4.6 |            150 | Emergency   |         120000 |       +50% | Perbaikan kamera offline    |           300000 |           900000 | per pekerjaan |

---

# Aturan Deteksi Harga Tidak Wajar

## Rule Harga

| Kondisi                                          | Decision          | Risk Flag            | Severity | Catatan                                            |
| ------------------------------------------------ | ----------------- | -------------------- | -------- | -------------------------------------------------- |
| harga_input berada dalam price_min–price_max     | wajar             | tidak ada            | none     | Sesuai referensi                                   |
| harga_input > price_max sampai 1.5x price_max    | perlu klarifikasi | harga_tidak_wajar    | low      | Bisa wajar jika worker premium / lokasi kota besar |
| harga_input > 1.5x price_max sampai 2x price_max | perlu klarifikasi | harga_tidak_wajar    | medium   | Perlu alasan jelas                                 |
| harga_input > 2x price_max                       | tidak wajar       | harga_tidak_wajar    | high     | Kecuali ada material besar atau scope tambahan     |
| harga_input < 0.5x price_min                     | perlu klarifikasi | data_tidak_lengkap   | medium   | Bisa salah satuan atau harga belum lengkap         |
| satuan tidak jelas                               | perlu klarifikasi | data_tidak_lengkap   | medium   | Tanyakan per unit/per m2/per titik                 |
| item/layanan tidak relevan dengan order          | tidak wajar       | item_tidak_relevan   | high     | Tanyakan alasan relevansi                          |
| alasan pembelian tidak ada                       | perlu klarifikasi | alasan_tidak_lengkap | medium   | Tanyakan alasan kebutuhan                          |
| layanan sama sudah dicatat sebelumnya            | perlu klarifikasi | duplikat             | medium   | Cek apakah pembelian tambahan atau double input    |

## Rule Variasi Worker

Harga worker tidak otomatis salah jika lebih mahal dari referensi umum. AI harus mengecek:

* worker verified atau tidak,
* rating,
* completed jobs,
* city_tier,
* experience_level,
* emergency,
* apakah termasuk material,
* tingkat kesulitan,
* kondisi akses lapangan.

Contoh:
Harga cuci AC Rp175.000/unit bisa terlihat tinggi dibanding baseline Rp75.000–Rp150.000. Namun bisa tetap wajar jika worker senior verified di kota besar atau menangani AC inverter.

---

# Contoh Evaluasi Harga

## Contoh 1

Order: Perbaikan pipa wastafel bocor.
Input worker: Jasa perbaikan pipa Rp150.000.
Harga referensi: Rp100.000–Rp300.000 per titik.
Analisis: Harga berada dalam rentang wajar.
Decision: wajar.
Risk flag: tidak ada.
Clarification question: tidak perlu.

## Contoh 2

Order: Perbaikan pipa wastafel bocor.
Input worker: Cat tembok Rp1.000.000.
Harga referensi: cat tidak relevan dengan pipa bocor.
Analisis: Item tidak sesuai konteks order.
Decision: tidak wajar.
Risk flag: item_tidak_relevan, alasan_tidak_lengkap.
Clarification question: Mengapa cat tembok diperlukan untuk perbaikan pipa wastafel bocor?

## Contoh 3

Order: AC tidak dingin.
Input worker: Cuci AC Rp90.000.
Harga referensi: Rp75.000–Rp150.000 per unit.
Analisis: Harga wajar.
Decision: wajar.
Risk flag: tidak ada.
Clarification question: tidak perlu.

## Contoh 4

Order: AC tidak dingin.
Input worker: Isi freon Rp800.000.
Harga referensi: Rp350.000–Rp600.000 per unit.
Analisis: Di atas rentang, perlu cek jenis freon, kebocoran, dan sparepart.
Decision: perlu klarifikasi.
Risk flag: harga_tidak_wajar.
Clarification question: Apakah harga Rp800.000 sudah termasuk perbaikan kebocoran, jenis freon tertentu, atau sparepart tambahan?

## Contoh 5

Order: Listrik korslet.
Input worker: Inspeksi listrik Rp85.000.
Harga referensi: Rp75.000–Rp175.000 per kunjungan.
Analisis: Harga wajar.
Decision: wajar.
Risk flag: tidak ada.
Clarification question: tidak perlu.

## Contoh 6

Order: Pasang stop kontak.
Input worker: Pasang stop kontak Rp500.000 per titik.
Harga referensi: Rp125.000–Rp300.000 per titik.
Analisis: Di atas referensi, bisa wajar jika termasuk kabel tanam dan material.
Decision: perlu klarifikasi.
Risk flag: harga_tidak_wajar, data_tidak_lengkap.
Clarification question: Apakah harga tersebut sudah termasuk kabel, pipa conduit, stop kontak, dan bobok tembok?

## Contoh 7

Order: Cat kamar.
Input worker: Jasa cat Rp25.000/m2.
Harga referensi: Rp18.000–Rp30.000/m2.
Analisis: Harga wajar.
Decision: wajar.
Risk flag: tidak ada.
Clarification question: tidak perlu.

## Contoh 8

Order: Plafon bocor.
Input worker: Pasang plafon PVC Rp250.000/m2.
Harga referensi: Rp175.000–Rp275.000/m2 plus material.
Analisis: Masih dalam rentang wajar jika termasuk material.
Decision: wajar.
Risk flag: tidak ada.
Clarification question: Apakah harga sudah termasuk rangka dan material PVC?

## Contoh 9

Order: Keramik kamar mandi.
Input worker: Pasang keramik Rp300.000/m2.
Harga referensi: Rp75.000–Rp150.000/m2 untuk dinding, tenaga saja.
Analisis: Terlalu tinggi jika jasa saja, mungkin termasuk material.
Decision: perlu klarifikasi.
Risk flag: harga_tidak_wajar, data_tidak_lengkap.
Clarification question: Apakah Rp300.000/m2 sudah termasuk keramik, semen, pasir, nat, dan waterproofing?

## Contoh 10

Order: Pompa air mati.
Input worker: Ganti kapasitor Rp150.000.
Harga referensi: Rp150.000–Rp350.000.
Analisis: Harga wajar.
Decision: wajar.
Risk flag: tidak ada.
Clarification question: tidak perlu.

## Contoh 11

Order: Kloset mampet.
Input worker: Perbaikan kloset mampet Rp1.500.000.
Harga referensi: Rp500.000–Rp1.250.000.
Analisis: Di atas rentang, mungkin karena mampet berat atau alat khusus.
Decision: perlu klarifikasi.
Risk flag: harga_tidak_wajar.
Clarification question: Apakah diperlukan alat khusus atau pembongkaran tambahan?

## Contoh 12

Order: Pasang kamera CCTV.
Input worker: Pasang 1 titik CCTV Rp200.000.
Harga referensi: Rp150.000–Rp400.000 per titik.
Analisis: Harga wajar.
Decision: wajar.
Risk flag: tidak ada.
Clarification question: tidak perlu.

## Contoh 13

Order: Perbaikan atap bocor.
Input worker: Tambal bocor darurat Rp1.200.000.
Harga referensi: Rp200.000–Rp900.000.
Analisis: Agak tinggi, bisa wajar jika emergency dan akses sulit.
Decision: perlu klarifikasi.
Risk flag: harga_tidak_wajar.
Clarification question: Apakah pekerjaan dilakukan darurat, di area tinggi, atau termasuk material waterproofing?

## Contoh 14

Order: Pasang shower.
Input worker: Pasang shower Rp180.000.
Harga referensi: Rp150.000–Rp450.000.
Analisis: Harga wajar.
Decision: wajar.
Risk flag: tidak ada.
Clarification question: tidak perlu.

## Contoh 15

Order: Pasang smart lock.
Input worker: Pasang smart lock Rp750.000.
Harga referensi: Rp250.000–Rp900.000.
Analisis: Harga wajar jika termasuk setting aplikasi.
Decision: wajar.
Risk flag: tidak ada.
Clarification question: Apakah sudah termasuk setup aplikasi dan kalibrasi?

---

# Sinonim Keyword Kategori

| Kategori               | Sinonim / Keyword                                                |
| ---------------------- | ---------------------------------------------------------------- |
| tukang_ac              | ac, service ac, cuci ac, freon, inverter, outdoor ac, indoor ac  |
| tukang_listrik         | listrik, stop kontak, saklar, kabel, mcb, korslet, lampu, panel  |
| tukang_pipa            | pipa, ledeng, plumbing, bocor, mampet, keran, wastafel, shower   |
| tukang_bangunan        | bangunan, renovasi, plester, aci, cor, bata, dinding             |
| tukang_cat             | cat, pengecatan, cat dinding, cat exterior, cat interior, plamir |
| tukang_plafon          | plafon, gypsum, pvc, grc, list plafon, compound                  |
| tukang_keramik         | keramik, granit, nat, lantai, backsplash, kamar mandi            |
| tukang_kayu            | kayu, pintu, lemari, rak, engsel, furniture, laci                |
| tukang_kunci           | kunci, pintu terkunci, silinder, handle, smart lock              |
| tukang_atap            | atap, genteng, bocor, nok, talang, waterproofing                 |
| tukang_kanopi          | kanopi, baja ringan, spandek, polycarbonate, rangka              |
| tukang_pompa_air       | pompa, jet pump, kapasitor, otomatis pompa, pressure switch      |
| tukang_water_heater    | water heater, pemanas air, safety valve, flushing                |
| tukang_cctv_smart_home | cctv, kamera, dvr, nvr, smart switch, smart home                 |
| tukang_taman           | taman, kebun, rumput, tanaman, koral, pangkas                    |
| tukang_las             | las, besi, pagar, teralis, railing, bracket                      |
| tukang_aluminium_kaca  | aluminium, kaca, sliding, kusen, sealant                         |
| tukang_sanitasi        | sanitasi, closet, shower, wastafel, floor drain, kamar mandi     |
| tukang_renovasi_kecil  | renovasi kecil, perbaikan rumah, dapur kecil, kamar kecil        |
| survey_inspeksi        | survey, inspeksi, rab, kunjungan, konsultasi teknis              |

---

# Rekomendasi Chunking untuk RAG

Agar retrieval lebih akurat, pisahkan dokumen menjadi beberapa file:

1. `price-principles.md`
   Berisi prinsip harga, multiplier lokasi, dan rule deteksi harga tidak wajar.

2. `service-price-reference-ac-listrik-pipa.md`
   Berisi harga referensi AC, listrik, pipa.

3. `service-price-reference-bangunan-finishing.md`
   Berisi harga bangunan, cat, plafon, keramik, renovasi kecil.

4. `service-price-reference-specialist.md`
   Berisi CCTV, smart home, water heater, pompa, las, aluminium, kaca.

5. `worker-pricing-variation.md`
   Berisi profil worker dan variasi harga antar-worker.

6. `price-evaluation-examples.md`
   Berisi contoh evaluasi harga dan risk flag.

Rekomendasi chunk:

* chunk_size: 700–1000 karakter
* chunk_overlap: 100–150 karakter
* metadata wajib: source, category, service_name, doc_type, updated_year
* doc_type: price_reference, worker_variation, risk_rule, example

---

# Disclaimer

Harga dalam dataset ini adalah estimasi pasar untuk membantu AI melakukan validasi awal. Harga final tetap perlu dikonfirmasi berdasarkan lokasi, tingkat kesulitan, pengalaman worker, waktu pengerjaan, material, dan kondisi lapangan. AI tidak boleh langsung menolak harga hanya karena berbeda dari referensi; AI harus memberi klarifikasi jika ada faktor yang belum jelas.
