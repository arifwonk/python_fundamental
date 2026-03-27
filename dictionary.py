#  hari ke 8 : Dictionary
# dictionary adalah tipe data yang menyimpan pasangan key-value

# TUPLE — DATA TETAP (IMMUTABLE)
# Apa itu Tuple?
# Tuple mirip list, TAPI tidak bisa diubah.
# Cocok untuk:
# Data tetap
# Konstanta
# Identitas

# contoh data tuple
data_tuple = ("senin", "selasa", "rabu")
print(data_tuple, "\n")

# # # SET — DATA UNIK (TANPA DUPLIKAT)
# # Apa itu Set?
# Set adalah kumpulan data TANPA urutan & TANPA duplikat.
angka = {1, 2, 3, 4, 5}
print(angka, "\n")

# tambah dan hapus data di set
angka.add(6)
angka.remove(3)
print(angka, "\n")

# DICTIONARY — KEY & VALUE
siswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}
print(siswa, "\n")
print(siswa["nama"], "\n")  # akses nilai berdasarkan key

# Tambah / ubah data dictionary
siswa["umur"] = 30  # ubah nilai umur
siswa["jurusan"] = "elektro"  # ubah nilai jurusan
print(siswa, "\n")

for key in siswa:
    print(key)

for key, value in siswa.items():
    print(f"{key}: {value}")

# / studi kasus utama hari 8
siswa = []
jumlah_siswa = int(input("masukan jumlah siswa: "))
for i in range(jumlah_siswa):
    data = {}
    data["nama"] = input("nama: ")
    data["umur"] = int(input("umur: "))
    data["jurusan"] = input("jurusan: ")
    siswa.append(data)

print("\n data siswa: ")
if not siswa:
    print("tidak ada data siswa")

for i, s in enumerate(siswa):
    print(f"{i+1}. {s['nama']} | {s['umur']} | {s['jurusan']}")

# Latihan 1 — Tuple
# Buat tuple:
# hari dalam seminggu
# tampilkan hari pertama & terakhir
hari = ("senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu")
print("Hari pertama:", hari[0])
print("Hari terakhir:", hari[-1])

# Latihan 2 — Set
# Input 5 angka
# Simpan ke set
# Tampilkan hasil (tanpa duplikat)
angka = set()
for i in range(5):
    angka.add(int(input("masukan angka: ")))

print("angka yang dimasukan: ")
for i in angka:
    print(i)

# latihan 3 — Dictionary
# Input data 1 orang (nama, umur, pekerjaan)
# Simpan dalam dictionary
# Tampilkan datanya dengan rapi
data = {}
data["nama"] = input("nama: ")
data["umur"] = int(input("umur: "))
data["pekerjaan"] = input("pekerjaan: ")
print("\nData yang dimasukan:")
for key, value in data.items():
    print(f"{key}: {value}")

# print satu baris dengan format tertentu
print(
    f"nama: {data["nama"]} | umur: {data["umur"]} | pekerjaan: {data["pekerjaan"]}")
