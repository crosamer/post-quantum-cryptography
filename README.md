> **Project Ujian Akhir Semester Kriptografi**  
> Mata Kuliah: Kriptografi Semester Ganjil 2025  
> Kelompok 12:  
> Mario Valentino Ardhana (L0123079)    
> Mohammad Adzka Crosamer (L0123083)  
> Muhammad Dzaky Putra Utomo (L0123092)   

# End-To-End Messaging for Mobile Devices Secured by Quantum Technology  
### Using Post-Quantum Key Encapsulation Techniques

Repository ini berisi implementasi **simulasi end-to-end secure messaging** menggunakan **Post-Quantum Cryptography (PQC)** dengan algoritma **Classic McEliece** sebagai **Key Encapsulation Mechanism (KEM)** dan **AES-256-GCM** sebagai algoritma enkripsi simetris.

Implementasi ini dibuat sebagai bagian dari tugas/penelitian pada mata kuliah **Kriptografi**, dengan tujuan memberikan gambaran praktis penerapan **Post-Quantum Cryptography** pada sistem komunikasi yang aman.

---

## 📌 Latar Belakang

Sebagian besar sistem end-to-end messaging saat ini masih mengandalkan algoritma kriptografi klasik seperti RSA dan Elliptic Curve Cryptography (ECC). Algoritma-algoritma tersebut berpotensi menjadi tidak aman di era **komputasi kuantum** karena dapat diserang menggunakan **Shor’s Algorithm**.

Sebagai solusi, penelitian ini menerapkan **Post-Quantum Cryptography**, khususnya **Key Encapsulation Mechanism (KEM)** berbasis **Classic McEliece**, yang hingga saat ini dianggap tahan terhadap serangan komputer kuantum.

---

## 🔐 Skema Keamanan yang Digunakan

- **Key Encapsulation Mechanism (KEM)**  
  - Algorithm: **Classic McEliece (mceliece6960119)**
- **Key Derivation Function (KDF)**  
  - SHA-256
- **Enkripsi Simetris**  
  - AES-256-GCM (Authenticated Encryption)

---

## ⚙️ Tech Stack

- **Bahasa Pemrograman**: Python 3
- **Library Post-Quantum**: `pqcrypto`
- **Library Kriptografi Simetris**: `pycryptodome`
- **Hash Function**: `hashlib (SHA-256)`

---

## 📦 Instalasi dan Penggunaan

Pastikan Python 3 sudah terpasang, lalu install dependensi berikut dan jalankan:

```bash
pip install pqcrypto pycryptodome
python pqc_secure_messaging.py
