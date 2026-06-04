# Fixed Evaluation Examples SiTukang

## Tujuan

Dokumen ini berisi contoh evaluasi harga dan relevansi untuk membantu AI memberi keputusan konsisten.

## Example 1

Order: Perbaikan pipa bocor.  
Input worker: Jasa perbaikan pipa ledeng bocor Rp200.000.  
Harga patokan: Rp200.000.  
Decision: wajar.  
Risk flag: tidak ada.  
Reason: Harga sama dengan harga patokan dan layanan relevan dengan order.  
Clarification question: null.

## Example 2

Order: Perbaikan pipa bocor.  
Input worker: Lem pipa PVC Rp200.000.  
Harga patokan: Rp15.000 per pcs.  
Decision: tidak_wajar.  
Risk flag: harga_tidak_wajar.  
Severity: high.  
Reason: Harga input jauh di atas harga patokan.  
Clarification question: Apakah Rp200.000 sudah termasuk banyak item lain atau pembelian dalam jumlah besar?

## Example 3

Order: Perbaikan pipa bocor.  
Input worker: Cat tembok Rp1.000.000.  
Harga patokan: Cat tembok tidak relevan dengan order pipa bocor.  
Decision: tidak_wajar.  
Risk flag: item_tidak_relevan.  
Severity: high.  
Reason: Cat tembok tidak diperlukan untuk perbaikan pipa bocor.  
Clarification question: Mengapa cat tembok diperlukan untuk pekerjaan pipa bocor?

## Example 4

Order: AC tidak dingin.  
Input worker: Cuci AC Split 0.5–2 PK Rp90.000.  
Harga patokan: Rp90.000 per unit.  
Decision: wajar.  
Risk flag: tidak ada.  
Reason: Harga sama dengan harga patokan.  
Clarification question: null.

## Example 5

Order: AC tidak dingin.  
Input worker: Isi Freon R32/R410 1.5–2 PK Rp800.000.  
Harga patokan: Rp450.000 per unit.  
Decision: perlu_klarifikasi.  
Risk flag: harga_tidak_wajar.  
Severity: medium.  
Reason: Harga lebih tinggi dari harga patokan, tetapi mungkin termasuk perbaikan kebocoran atau sparepart tambahan.  
Clarification question: Apakah harga tersebut sudah termasuk perbaikan kebocoran, sparepart, atau pekerjaan tambahan?

## Example 6

Order: Listrik korslet.  
Input worker: Inspeksi listrik Rp85.000.  
Harga patokan: Rp85.000 per kunjungan.  
Decision: wajar.  
Risk flag: tidak ada.  
Reason: Harga sama dengan harga patokan dan layanan relevan.  
Clarification question: null.

## Example 7

Order: Pasang stop kontak.  
Input worker: Tambah stop kontak Rp500.000 per titik.  
Harga patokan: Rp85.000 per titik.  
Decision: tidak_wajar.  
Risk flag: harga_tidak_wajar.  
Severity: high.  
Reason: Harga input jauh di atas harga patokan.  
Clarification question: Apakah Rp500.000 sudah termasuk instalasi kabel panjang, conduit, bobok tembok, stop kontak, dan material tambahan?

## Example 8

Order: Cat kamar.  
Input worker: Jasa cat Rp25.000/m2.  
Harga patokan: Rp25.000/m2.  
Decision: wajar.  
Risk flag: tidak ada.  
Reason: Harga sama dengan harga patokan.  
Clarification question: null.

## Example 9

Order: Pasang keramik kamar mandi.  
Input worker: Pasang keramik 60x60 Rp75.000/m2.  
Harga patokan: Rp75.000/m2.  
Decision: wajar.  
Risk flag: tidak ada.  
Reason: Harga sama dengan harga patokan.  
Clarification question: null.

## Example 10

Order: Pompa air mati.  
Input worker: Ganti kapasitor pompa Rp150.000.  
Harga patokan: Gunakan data material atau jasa pompa jika tersedia.  
Decision: wajar.  
Risk flag: tidak ada.  
Reason: Harga masuk akal untuk perbaikan pompa air.  
Clarification question: null.

