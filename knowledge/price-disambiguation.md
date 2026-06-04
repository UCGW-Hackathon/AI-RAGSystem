# Price Disambiguation Rules SiTukang

## Hard Rule AC Service Code

AC-001 selalu berarti Cuci AC Split 0.5–2 PK dengan harga_patokan Rp90.000 per unit.
AC-002 selalu berarti Cuci AC Inverter 0.5–2 PK dengan harga_patokan Rp140.000 per unit.

Jika user menyebut Cuci AC Split, AC Split, AC biasa, atau AC non-inverter, gunakan AC-001.
Jika user menyebut Cuci AC Inverter, gunakan AC-002.

AI dilarang menggunakan harga Rp140.000 untuk Cuci AC Split.
AI dilarang menggunakan harga worker sebagai harga patokan.

## Canonical AC Price Table

| Query User | Kode | Nama Resmi | Harga Patokan | Unit | Source |
|---|---|---|---:|---|---|
| Cuci AC Split 0.5–2 PK | AC-001 | Cuci AC Split 0.5–2 PK | 90000 | per unit | fixedprice.md |
| Cuci AC biasa | AC-001 | Cuci AC Split 0.5–2 PK | 90000 | per unit | fixedprice.md |
| Cuci AC non-inverter | AC-001 | Cuci AC Split 0.5–2 PK | 90000 | per unit | fixedprice.md |
| Cuci AC Inverter 0.5–2 PK | AC-002 | Cuci AC Inverter 0.5–2 PK | 140000 | per unit | fixedprice.md |
| Tambah Freon R32/R410 0.5–1 PK | AC-005 | Tambah Freon R32/R410 0.5–1 PK | 225000 | per unit | fixedprice.md |
| Kapasitor AC | MAT-AC-003 | Kapasitor AC | 125000 | per pcs | material-fixed-price.md |
| Selang drain AC | MAT-AC-004 | Selang drain AC | 10000 | per meter | material-fixed-price.md |
| Kabel power AC | MAT-AC-005 | Kabel power AC | 15000 | per meter | material-fixed-price.md |
| Bracket outdoor AC | MAT-AC-002 | Bracket outdoor AC | 75000 | per set | material-fixed-price.md |