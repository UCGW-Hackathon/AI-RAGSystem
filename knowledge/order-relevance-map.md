# Order Relevance Map SiTukang

## Tujuan

Dokumen ini memetakan jenis order dengan layanan dan material yang relevan. AI harus menggunakan dokumen ini untuk menentukan apakah item atau layanan yang diajukan worker sesuai dengan konteks order.

## Order: Perbaikan Pipa Bocor

Layanan relevan:
- Perbaikan pipa ledeng bocor
- Ganti pipa PVC
- Ganti sambungan pipa
- Ganti keran
- Perbaikan wastafel atau sink
- Ganti flexible hose
- Perbaikan floor drain
- Seal ulang sambungan pipa

Material relevan:
- Pipa PVC
- Sambungan pipa PVC
- Elbow PVC
- Socket PVC
- Lem pipa PVC
- Seal tape
- Keran
- Flexible hose
- Floor drain

Material tidak relevan:
- Cat tembok
- Kabel listrik
- Stop kontak
- Freon AC
- Keramik lantai
- CCTV
- Smart lock
- Tanaman hias

Risk rule:
Jika worker memasukkan cat, kabel listrik, freon, CCTV, atau item lain yang tidak berhubungan dengan pipa bocor, beri `item_tidak_relevan`.

## Order: Saluran Air Mampet

Layanan relevan:
- Perbaikan pipa ledeng mampet
- Perbaikan kloset mampet
- Pembersihan saluran air
- Bongkar saringan saluran
- Perbaikan floor drain

Material relevan:
- Cairan pembersih saluran
- Floor drain
- Flexible hose
- Seal tape
- Lem pipa
- Pipa PVC
- Sambungan pipa

Material tidak relevan:
- Cat tembok
- Stop kontak
- Freon
- Keramik dinding kecuali ada bongkar pasang
- CCTV

## Order: AC Tidak Dingin

Layanan relevan:
- Cuci AC Split
- Cuci AC inverter
- Tambah freon
- Isi freon
- Cek kebocoran freon
- Ganti kapasitor AC
- Bersihkan indoor/outdoor AC
- Perbaikan pipa AC

Material relevan:
- Freon R22
- Freon R32/R410
- Kapasitor AC
- Pipa AC
- Selang drain AC
- Bracket outdoor AC
- Kabel power AC
- Duct tape AC

Material tidak relevan:
- Pipa PVC air
- Lem pipa PVC
- Cat tembok
- Keramik lantai
- Kloset
- Floor drain
- CCTV

## Order: Listrik Korslet

Layanan relevan:
- Inspeksi listrik
- Perbaikan korsleting
- Ganti MCB
- Ganti sekring
- Instalasi kabel
- Cek panel listrik
- Cek jalur stop kontak
- Cek saklar

Material relevan:
- Kabel NYM
- Kabel NYA
- MCB
- Sekring
- Saklar
- Stop kontak
- Isolasi listrik
- Pipa conduit
- Box inbow

Material tidak relevan:
- Freon AC
- Lem pipa
- Pipa PVC air
- Cat tembok
- Kloset
- Keramik
- Tanaman

## Order: Pasang Stop Kontak

Layanan relevan:
- Tambah stop kontak
- Instalasi line stop kontak
- Instalasi kabel tanpa bobok
- Instalasi kabel dengan conduit
- Pasang stop kontak unit

Material relevan:
- Stop kontak
- Kabel NYM
- Kabel NYA
- Pipa conduit
- Box stop kontak inbow
- Isolasi listrik
- Sekrup

Material tidak relevan:
- Freon
- Lem pipa
- Cat tembok
- Kloset
- Shower
- Keramik
- Bracket AC

## Order: Cat Kamar

Layanan relevan:
- Borongan cat tembok jasa saja
- Cat interior
- Plamir dinding
- Pengerokan cat lama
- Amplas tembok
- Cat plafon

Material relevan:
- Cat tembok
- Kuas cat
- Roller cat
- Baki cat
- Plamir
- Amplas
- Lakban kertas

Material tidak relevan:
- Freon AC
- Kabel listrik
- Stop kontak kecuali ada instalasi listrik
- Pipa PVC
- Kloset
- CCTV

## Order: Pasang Keramik

Layanan relevan:
- Pasang keramik 40x40
- Pasang keramik 60x60
- Pasang granit
- Nat keramik
- Bongkar keramik lama
- Pasang backsplash
- Pasang keramik dinding kamar mandi

Material relevan:
- Keramik
- Granit tile
- Semen
- Pasir
- Semen instan
- Nat
- Tile spacer
- Waterproofing untuk kamar mandi

Material tidak relevan:
- Freon AC
- Kabel listrik
- Stop kontak
- Cat tembok kecuali finishing
- Pipa PVC kecuali kamar mandi
- CCTV

## Order: Pompa Air Mati

Layanan relevan:
- Inspeksi pompa air
- Pancing pompa
- Ganti kapasitor pompa
- Ganti otomatis pompa
- Perbaikan pompa tidak menyala
- Pasang pompa baru
- Setting pressure switch

Material relevan:
- Kapasitor pompa
- Pressure switch
- Otomatis pompa
- Seal pompa
- Kabel listrik
- Pipa PVC
- Seal tape

Material tidak relevan:
- Freon AC
- Cat tembok
- Keramik
- CCTV
- Smart lock

## Order: Pasang CCTV

Layanan relevan:
- Pasang kamera CCTV
- Tarik kabel CCTV
- Setting DVR/NVR
- Pasang kamera WiFi
- Setting remote view
- Perbaikan kamera offline
- Pasang smart doorbell

Material relevan:
- Kamera CCTV
- Kabel CCTV
- Adaptor CCTV
- DVR/NVR
- Konektor BNC
- Hard disk CCTV
- Kabel LAN
- Bracket kamera

Material tidak relevan:
- Freon AC
- Lem pipa
- Cat tembok
- Kloset
- Keramik
- Pipa PVC air

## Instruksi AI

Jika order dan item tidak cocok dengan mapping:
- Decision: tidak_wajar
- Risk flag: item_tidak_relevan
- Clarification question: "Mengapa item atau layanan tersebut diperlukan untuk order ini?"
