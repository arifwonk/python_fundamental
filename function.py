# APA ITU FUNCTION?
# Function = kumpulan kode yang diberi nama, lalu bisa dipanggil kapan saja.
# Analogi:
# Function itu seperti resep masakan
# Ditulis sekali, dipakai berkali-kali.

# FUNCTION PALING DASAR
def sapa():
    print("halo, selamat datang")


sapa()  # panggil function sapa

# Penjelasan:
# def → membuat function
# sapa → nama function
# () → tanda function
# Kode di dalam function tidak jalan sebelum dipanggil

# FUNCTION DENGAN PARAMETER


def sapa_nama(nama):
    print("halo", nama)


sapa_nama("Andi")  # panggil function dengan argumen "Andi"

# FUNCTION DENGAN LEBIH DARI 1 PARAMETER


def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    print("luas persegi:", luas)


hitung_luas(5, 3)  # panggil function dengan argumen panjang=5 dan lebar=3

# FUNCTION DENGAN PARAMETER DEFAULT


def sapa_nama(nama="teman"):
    print("halo", nama)


sapa_nama()  # panggil function tanpa argumen, gunakan nilai default
sapa_nama("Budi")  # panggil function dengan argumen "Budi

# FUNCTION DENGAN RETURN


def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas  # kembalikan nilai luas


hasil = hitung_luas(20, 40)  # simpan hasil return ke variabel hasil
print("luas pesegi:", hasil)  # cetak hasil

# studi kasus Program Kasir Sederhana


def hitung_total(harga, jumlah):
    return harga * jumlah


def hitung_diskon(total):
    if total > 200000:
        return total * 0.1  # diskon 10%
    return 0  # tidak ada diskon


harga = float(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang: "))

total = hitung_total(harga, jumlah)
diskon = hitung_diskon(total)
total_bayar = total - diskon

print("Total:", total)
print("Diskon:", diskon)
print("Total bayar:", total_bayar)

# latihan 1
# Buat function:
# tambah(a, b)
# Kembalikan hasil penjumlahan a dan b


def tambah(a, b):
    return a + b


hasil = tambah(10, 20)
print("Hasil penjumlahan:", hasil)

# latihan 2
# Buat function:
# cek_genap(angka)
# Return "Genap" atau "Ganjil"


def cek_genap(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

    # return "Genap" if angka % 2 == 0 else "Ganjil"  # alternatif dengan ternary operator


print(cek_genap(4))  # Output: Genap
print(cek_genap(5))  # Output: Ganjil

#  latihan 3
# hitung_rata(nilai_list)
# Return rata-rata nilai dari list


def hitung_rata_rata(nilai_list):
    total = sum(nilai_list)  # hitung total nilai
    jumlah_nilai = len(nilai_list)  # hitung jumlah nilai
    if jumlah_nilai == 0:
        return 0  # hindari pembagian dengan nol
    return total / jumlah_nilai  # kembalikan rata-rata


nilai_list = [20, 10, 10, 85]
rata_rata = hitung_rata_rata(nilai_list)
print("Rata-rata nilai:", rata_rata)

#  latihan 4
# hitung_rata(nilai_list)
# Return rata-rata nilai dari list
# input nilai dari user, lalu hitung rata-ratanya


def hitung_rata_rata(nilai_list):
    total = sum(nilai_list)  # hitung total nilai
    jumlah_nilai = len(nilai_list)  # hitung jumlah nilai
    if jumlah_nilai == 0:
        return 0  # hindari pembagian dengan nol
    return total / jumlah_nilai  # kembalikan rata-rata


nilai_list = []
jumlah = int(input("Masukkan jumlah nilai: "))
for i in range(jumlah):
    nilai = float(input(f"Masukkan nilai ke-{i + 1}: "))
    nilai_list.append(nilai)

rata_rata = hitung_rata_rata(nilai_list)
print("Rata-rata nilai:", rata_rata)
