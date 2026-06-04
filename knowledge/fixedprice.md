# Fixed Price Knowledge Base Jasa Tukang Indonesia 2026 untuk SiTukang

## Status Data

Dataset ini menggunakan harga patokan tunggal, bukan kisaran. Harga patokan dipakai agar RAG tidak menjawab dengan kata "kisaran" terus-menerus.

Harga patokan ini bukan harga resmi nasional. Harga ini adalah baseline operasional untuk AI SiTukang berdasarkan kurasi harga vendor, marketplace jasa, dan referensi publik Indonesia 2025–2026.

Aturan jawaban AI:
- Jawab dengan harga patokan tunggal.
- Jangan menjawab dengan kisaran kecuali user meminta perbandingan harga.
- Jika harga aktual worker berbeda dari harga patokan, jelaskan apakah selisihnya masih wajar berdasarkan lokasi, pengalaman, emergency, atau material.
- Jika layanan tidak ada di data, katakan "harga patokan belum tersedia di knowledge base".

---

# Pricing Rules

## Rule Umum

- `harga_patokan` adalah angka utama yang dipakai AI untuk menjawab.
- `tolerance_low_percent` adalah batas bawah toleransi.
- `tolerance_high_percent` adalah batas atas toleransi.
- Jika harga worker melebihi toleransi atas, beri risk flag `harga_tidak_wajar`.
- Jika harga worker jauh di bawah toleransi bawah, beri risk flag `data_tidak_lengkap`.
- Jika layanan tidak relevan dengan order, beri risk flag `item_tidak_relevan`.
- Jika alasan pekerjaan tidak jelas, beri risk flag `alasan_tidak_lengkap`.

## Default Tolerance

| Kondisi | Toleransi |
|---|---:|
| Kota kecil / kabupaten | -15% sampai +5% |
| Kota sedang | -10% sampai +15% |
| Kota besar | 0% sampai +30% |
| Worker senior verified | 0% sampai +35% |
| Worker specialist | 0% sampai +50% |
| Emergency malam / hari libur | +20% sampai +50% |

---

# Fixed Price Service Data

## Tukang AC

| service_code | category | service_name | harga_patokan | unit | includes_material | pricing_method | source_note |
|---|---|---|---:|---|---|---|---|
| AC-001 | tukang_ac | Cuci AC Split 0.5–2 PK | 90000 | per unit | false | median_vendor_price | Dipatok dari harga cuci AC 0.5–2 PK Rp85.000–Rp95.000 |
| AC-002 | tukang_ac | Cuci AC Inverter 0.5–2 PK | 140000 | per unit | false | median_vendor_price | Dipatok dari harga cuci AC inverter Rp130.000–Rp150.000 |
| AC-003 | tukang_ac | Tambah Freon R22 0.5–1 PK | 175000 | per unit | true | listed_vendor_price | Harga sumber tunggal |
| AC-004 | tukang_ac | Tambah Freon R22 1.5–2 PK | 225000 | per unit | true | listed_vendor_price | Harga sumber tunggal |
| AC-005 | tukang_ac | Tambah Freon R32/R410 0.5–1 PK | 225000 | per unit | true | listed_vendor_price | Harga sumber tunggal |
| AC-006 | tukang_ac | Tambah Freon R32/R410 1.5–2 PK | 275000 | per unit | true | listed_vendor_price | Harga sumber tunggal |
| AC-007 | tukang_ac | Isi Freon R22 0.5–1 PK | 275000 | per unit | true | listed_vendor_price | Harga sumber tunggal |
| AC-008 | tukang_ac | Isi Freon R22 1.5–2 PK | 325000 | per unit | true | listed_vendor_price | Harga sumber tunggal |
| AC-009 | tukang_ac | Isi Freon R32/R410 0.5–1 PK | 350000 | per unit | true | listed_vendor_price | Harga sumber tunggal |
| AC-010 | tukang_ac | Isi Freon R32/R410 1.5–2 PK | 450000 | per unit | true | listed_vendor_price | Harga sumber tunggal |
| AC-011 | tukang_ac | Bongkar AC 0.5–2 PK | 250000 | per pekerjaan | false | listed_vendor_price | Harga vendor Surabaya |
| AC-012 | tukang_ac | Pasang AC 0.5–1 PK | 350000 | per pekerjaan | false | listed_vendor_price | Harga vendor Surabaya |

