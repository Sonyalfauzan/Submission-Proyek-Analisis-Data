# Proyek Analisis Data: Bike Sharing

Proyek ini menganalisis dataset Bike Sharing untuk memahami pengaruh cuaca dan pola penyewaan sepeda. 

## Cara Menjalankan Dashboard

### 1. Setting Environment

Anda dapat memilih salah satu cara berikut untuk setup environment:

**a. Menggunakan Anaconda:**

1. **Buat environment:**
   ```bash
   conda create --name bike-sharing python=3.9

Aktifkan environment:
conda activate bike-sharing

Install library:
pip install -r requirements.txt

Menggunakan Shell/Terminal (tanpa Anaconda):
Buat direktori project:
mkdir bike-sharing
cd bike-sharing

Buat virtual environment (venv):
python3 -m venv venv

Aktifkan virtual environment:
source venv/bin/activate

Install library:
pip install -r requirements.txt

Running Dashboard
Pindah ke direktori submission/dashboard di terminal.
Jalankan dashboard dengan perintah:
streamlit run dashboard.py
