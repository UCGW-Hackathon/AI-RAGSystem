# Manual Tests: SiTukang Fixed Price Retrieval

Jalankan API lokal:

```powershell
uv run --python .\.venv311\Scripts\python.exe python -m uvicorn llm_service.main:app --host 127.0.0.1 --port 8001
```

## 1. Exact Lookup Service Code

```powershell
curl -X POST "http://127.0.0.1:8001/ask" `
  -H "Content-Type: application/json" `
  -d "{\"question\":\"Cari service_code AC-001 dari JSONL. Tampilkan service_code, service_name, harga_patokan, unit, source_key, source_confidence.\"}"
```

Expected:

- `AC-001` ditemukan.
- `service_name` adalah `Cuci AC Split 0.5-2 PK`.
- `harga_patokan` adalah `Rp90.000`.
- `sources` berisi `http://localhost:9000/situkang_fixedprice.jsonl`.

## 2. Deterministic Price Evaluation

```powershell
curl -X POST "http://127.0.0.1:8001/ask" `
  -H "Content-Type: application/json" `
  -d "{\"question\":\"Evaluasi harga AC-001=120000, AC-002=130000, AC-005=300000. Ambil data berdasarkan service_code exact dari JSONL service fixed price.\"}"
```

Expected:

- `AC-001`, `AC-002`, dan `AC-005` ditemukan melalui exact lookup.
- Total input: `Rp550.000`.
- Total patokan: `Rp455.000`.
- Status dihitung deterministic oleh backend.
- `sources` berisi `http://localhost:9000/situkang_fixedprice.jsonl`.

## 3. Filtered Service Search Without Code

```powershell
curl -X POST "http://127.0.0.1:8001/ask" `
  -H "Content-Type: application/json" `
  -d "{\"question\":\"Berapa harga cuci AC biasa?\"}"
```

Expected:

- Mengarah ke layanan AC fixed price.
- Hasil utama ideal: `AC-001 | Cuci AC Split 0.5-2 PK | Rp90.000 per unit`.