## Tukang Listrik

| service_code | category | service_name | harga_patokan | unit | includes_material | pricing_method | source_note |
|---|---|---|---:|---|---|---|---|
| EL-001 | tukang_listrik | Inspeksi listrik | 85000 | per kunjungan | false | listed_marketplace_price | Harga sumber tunggal |
| EL-002 | tukang_listrik | Pemasangan MCB listrik | 80000 | per pekerjaan | false | listed_marketplace_price | Harga sumber tunggal |
| EL-003 | tukang_listrik | Ganti sekring | 75000 | per pekerjaan | false | listed_marketplace_price | Harga sumber tunggal |
| EL-004 | tukang_listrik | Instalasi kabel tanpa bobok | 90000 | per titik | false | listed_marketplace_price | Harga sumber tunggal |
| EL-005 | tukang_listrik | Tambah stop kontak | 85000 | per titik | false | listed_marketplace_price | Harga sumber tunggal |
| EL-006 | tukang_listrik | Tambah titik listrik | 85000 | per titik | false | listed_marketplace_price | Harga sumber tunggal |
| EL-007 | tukang_listrik | Pemasangan grounding | 400000 | per meter | false | listed_marketplace_price | Harga sumber tunggal |
| EL-008 | tukang_listrik | Pasang stop kontak unit saja | 20000 | per unit | false | listed_vendor_price | Harga vendor instalasi |
| EL-009 | tukang_listrik | Instalasi line stop kontak | 90000 | per titik | false | listed_vendor_price | Harga vendor instalasi |
| EL-010 | tukang_listrik | Instalasi line stop kontak dengan conduit PVC | 130000 | per titik | false | listed_vendor_price | Harga vendor instalasi |
| EL-011 | tukang_listrik | Pasang stop kontak AC unit saja | 25000 | per unit | false | listed_vendor_price | Harga vendor instalasi |
| EL-012 | tukang_listrik | Instalasi line exhaust fan | 85000 | per titik | false | listed_vendor_price | Harga vendor instalasi |
| EL-013 | tukang_listrik | Pasang exhaust fan | 140000 | per unit | false | listed_vendor_price | Harga vendor instalasi |

## Tukang Pipa / Ledeng / Plumbing

| service_code | category | service_name | harga_patokan | unit | includes_material | pricing_method | source_note |
|---|---|---|---:|---|---|---|---|
| PL-001 | tukang_pipa | Perbaikan pipa ledeng bocor | 200000 | per pekerjaan | false | listed_marketplace_price | Harga sumber tunggal |
| PL-002 | tukang_pipa | Perbaikan pipa ledeng mampet | 350000 | per pekerjaan | false | listed_marketplace_price | Harga sumber tunggal |
| PL-003 | tukang_pipa | Perbaikan pipa ledeng mampet air kotor | 500000 | per pekerjaan | false | listed_marketplace_price | Harga sumber tunggal |
| PL-004 | tukang_pipa | Perbaikan wastafel atau sink | 220000 | per pekerjaan | false | listed_marketplace_price | Harga sumber tunggal |
| PL-005 | tukang_pipa | Perbaikan atau penggantian keran wastafel | 250000 | per pekerjaan | false | listed_marketplace_price | Harga sumber tunggal |
| PL-006 | tukang_pipa | Perbaikan atau penggantian keran double wastafel | 350000 | per pekerjaan | false | listed_marketplace_price | Harga sumber tunggal |
| PL-007 | tukang_pipa | Perbaikan kloset | 325000 | per pekerjaan | false | listed_marketplace_price | Harga sumber tunggal |
| PL-008 | tukang_pipa | Perbaikan kloset mampet | 500000 | per pekerjaan | false | listed_marketplace_price | Harga sumber tunggal |
| PL-009 | tukang_pipa | Ganti kloset | 500000 | per pekerjaan | false | listed_marketplace_price | Harga sumber tunggal |
| PL-010 | tukang_pipa | Perbaikan atau penggantian shower single | 200000 | per pekerjaan | false | listed_marketplace_price | Harga sumber tunggal |
| PL-011 | tukang_pipa | Perbaikan atau penggantian shower double | 350000 | per pekerjaan | false | listed_marketplace_price | Harga sumber tunggal |

