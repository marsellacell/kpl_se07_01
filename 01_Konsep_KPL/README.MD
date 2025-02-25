# Task in Contruction
#### • Memastikan fondasi yang kuat dalam memahami konsep KPL
```java
Proyek: Sistem Manajemen Toko Online  
Teknologi: PHP (Backend), MySQL (Database), Flutter (Frontend)  
Arsitektur: MVC (Model-View-Controller)  
Rencana Fitur: Autentikasi, Manajemen Produk, Checkout, Notifikasi  
```
#### • Menentukan bagaimana kode program di uji
```python
import unittest

def tambah(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```
#### • Merancang dan menulis kelas
```python
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def get_info(self):
        return f"{self.judul} oleh {self.penulis} ({self.tahun})"

buku1 = Buku("Python for Beginners", "John Doe", 2021)
print(buku1.get_info())
```
#### • Membuat dan memberi nama variabel serta konstanta yang bermakna
```python
PI = 3.14159  # Konstanta
max_user_limit = 100  # Variabel dengan nama deskriptif
```
#### • Memilih struktur kontrol dan mengorganisir blok pernyataan
```python
for i in range(1, 6):
    print(f"Iterasi ke-{i}")

usia = 20
if usia >= 18:
    print("Anda sudah dewasa.")
else:
    print("Anda masih anak-anak.")
```
#### • Melakukan unit testing, integration testing, dan debugging kode sendiri
```python
import pdb

def bagi(a, b):
    pdb.set_trace()  # Memulai debugging mode
    return a / b

print(bagi(10, 2))
```
#### • Melakukan review kode tim lain dan meminta kode sendiri direview
```bash
$ git checkout -b fitur-baru
$ git add .
$ git commit -m "Menambahkan fitur baru"
$ git push origin fitur-baru
$ git checkout main
$ git merge fitur-baru
$ git push origin main
```
#### • Memperbaiki kode dengan memformat dan memberikan komentar dengan baik
```python
def luas_lingkaran(radius):
    """Menghitung luas lingkaran berdasarkan radius."""
    return PI * radius ** 2
```
#### • Mengintegrasikan komponen perangkat lunak yang dibuat secara terpisah
```python
import sqlite3

conn = sqlite3.connect('perpustakaan.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS buku (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    judul TEXT, penulis TEXT, tahun INTEGER)''')

conn.commit()
conn.close()
```
#### • Mengoptimalkan kode agar lebih cepat dan menggunakan lebih sedikit sumber daya
```python
# Sebelumnya
angka = [x for x in range(1, 100) if x % 2 == 0]

# Mengoptimalkan dengan list comprehension
print(angka)
```