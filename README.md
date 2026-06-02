# Obesity Prediction - Naive Bayes

>Online view : [mungkinkamuobes.vercel.app](https://mungkinkamuobes.vercel.app)

Aplikasi web berbasis **Django** untuk memprediksi tingkat obesitas seseorang menggunakan algoritma **Naive Bayes**. Pengguna dapat memasukkan data kesehatan dan mendapatkan hasil prediksi secara langsung.

---

## Our Team
- Muhammad Ali Murtadho
- Mochammad Zaenal Abidin
- Ahmad Maulana Ishaq
- Yohanes Oktanio

---

## Deskripsi

Sistem ini mengklasifikasikan tingkat obesitas berdasarkan parameter kesehatan seperti usia, tinggi badan, berat badan, kebiasaan makan, dan aktivitas fisik menggunakan pendekatan probabilistik Naive Bayes.

---

##  Teknologi yang Digunakan

| Teknologi | Versi |
|-----------|-------|
| Python | 3.x |
| Django | 6.0.5 |
| scikit-learn | 1.8.0 |
| pandas | 3.0.1 |
| numpy | 2.4.4 |
| matplotlib | 3.10.8 |
| seaborn | 0.13.2 |

---

## Struktur Project

```
obesity-prediction-naive-bayes/
├── bayes_classifier/       # App utama klasifikasi Naive Bayes
├── classifier/             # Konfigurasi project Django
├── manage.py               # Entry point Django
├── requirements.txt        # Daftar dependencies
└── .gitignore
```

---

## Cara Menjalankan Project

### 1. Clone Repository

```bash
git clone https://github.com/muhammadalimurtadho05/obesity-prediction-naive-bayes.git
cd obesity-prediction-naive-bayes
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```


### 3. Jalankan Server

```bash
python manage.py runserver
```

### 4. Buka di Browser

```
http://127.0.0.1:8000/
```

---

## Fitur

- Input data kesehatan pengguna
- Prediksi tingkat obesitas menggunakan Naive Bayes
- Tampilan hasil prediksi beserta probabilitas
- Visualisasi data dan hasil klasifikasi

---

## Kategori Prediksi

| Kategori | Keterangan |
|----------|------------|
| Insufficient | Berat badan kurang |
| Normal | Berat badan normal |
| Overweight | Kelebihan berat badan |
| Obesity  | Obesitas |

---
"# obesity-prediction-knn" 