## Tukang Bangunan Harian

| service_code | category | service_name | harga_patokan | unit | includes_material | pricing_method | source_note |
|---|---|---|---:|---|---|---|---|
| BG-001 | tukang_bangunan | Kuli harian standar | 90000 | per hari | false | median_public_reference | Dipatok dari range Rp80.000–Rp100.000 |
| BG-002 | tukang_bangunan | Tukang bangunan harian standar nasional | 200000 | per hari | false | operational_baseline | Patokan SiTukang untuk tukang umum |
| BG-003 | tukang_bangunan | Tukang harian Jakarta | 235000 | per hari | false | median_news_reference | Dipatok dari laporan Rp230.000–Rp240.000 |
| BG-004 | tukang_bangunan | Helper atau kenek Jakarta | 195000 | per hari | false | median_news_reference | Dipatok dari laporan Rp190.000–Rp200.000 |
| BG-005 | tukang_bangunan | Mandor | 180000 | per hari | false | listed_public_reference | Harga sumber tunggal |
| BG-006 | tukang_bangunan | Kepala tukang | 150000 | per hari | false | median_public_reference | Dipatok dari range Rp125.000–Rp175.000 |
| BG-007 | tukang_bangunan | Operator | 150000 | per hari | false | listed_public_reference | Harga sumber tunggal |
| BG-008 | tukang_bangunan | Tukang listrik harian | 115000 | per hari | false | median_public_reference | Dipatok dari range Rp110.000–Rp120.000 |
| BG-009 | tukang_bangunan | Tukang kayu harian | 120000 | per hari | false | median_public_reference | Dipatok dari range Rp110.000–Rp130.000 |
| BG-010 | tukang_bangunan | Tukang las harian | 110000 | per hari | false | listed_public_reference | Harga sumber tunggal |

## Tukang Cat

| service_code | category | service_name | harga_patokan | unit | includes_material | pricing_method | source_note |
|---|---|---|---:|---|---|---|---|
| CT-001 | tukang_cat | Borongan cat tembok jasa saja | 25000 | per m2 | false | example_public_reference | Angka contoh perhitungan jasa cat |
| CT-002 | tukang_cat | Cat tembok plus bahan Dulux | 65000 | per m2 | true | listed_public_reference | Harga sumber tunggal |
| CT-003 | tukang_cat | Cat tembok plus bahan Mowilex | 52000 | per m2 | true | listed_public_reference | Harga sumber tunggal |
| CT-004 | tukang_cat | Cat tembok plus bahan Jotun | 100000 | per m2 | true | listed_public_reference | Harga sumber tunggal |
| CT-005 | tukang_cat | Cat tembok plus bahan Vinilex | 35000 | per m2 | true | listed_public_reference | Harga sumber tunggal |
| CT-006 | tukang_cat | Cat tembok plus bahan Catylac | 35000 | per m2 | true | listed_public_reference | Harga sumber tunggal |
| CT-007 | tukang_cat | Cat tembok plus bahan No Drop | 30000 | per m2 | true | listed_public_reference | Harga sumber tunggal |
| CT-008 | tukang_cat | Cat exterior Propan Decor Shield | 25500 | per m2 | true | median_vendor_price | Dipatok dari range Rp24.000–Rp27.000 |
| CT-009 | tukang_cat | Cat exterior Dulux Weather Shield | 27500 | per m2 | true | median_vendor_price | Dipatok dari range Rp26.000–Rp29.000 |

