# FAQ SiTukang untuk User dan Worker

## User

### Bagaimana cara memesan tukang?

User memilih kategori jasa, memilih worker, mengisi detail masalah, memasukkan lokasi, memilih jadwal, lalu membuat order.

### Bagaimana cara mengecek status order?

User dapat melihat tracking order dari status:
- pending
- accepted
- on_the_way
- arrived
- in_progress
- completed
- cancelled
- rejected

### Apa itu purchase tracking?

Purchase tracking adalah fitur untuk mencatat pembelian material atau biaya tambahan yang diajukan worker selama mengerjakan order.

### Bagaimana cara menyetujui pembelian material?

User melihat daftar purchase yang diajukan worker, membaca alasan pembelian, melihat nota jika ada, lalu memilih approve, reject, atau minta klarifikasi.

### Apa arti risk flag harga_tidak_wajar?

Risk flag `harga_tidak_wajar` berarti harga yang dimasukkan worker berbeda jauh dari harga patokan di knowledge base.

### Apa arti risk flag item_tidak_relevan?

Risk flag `item_tidak_relevan` berarti item atau layanan yang dimasukkan worker tidak sesuai dengan konteks order.

### Apakah AI langsung menolak pembelian?

Tidak. AI hanya memberi analisis, risk flag, dan pertanyaan klarifikasi. Keputusan akhir tetap dapat dikonfirmasi oleh user atau sistem approval.

### Apakah harga patokan adalah harga final?

Tidak. Harga patokan adalah baseline untuk membantu validasi. Harga final dapat berbeda karena lokasi, material, kesulitan, worker senior, atau emergency.

## Worker

### Bagaimana worker mencatat pembelian material?

Worker memasukkan nama item, jumlah, satuan, harga, alasan pembelian, dan nota jika tersedia.

### Apa fungsi AI pada purchase tracking?

AI membantu merapikan input pembelian, mengecek harga patokan, mendeteksi risk flag, dan membuat pertanyaan klarifikasi.

### Apa yang terjadi jika harga terlalu mahal?

Sistem memberi risk flag `harga_tidak_wajar` dan user dapat meminta klarifikasi.

### Bagaimana agar pembelian tidak ditandai mencurigakan?

Worker harus mengisi:
- nama item jelas,
- jumlah jelas,
- satuan jelas,
- harga jelas,
- alasan pembelian jelas,
- nota jika tersedia.

### Apa contoh alasan pembelian yang baik?

Contoh:
- "Pipa PVC 2 meter diperlukan untuk mengganti bagian pipa wastafel yang bocor."
- "Kapasitor AC diganti karena kompresor tidak menyala."
- "Stop kontak baru dipasang karena titik lama terbakar akibat korsleting."

### Apa contoh alasan pembelian yang kurang baik?

Contoh:
- "Beli tambahan."
- "Butuh aja."
- "Barang kerja."
- "Biaya lain-lain."

### Apa yang harus dilakukan jika AI meminta klarifikasi?

Worker harus menjawab pertanyaan klarifikasi dengan detail, misalnya menjelaskan jumlah, satuan, alasan, dan apakah harga termasuk material atau jasa.

## Admin

### Apa fungsi knowledge base?

Knowledge base digunakan untuk memberi konteks kepada AI agar jawaban dan validasi tidak hanya berdasarkan pengetahuan umum model.

### Data apa yang sebaiknya masuk Qdrant?

Data yang cocok masuk Qdrant:
- profil aplikasi,
- FAQ,
- aturan validasi harga,
- harga patokan jasa,
- harga patokan material,
- mapping relevansi order,
- contoh evaluasi.

Data yang tidak sebaiknya masuk Qdrant:
- password hash,
- token,
- data pribadi user,
- alamat lengkap user,
- transaksi sensitif,
- chat pribadi.
