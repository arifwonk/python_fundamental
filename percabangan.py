# if else statement
umur = 15

if umur >= 18:
    print("bisa membuat SIM.")
else:
    print("belum bisa membuat SIM.")

# if elif else statement

nilai = 69

if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
else:
    print("Nilai D")

# kondisi dengan operator logika
umur = 17
punya_sim = True

if umur >= 18 and punya_sim:
    print("boleh mengendarai mobil.")
else:
    print("tidak boleh mengendarai mobil.")

#  studi kasusn 1 cek kelulusan
# Input nilai
# Jika nilai ≥ 75 → LULUS
# Jika < 75 → TIDAK LULUS
nilai = int(input("Masukkan nilai Anda: "))
if nilai >= 75:
    print("LULUS")
else:
    print("TIDAK LULUS")

# Studi kasus 2 diskon belanja
# Total ≥ 100.000 → Diskon 10%
# Total < 100.000 → Tidak ada diskon
total = int(input("Masukkan total belanja: "))
if total >= 100000:
    diskon = total * 0.1
    total_bayar = total - diskon
    print("Anda mendapatkan diskon 10%")
    print("Total bayar setelah diskon:", total_bayar)
else:
    print("Tidak ada diskon")
    print("Total bayar:", total)

#  latihan 1
# Input umur
# Jika umur ≥ 18 → "Dewasa"
# Jika < 18 → "Belum dewasa"
umur = int(input("Masukkan umur Anda: "))
if umur >= 18:
    print("Dewasa")
else:
    print("Belum dewasa")

# latihan 2 Input nilai
# ≥ 90 → A
# ≥ 80 → B
# ≥ 70 → C
# < 70 → D
nilai = int(input("Masukkan nilai Anda: "))
if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
else:
    print("Nilai D")


# Latihan 3 (REAL CASE 🔥)
# Program kasir:
# Input total belanja
# Jika total ≥ 200.000 → diskon 20%
# Tampilkan total bayar setelah diskon
total = int(input("Masukkan total belanja: "))
if total >= 200000:
    diskon = total * 0.2
    total_bayar = total - diskon
    print("Anda mendapatkan diskon 20%")
    print("Total bayar setelah diskon:", total_bayar)
else:
    print("Tidak ada diskon")
    print("Total bayar:", total)

# RANGKUMAN HARI 5

# ✔ if = satu kondisi
# ✔ else = kondisi lain
# ✔ elif = banyak kondisi
# ✔ Indentasi WAJIB
# ✔ Program mulai “berpikir”