## Tukang Keramik

| service_code | category | service_name | harga_patokan | unit | includes_material | pricing_method | source_note |
|---|---|---|---:|---|---|---|---|
| KR-001 | tukang_keramik | Pasang keramik 20x20 atau 25x25 | 52500 | per m2 | false | median_public_reference | Dipatok dari range Rp45.000–Rp60.000 |
| KR-002 | tukang_keramik | Pasang keramik 30x30 | 55000 | per m2 | false | median_public_reference | Dipatok dari range Rp45.000–Rp65.000 |
| KR-003 | tukang_keramik | Pasang keramik 40x40 | 60000 | per m2 | false | median_public_reference | Dipatok dari range Rp50.000–Rp70.000 |
| KR-004 | tukang_keramik | Pasang keramik 50x50 | 67500 | per m2 | false | median_public_reference | Dipatok dari range Rp55.000–Rp80.000 |
| KR-005 | tukang_keramik | Pasang keramik 60x60 | 75000 | per m2 | false | median_public_reference | Dipatok dari range Rp60.000–Rp90.000 |
| KR-006 | tukang_keramik | Pasang granit besar | 120000 | per m2 | false | median_public_reference | Dipatok dari range Rp90.000–Rp150.000 |
| KR-007 | tukang_keramik | Pasang keramik 60x60 jasa murah | 35000 | per m2 | false | listed_public_reference | Harga sumber contoh biaya tukang |
| KR-008 | tukang_keramik | Material keramik 60x60 standar | 80000 | per m2 | true | listed_public_reference | Harga keramik 60x60 per dus untuk 1 m2 |
| KR-009 | tukang_keramik | Semen untuk pasang keramik | 13750 | per m2 | true | calculated_public_reference | 0.25 sak dari harga semen Rp55.000 |
| KR-010 | tukang_keramik | Pasir untuk pasang keramik | 10000 | per m2 | true | listed_public_reference | Harga asumsi sumber |
| KR-011 | tukang_keramik | Semen grouting | 7500 | per m2 | true | listed_public_reference | Harga sumber contoh |

## Tukang Kanopi / Baja Ringan

| service_code | category | service_name | harga_patokan | unit | includes_material | pricing_method | source_note |
|---|---|---|---:|---|---|---|---|
| KP-001 | tukang_kanopi | Kanopi baja ringan spandek zincalume 0.35 mm | 200000 | per m2 | true | listed_vendor_price | Harga sumber tunggal |
| KP-002 | tukang_kanopi | Kanopi baja ringan spandek warna 0.35 mm | 220000 | per m2 | true | listed_vendor_price | Harga sumber tunggal |
| KP-003 | tukang_kanopi | Kanopi baja ringan spandek pasir 0.35 mm | 250000 | per m2 | true | listed_vendor_price | Harga sumber tunggal |
| KP-004 | tukang_kanopi | Kanopi genteng metal polos 0.35 mm | 220000 | per m2 | true | listed_vendor_price | Harga sumber tunggal |
| KP-005 | tukang_kanopi | Kanopi genteng metal pasir 0.35 mm | 250000 | per m2 | true | listed_vendor_price | Harga sumber tunggal |
| KP-006 | tukang_kanopi | Kanopi rangka baja ringan spandek zincalume Jakarta | 350000 | per m2 | true | listed_vendor_price | Harga sumber tunggal |
| KP-007 | tukang_kanopi | Kanopi rangka baja ringan spandek warna Jakarta | 370000 | per m2 | true | listed_vendor_price | Harga sumber tunggal |
| KP-008 | tukang_kanopi | Kanopi rangka baja ringan spandek pasir Jakarta | 380000 | per m2 | true | listed_vendor_price | Harga sumber tunggal |
| KP-009 | tukang_kanopi | Kanopi rangka baja ringan polycarbonate Jakarta | 450000 | per m2 | true | listed_vendor_price | Harga sumber tunggal |
| KP-010 | tukang_kanopi | Kanopi rangka baja ringan alderon Jakarta | 600000 | per m2 | true | listed_vendor_price | Harga sumber tunggal |
| KP-011 | tukang_kanopi | Kanopi alderon single layer | 650000 | per m2 | true | listed_vendor_price | Harga sumber tunggal |
| KP-012 | tukang_kanopi | Kanopi alderon double layer | 850000 | per m2 | true | listed_vendor_price | Harga sumber tunggal |

