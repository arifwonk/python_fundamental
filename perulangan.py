# for i in range(5):
#     print(i)

#  mulai dari 1 sampai 5
for i in range(1, 6):
    print(i)

# cetak bilangan genap 1-20
# range(start, stop, step)
for i in range(2, 21, 2):
    print(i)

# while loop digunakan jika kita belum berapa kali mengulang, atau kita ingin mengulang sampai suatu kondisi terpenuhi
i = 1
while i <= 5:
    print(i)
    i += 1

# break & continue
for i in range(1, 10):
    if i == 5:
        break  # keluar dari loop
    print(i)

for i in range(1, 10):
    if i == 5:
        continue  # lewati iterasi ini
    print(i)

# studi kasus 1: cetak total belanja berulang
# Input jumlah item
# Loop input harga
# Hitung total
total = 0
jumlah_item = int(input("Masukkan jumlah item: "))

for i in range(jumlah_item):
    harga = float(input(f"Masukkan harga item ke-{i+1}: "))
    total += harga

print(f"Total belanja: {total}")

# Kasus 2: Menu Berulang (while)
while True:
    print("1. lanjut")
    print("2. keluar")

    pilihan = input("Pilih menu: ")
    if pilihan == "2":
        print("program selesai")
        break

# latihan 1
# Gunakan for:
# Cetak angka 1–10
for i in range(1, 11):
    print(i)

# latihan 2
# Gunakan for:
# Cetak bilangan ganjil 1–20
for i in range(1, 21, 2):
    print(i)

# latihan 3
# Gunakan while:
# Input angka sampai user mengetik 0
# Hitung total semua angka
total = 0
while True:
    angka = float(input("Masukkan angka (0 untuk keluar): "))
    if angka == 0:
        break
    total += angka
    # total = total + angka #alternatif penjumlahan
print(f"Total semua angka: {total}")
