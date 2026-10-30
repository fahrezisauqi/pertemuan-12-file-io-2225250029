
# Pertemuan 12 - File I/O dan Error Handling

## Identitas

Nama: Fahrezi Sauqi Alghani

NIM: 2225250029

Kelas: 3E

## Tujuan

Mempelajari cara membaca, menulis, memproses,
dan menangani error pada file menggunakan Python.

## Materi

1. Menulis file menggunakan mode w.
2. Membaca file menggunakan mode r.
3. Menambahkan data menggunakan mode a.
4. Memproses baris menggunakan strip() dan split().
5. Menangani FileNotFoundError.
6. Menangani ValueError.
7. Menggunakan fungsi untuk file I/O.

## Struktur Data

Folder data berisi:

- catatan.txt
- nilai.txt
- hasil_rekap.txt

Format file nilai.txt:

NIM,nilai

Contoh:

A001,85
A002,78
A003,92

## Cara Menjalankan

Latihan 1:

py latihan/01_tulis_file.py

Latihan 2:

py latihan/02_baca_file.py

Latihan 3:

py latihan/03_append_file.py

Latihan 4:

py latihan/04_proses_baris.py

Latihan 5:

py latihan/05_file_not_found.py

Latihan 6:

py latihan/06_value_error.py

Program utama:

py tugas/rekap_nilai_file.py

## Error yang Ditangani

- FileNotFoundError
- ValueError

## Hasil Pengujian

- Jumlah data valid: 5
- Rata-rata: 83.40
- Nilai minimum: 74.00
- Nilai maksimum: 92.00
- Jumlah lulus: 5

## Refleksi

Kesalahan yang ditemukan adalah ValueError ketika
nilai mahasiswa berisi teks yang tidak dapat
dikonversi menjadi angka.

Kesalahan tersebut ditangani menggunakan
try-except sehingga data lainnya tetap diproses.

## Kesimpulan

File I/O memungkinkan data disimpan dan dibaca
kembali. Error handling membantu program
memberikan pesan yang jelas ketika terjadi
kesalahan.