## Survey dan Biaya Kunjungan

| service_code | category | service_name | harga_patokan | unit | includes_material | pricing_method | source_note |
|---|---|---|---:|---|---|---|---|
| SV-001 | survey_inspeksi | Biaya kunjungan ringan | 50000 | per kunjungan | false | operational_baseline | Patokan SiTukang |
| SV-002 | survey_inspeksi | Survey teknis standar | 100000 | per kunjungan | false | operational_baseline | Patokan SiTukang |
| SV-003 | survey_inspeksi | Survey teknis detail | 150000 | per kunjungan | false | operational_baseline | Patokan SiTukang |
| SV-004 | survey_inspeksi | Survey emergency | 250000 | per kunjungan | false | operational_baseline | Patokan SiTukang |

---

# Worker Fixed Prices

Data ini menunjukkan bahwa worker berbeda dapat memiliki harga aktual berbeda walaupun layanan sama.

## Worker AC

| worker_code | worker_name | city_tier | experience | rating_avg | completed_jobs | verification_status | price_positioning | service_name | harga_worker | unit | reason |
|---|---|---|---|---:|---:|---|---|---|---:|---|---|
| AC-KAB-001 | Budi Service AC | kabupaten | junior | 4.3 | 48 | verified | budget | Cuci AC Split 0.5–2 PK | 80000 | per unit | Worker junior di kabupaten |
| AC-KSD-002 | Raka Teknik AC | kota_sedang | mid | 4.6 | 132 | verified | standard | Cuci AC Split 0.5–2 PK | 90000 | per unit | Mengikuti harga patokan |
| AC-SBY-003 | Ahmad Cooling | kota_besar | senior | 4.8 | 320 | verified | premium | Cuci AC Split 0.5–2 PK | 120000 | per unit | Senior di kota besar |
| AC-JKT-004 | Dimas Inverter Specialist | kota_besar | specialist | 4.9 | 410 | verified | specialist | Cuci AC Inverter 0.5–2 PK | 180000 | per unit | Spesialis inverter |
| AC-EMG-005 | Cepat Dingin 24 Jam | kota_besar | senior | 4.7 | 280 | verified | emergency | Cuci AC Split 0.5–2 PK | 150000 | per unit | Panggilan emergency |

## Worker Listrik

| worker_code | worker_name | city_tier | experience | rating_avg | completed_jobs | verification_status | price_positioning | service_name | harga_worker | unit | reason |
|---|---|---|---|---:|---:|---|---|---|---:|---|---|
| EL-KAB-001 | Joko Listrik Rumah | kabupaten | junior | 4.2 | 35 | verified | budget | Tambah stop kontak | 70000 | per titik | Worker junior |
| EL-KSD-002 | Taufik Elektro | kota_sedang | mid | 4.5 | 120 | verified | standard | Tambah stop kontak | 85000 | per titik | Harga patokan |
| EL-SBY-003 | Surya Instalasi | kota_besar | senior | 4.8 | 260 | verified | premium | Tambah stop kontak | 120000 | per titik | Senior kota besar |
| EL-JKT-004 | Panel Aman Teknik | kota_besar | specialist | 4.9 | 360 | verified | specialist | Instalasi kabel tanpa bobok | 150000 | per titik | Spesialis instalasi |
| EL-EMG-005 | Listrik Cepat 24 Jam | kota_besar | senior | 4.7 | 240 | verified | emergency | Inspeksi listrik | 150000 | per kunjungan | Emergency malam |

## Worker Pipa

