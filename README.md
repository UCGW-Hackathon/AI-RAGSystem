# AI RAG System

AI RAG System adalah aplikasi tanya jawab berbasis Agentic RAG. Sistem ini dapat mengambil referensi dari URL, menyimpan potongan dokumen ke Qdrant Cloud, lalu menggunakan Gemini API untuk menjawab pertanyaan berdasarkan konteks yang paling relevan.

Backend dibangun dengan FastAPI, LangGraph, LangChain, dan Qdrant. Frontend Vue sudah dibundel ke dalam service backend, sehingga aplikasi cukup dijalankan dari satu Docker Compose service.

## Fitur Utama

- Agentic RAG dengan alur retrieve, grade relevance, rewrite question, dan generate answer.
- Gemini API sebagai LLM provider.
- Qdrant Cloud sebagai vector database.
- Injection URL secara real-time dari UI.
- Hapus data berdasarkan metadata URL.
- Dashboard sederhana untuk melihat jumlah chunk per URL.
- Frontend Vue + PrimeVue sudah tertanam di FastAPI.
- Konfigurasi lewat `.env`.

## Arsitektur Singkat

```text
Browser UI
   |
   v
FastAPI backend
   |
   +-- LangGraph agent
   |     +-- Gemini API
   |     +-- Retriever tool
   |
   +-- Qdrant Cloud
         +-- URL chunks + embeddings
```

## Struktur Project

```text
.
+-- docker-compose.yml
+-- llm_service/
|   +-- main.py
|   +-- graph.py
|   +-- vectordb.py
|   +-- tools.py
|   +-- config.py
|   +-- requirements.txt
|   +-- dist/
+-- VUE/
+-- Images/
+-- .env
```

## Kebutuhan

- Docker Desktop
- Gemini API key
- Qdrant Cloud cluster URL
- Qdrant Cloud API key

Untuk development lokal tanpa Docker, gunakan Python 3.11. Beberapa dependency native belum stabil di Python 3.14.

## Konfigurasi Environment

Buat atau isi file `.env` di root project:

```env
GEMINI_API_KEY=isi_api_key_gemini
LLM_MODEL=gemini-flash-lite-latest

QDRANT_URL=https://isi-url-cluster-qdrant-cloud
QDRANT_API_KEY=isi_api_key_qdrant_cloud

LOG_LEVEL=INFO
COLLECTION_NAME=my_collection
EMBEDDINGS_MODEL=sentence-transformers/all-mpnet-base-v2
USER_AGENT=myagent
```

`LLM_MODEL=gemini-flash-lite-latest` dipakai sebagai default karena sudah dites bekerja pada setup free tier. Jika ingin memakai model lain, pastikan model tersebut tersedia untuk API key dan kuota project kamu.

## Menjalankan Aplikasi

Pastikan Docker Desktop sudah aktif, lalu jalankan:

```powershell
docker compose up --build
```

Jika service berhasil naik, buka:

```text
http://localhost:80
```

Untuk menghentikan aplikasi:

```powershell
docker compose down
```

## Cara Pakai

1. Buka UI di `http://localhost:80`.
2. Masukkan satu atau beberapa URL pada bagian `URL Input`.
3. Klik `Submit URLs`.
4. Tunggu sampai proses injection selesai.
5. Klik `Get Metadata Count` untuk memastikan data sudah masuk ke Qdrant.
6. Ajukan pertanyaan di bagian `Your Message`.

Contoh URL untuk testing:

```text
https://lilianweng.github.io/posts/2024-11-28-reward-hacking/
https://lilianweng.github.io/posts/2024-07-07-hallucination/
https://lilianweng.github.io/posts/2024-04-12-diffusion-video/
```

Contoh pertanyaan:

```text
What does Lilian Weng say about types of reward hacking?
```

## API Endpoint

### Ask

```powershell
curl -X POST "http://localhost:80/ask" `
  -H "Content-Type: application/json" `
  -d "{\"question\":\"What does Lilian Weng say about reward hacking?\"}"
```

### Inject URLs

```powershell
curl -X POST "http://localhost:80/inject" `
  -H "Content-Type: application/json" `
  -d "{\"urls\":[\"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/\"]}"
```

### Metadata Counts

```powershell
curl "http://localhost:80/metadata/counts"
```

### Debug Points

```powershell
curl "http://localhost:80/debug/points"
```

### Delete By URL Metadata

```powershell
curl -X POST "http://localhost:80/delete_by_metadata" `
  -H "Content-Type: application/json" `
  -d "{\"url\":\"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/\"}"
```

### App Config

```powershell
curl "http://localhost:80/api/config"
```

## Development Lokal

Buat virtual environment Python 3.11:

```powershell
uv venv .venv311 --python 3.11
```

Install dependency backend:

```powershell
uv pip install --python .venv311\Scripts\python.exe -r llm_service\requirements.txt
```

Validasi sintaks:

```powershell
.venv311\Scripts\python.exe -m py_compile llm_service\config.py llm_service\graph.py llm_service\vectordb.py llm_service\main.py
```

## Frontend

Source frontend ada di folder `VUE/`. Build production yang dipakai backend ada di `llm_service/dist/`.

Untuk menjalankan frontend secara terpisah:

```powershell
cd VUE
npm install
npm run dev
```

Setelah perubahan frontend selesai:

```powershell
npm run build
```

Lalu salin hasil build ke `llm_service/dist/` jika struktur build belum otomatis mengarah ke folder tersebut.

## Catatan Teknis

- Collection Qdrant akan dibuat otomatis saat aplikasi pertama kali melakukan inisialisasi vector store.
- Embedding default memakai `sentence-transformers/all-mpnet-base-v2`.
- Chunking dokumen dikonfigurasi di `llm_service/vectordb.py` dengan `chunk_size=200` dan `chunk_overlap=50`.
- Graph agent dikonfigurasi di `llm_service/graph.py`.
- Endpoint FastAPI utama berada di `llm_service/main.py`.

## Troubleshooting

Jika Docker gagal dengan pesan `dockerDesktopLinuxEngine`, buka Docker Desktop terlebih dahulu lalu ulangi `docker compose up --build`.

Jika Gemini mengembalikan error quota, coba cek kuota project di Google AI Studio atau gunakan model lain yang tersedia untuk API key kamu.

Jika koneksi Qdrant gagal, pastikan `QDRANT_URL` memakai URL cluster lengkap dengan `https://` dan `QDRANT_API_KEY` berasal dari cluster yang sama.