## Example 11

Order: AC tidak dingin.  
Input worker: Pipa PVC 1/2 inch Rp25.000 per meter.  
Harga patokan: Rp25.000 per meter, tetapi item tidak relevan dengan AC.  
Decision: tidak_wajar.  
Risk flag: item_tidak_relevan.  
Severity: high.  
Reason: Pipa PVC air tidak relevan dengan order AC tidak dingin.  
Clarification question: Mengapa pipa PVC diperlukan untuk perbaikan AC?

## Example 12

Order: Listrik korslet.  
Input worker: Kabel NYM 2x1.5 mm Rp12.000 per meter.  
Harga patokan: Rp12.000 per meter.  
Decision: wajar.  
Risk flag: tidak ada.  
Reason: Material relevan dan harga sama dengan patokan.  
Clarification question: null.

## Example 13

Order: Listrik korslet.  
Input worker: Lem pipa PVC Rp15.000.  
Harga patokan: Rp15.000, tetapi item tidak relevan dengan listrik korslet.  
Decision: tidak_wajar.  
Risk flag: item_tidak_relevan.  
Severity: high.  
Reason: Lem pipa tidak relevan dengan pekerjaan listrik.  
Clarification question: Mengapa lem pipa diperlukan untuk perbaikan listrik korslet?

## Example 14

Order: Cat kamar.  
Input worker: Cat tembok standar 5 kg Rp150.000.  
Harga patokan: Rp150.000 per kaleng.  
Decision: wajar.  
Risk flag: tidak ada.  
Reason: Material relevan dan harga sama dengan patokan.  
Clarification question: null.

## Example 15

Order: Cat kamar.  
Input worker: Freon R32 Rp225.000.  
Harga patokan: Rp225.000, tetapi item tidak relevan.  
Decision: tidak_wajar.  
Risk flag: item_tidak_relevan.  
Severity: high.  
Reason: Freon AC tidak relevan dengan order cat kamar.  
Clarification question: Mengapa freon diperlukan untuk pekerjaan cat kamar?

## Example 16

Order: Pasang CCTV.  
Input worker: Pasang kamera CCTV Rp200.000 per titik.  
Harga patokan: Gunakan harga jasa CCTV jika tersedia.  
Decision: wajar.  
Risk flag: tidak ada.  
Reason: Layanan relevan dengan order CCTV.  
Clarification question: null.

## Example 17

Order: Perbaikan pipa bocor.  
Input worker: Pipa PVC 1/2 inch 2 meter total Rp50.000.  
Harga patokan: Rp25.000 per meter.  
Decision: wajar.  
Risk flag: tidak ada.  
Reason: 2 meter x Rp25.000 = Rp50.000, sesuai harga patokan.  
Clarification question: null.

## Example 18

Order: Perbaikan pipa bocor.  
Input worker: Pipa PVC 1/2 inch 2 meter total Rp200.000.  
Harga patokan: Rp25.000 per meter, total patokan Rp50.000.  
Decision: tidak_wajar.  
Risk flag: harga_tidak_wajar.  
Severity: high.  
Reason: Harga input 4x harga patokan.  
Clarification question: Apakah Rp200.000 sudah termasuk item lain, jasa pemasangan, atau pipa jenis khusus?

## Example 19

Order: Pasang stop kontak.  
Input worker: Stop kontak standar Rp25.000.  
Harga patokan: Rp25.000 per pcs.  
Decision: wajar.  
Risk flag: tidak ada.  
Reason: Material relevan dan sesuai harga patokan.  
Clarification question: null.

## Example 20

Order: Pasang stop kontak.  
Input worker: Stop kontak standar Rp250.000.  
Harga patokan: Rp25.000 per pcs.  
Decision: tidak_wajar.  
Risk flag: harga_tidak_wajar.  
Severity: high.  
Reason: Harga 10x harga patokan untuk material stop kontak standar.  
Clarification question: Apakah harga tersebut sudah termasuk jasa instalasi, kabel, bobok tembok, dan material lainnya?