| worker_code | worker_name | city_tier | experience | rating_avg | completed_jobs | verification_status | price_positioning | service_name | harga_worker | unit | reason |
|---|---|---|---|---:|---:|---|---|---|---:|---|---|
| PL-KAB-001 | Pak Slamet Ledeng | kabupaten | junior | 4.2 | 52 | verified | budget | Perbaikan pipa ledeng bocor | 160000 | per pekerjaan | Kabupaten dan junior |
| PL-KSD-002 | Hendra Plumbing | kota_sedang | mid | 4.5 | 140 | verified | standard | Perbaikan pipa ledeng bocor | 200000 | per pekerjaan | Harga patokan |
| PL-SBY-003 | Master Pipa Surabaya | kota_besar | senior | 4.8 | 280 | verified | premium | Perbaikan pipa ledeng bocor | 275000 | per pekerjaan | Senior kota besar |
| PL-JKT-004 | Drain Specialist | kota_besar | specialist | 4.9 | 390 | verified | specialist | Perbaikan pipa ledeng mampet air kotor | 750000 | per pekerjaan | Spesialis saluran mampet |
| PL-EMG-005 | Ledeng Darurat 24 Jam | kota_besar | senior | 4.7 | 230 | verified | emergency | Perbaikan kloset mampet | 800000 | per pekerjaan | Emergency |

## Worker Cat

| worker_code | worker_name | city_tier | experience | rating_avg | completed_jobs | verification_status | price_positioning | service_name | harga_worker | unit | reason |
|---|---|---|---|---:|---:|---|---|---|---:|---|---|
| CT-KAB-001 | Cat Hemat Pak Narto | kabupaten | junior | 4.2 | 50 | verified | budget | Borongan cat tembok jasa saja | 20000 | per m2 | Harga hemat kabupaten |
| CT-KSD-002 | Warna Rapi | kota_sedang | mid | 4.5 | 130 | verified | standard | Borongan cat tembok jasa saja | 25000 | per m2 | Harga patokan |
| CT-SBY-003 | Finishing Paint Pro | kota_besar | senior | 4.8 | 290 | verified | premium | Borongan cat tembok jasa saja | 35000 | per m2 | Senior finishing |
| CT-JKT-004 | Exterior Specialist | kota_besar | specialist | 4.9 | 340 | verified | specialist | Cat exterior Dulux Weather Shield | 40000 | per m2 | Specialist exterior |
| CT-EMG-005 | Cat Kilat 24 Jam | kota_besar | senior | 4.6 | 170 | verified | emergency | Borongan cat tembok jasa saja | 45000 | per m2 | Deadline cepat |

## Worker Keramik

| worker_code | worker_name | city_tier | experience | rating_avg | completed_jobs | verification_status | price_positioning | service_name | harga_worker | unit | reason |
|---|---|---|---|---:|---:|---|---|---|---:|---|---|
| KR-KAB-001 | Pasang Keramik Hemat | kabupaten | junior | 4.2 | 47 | verified | budget | Pasang keramik 60x60 | 60000 | per m2 | Budget kabupaten |
| KR-KSD-002 | Keramik Rapi | kota_sedang | mid | 4.6 | 150 | verified | standard | Pasang keramik 60x60 | 75000 | per m2 | Harga patokan |
| KR-SBY-003 | Granit Presisi | kota_besar | senior | 4.8 | 310 | verified | premium | Pasang keramik 60x60 | 95000 | per m2 | Senior kota besar |
| KR-JKT-004 | Tile Specialist | kota_besar | specialist | 4.9 | 360 | verified | specialist | Pasang granit besar | 180000 | per m2 | Granit besar dan presisi |
| KR-EMG-005 | Keramik Cepat | kota_besar | senior | 4.6 | 160 | verified | emergency | Pasang keramik 60x60 | 120000 | per m2 | Deadline cepat |

---

# Fixed Price Evaluation Examples

## Example 1
Order: Perbaikan pipa wastafel bocor.  
Input worker: Perbaikan pipa ledeng bocor Rp200.000.  
Harga patokan: Rp200.000.  
Decision: wajar.  
Risk flag: tidak ada.  
Clarification question: tidak perlu.

