# 1️⃣ MASALAH TANPA ERROR HANDLING
umur = int(input("Masukkan umur: "))
print(umur)

# Solusi
try:
    umur = int(input("Masukkan umur: "))
    print(umur)
except:
    print("Input harus angka!")

# LOOP + VALIDASI (REAL USE 🔥)
while True:
    try:
        umur = int(input("Masukan umur: "))
        print(umur)
        break
    except:
        print("Input harus Angka !")

# 4️⃣ MENANGANI ERROR SPESIFIK
try:
    angka = int(input("Masukan Angka: "))
    hasil = 10 / angka  # buat zero division
    print(hasil)
except ValueError:
    print("Harus Angka !")
except ZeroDivisionError:
    ("Tidak Boleh nol !")

# STUDI KASUS (REAL 🔥)
harga_list = []
barang = []

while True:
    try:
        jumlah = int(input("Masukkan jumlah barang: "))
        break
    except:
        print("Input harus angka!")

for i in range(jumlah):
    while True:
        try:
            harga = float(input(f"Harga barang ke-{i+1}: "))
            break
        except:
            print("Harga harus angka!")

    nama = input(f"Nama barang ke-{i+1}: ")
    barang.append(nama)
    harga_list.append(harga)


# latihan 1
try:
    angka = int(input("Masukan Angka: "))
    print(angka)
except ValueError:
    print("Input Harus Angka!")

# Latihan 2
while True:
    try:
        angka = int(input("Masukan Angka: "))
        hasil = 100 / angka
        print(hasil)
        break
    except ValueError:
        print("Input Harus Angka!")
    except ZeroDivisionError:
        print("angka tidak boleh 0")

# Latihan 3


def hitung_total(harga_list):
    return sum(harga_list)


def hitung_diskon(total):
    if total >= 200000:
        return total * 0.2
    return 0


harga_list = []
barang = []

while True:
    try:
        jumlah = int(input("Masukan jumlah barang: "))
        break
    except:
        print("Input harus angka !")

for i in range(jumlah):
    while True:
        try:
            harga = float(input(f"Harga barang ke- {i+1}: "))
            break
        except ValueError:
            print("Input Harus Angka")

    nama_barang = input(f"Masukan Nama Barang ke- {i+1}:")
    barang.append(nama_barang)
    harga_list.append(harga)

total = hitung_total(harga_list)
diskon = hitung_diskon(total)
bayar = total - diskon

print("\n--- STRUK ---\n")

for i in range(len(barang)):
    print(f"{i+1}. {barang[i]} - RP. {harga_list[i]}")

print(f"Total: {total}")
print(f"diskon: {diskon}")
print(f"bayar: {bayar}")
