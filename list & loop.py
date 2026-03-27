# membuat list
buah = ["apel", "jeruk", "mangga"]
print(buah)

# index list
print(buah[0])  # akses elemen pertama
print(buah[1])  # akses elemen kedua
print(buah[2])  # akses elemen ketiga

# menambhakan data ke list
# apend()   tambah di akhir list
buah.append("pisang")
print(buah)

# insert()   tambah di posisi tertentu
buah.insert(1, "pepaya")  # tambah pepaya di index 1
print(buah)

# menhapus data dari list
# remove()   hapus berdasarkan nilai
buah.remove("jeruk")
print(buah)

# pop()   hapus berdasarkan index
buah.pop(0)  # hapus elemen pertama
print(buah)

# looping list
for item in buah:
    print(item)

# studi kasus utama hari 7
# kasus data nilai siswa: LIST + LOOP + INPUT + HITUNG
    nilai = []
    jumlah_siswa = int(input("masukan jumlah nilai: "))
    for i in range(jumlah_siswa):
        n = float(input(f"masukan nilai ke-{i+1}: "))
        nilai.append(n)

    total = sum(nilai)
    rata_rata = total / len(nilai)
    print(f"total nilai: {total}")
    print(f"rata-rata nilai: {rata_rata}")

# latihan 1
# Buat list:
# nama buah (minimal 3)
# tampilkan semua buah dengan loop
buah = ["mangga", "apel", "jeruk"]
for item in buah:
    print(item)

# latihan 2
# Tambah 1 buah baru
# Hapus 1 buah
# Tampilkan hasil akhirnya
buah = ["mangga", "apel", "jeruk"]
buah.insert(0, "jambu")
buah.remove("apel")
print(buah)

# latihan 3
# Input jumlah barang
# Simpan nama barang ke list
# Tampilkan semua barang
barang = []
jumlah_barang = int(input("masukan jumlah barang: "))
for i in range(jumlah_barang):
    n = input(f"masukan nama barang ke-{i+1}: ")
    barang.append(n)


print("Daftar barang:")
if jumlah_barang == 0:
    print("Tidak ada barang yang dimasukkan.")

for i, item in enumerate(barang, start=1):
    print(f"{i}. {item}")

# print jika tidak ingin menampilkan nomor urut
# for item in barang:
#     print(item)