## Example 2
Order: Perbaikan pipa wastafel bocor.  
Input worker: Cat tembok Rp1.000.000.  
Harga patokan: layanan cat tidak relevan dengan order pipa.  
Decision: tidak wajar.  
Risk flag: item_tidak_relevan, alasan_tidak_lengkap.  
Clarification question: Mengapa cat tembok diperlukan untuk perbaikan pipa wastafel bocor?

## Example 3
Order: AC tidak dingin.  
Input worker: Cuci AC Split Rp90.000.  
Harga patokan: Rp90.000.  
Decision: wajar.  
Risk flag: tidak ada.  
Clarification question: tidak perlu.

## Example 4
Order: AC tidak dingin.  
Input worker: Isi Freon R32/R410 1.5–2 PK Rp800.000.  
Harga patokan: Rp450.000.  
Decision: perlu klarifikasi.  
Risk flag: harga_tidak_wajar.  
Clarification question: Apakah Rp800.000 sudah termasuk perbaikan kebocoran, sparepart, atau pekerjaan tambahan?

## Example 5
Order: Listrik korslet.  
Input worker: Inspeksi listrik Rp85.000.  
Harga patokan: Rp85.000.  
Decision: wajar.  
Risk flag: tidak ada.  
Clarification question: tidak perlu.

## Example 6
Order: Pasang stop kontak.  
Input worker: Tambah stop kontak Rp500.000 per titik.  
Harga patokan: Rp85.000.  
Decision: tidak wajar.  
Risk flag: harga_tidak_wajar.  
Clarification question: Apakah Rp500.000 sudah termasuk instalasi kabel panjang, conduit, bobok tembok, stop kontak, dan material tambahan?

## Example 7
Order: Cat kamar.  
Input worker: Jasa cat Rp25.000/m2.  
Harga patokan: Rp25.000/m2.  
Decision: wajar.  
Risk flag: tidak ada.  
Clarification question: tidak perlu.

## Example 8
Order: Pasang keramik kamar mandi.  
Input worker: Pasang keramik 60x60 Rp75.000/m2.  
Harga patokan: Rp75.000/m2.  
Decision: wajar.  
Risk flag: tidak ada.  
Clarification question: tidak perlu.

## Example 9
Order: Kanopi carport.  
Input worker: Kanopi spandek zincalume baja ringan Rp350.000/m2.  
Harga patokan: Rp350.000/m2 untuk Jakarta.  
Decision: wajar.  
Risk flag: tidak ada.  
Clarification question: tidak perlu.

## Example 10
Order: Bangun tembok ringan.  
Input worker: Tukang harian Jakarta Rp235.000/hari.  
Harga patokan: Rp235.000/hari.  
Decision: wajar.  
Risk flag: tidak ada.  
Clarification question: tidak perlu.

---

# Instruction for RAG Answer Style

Jika user bertanya harga:
- Jawab: "Harga patokan [layanan] adalah RpX per [unit]."
- Jangan jawab: "Kisarannya sekitar..."
- Jika ada variasi worker, jawab: "Harga worker bisa berbeda, tetapi harga patokan knowledge base adalah RpX."
- Jika user bertanya wajar/tidak, bandingkan input dengan `harga_patokan`.
- Jika harga worker lebih tinggi tetapi worker senior/verified/emergency, jelaskan alasan toleransinya.

Contoh jawaban:
"Harga patokan cuci AC Split 0.5–2 PK adalah Rp90.000 per unit. Jika worker memasukkan Rp120.000, harga tersebut lebih tinggi dari patokan, tetapi masih bisa wajar untuk worker senior di kota besar atau layanan panggilan cepat."

---

# Source Notes

Sumber data digunakan sebagai baseline kurasi harga. Beberapa sumber menyediakan harga tunggal, beberapa menyediakan rentang. Jika sumber menyediakan rentang, dataset ini menggunakan angka patokan tunggal berupa median atau angka contoh agar RAG tidak menjawab dalam bentuk kisaran.