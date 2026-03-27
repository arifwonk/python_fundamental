# Perhitungan Matematika Dasar
a = 10
b = 3

print(a + b)  # penjumlahan
print(a - b)  # pengurangan
print(a * b)  # perkalian
print(a / b)  # pembagian
print(a // b)  # pembagian bulat atau floor division
print(a % b)  # modulus atau sisa bagi
print(a ** b)  # pangkat

# Catatan penting:
# / → hasil float
# // → hasil integer

# OPERATOR + VARIABEL (REAL CASE)

harga = 5000
jumlah = 3
total_harga = harga * jumlah
print("Total harga:", total_harga)

# OPERATOR PERBANDINGAN
umur = 20
print(umur > 17)  # lebih besar dari
print(umur < 18)  # lebih kecil dari
print(umur >= 15)  # lebih besar atau sama dengan
print(umur <= 16)  # lebih kecil atau sama dengan
print(umur == 20)  # sama dengan
print(umur != 18)  # tidak sama dengan

# OPERATOR LOGIKA
umur = 20
punya_sim = True
print(umur > 17 and punya_sim)  # AND , semua harus benar
print(umur > 17 or punya_sim)  # OR , salah satu benar
print(not punya_sim)  # NOT , negasi atau kebalikan

# studi kasus
harga = 12000
jumlah = 4
total_harga = harga * jumlah

print("Total harga:", total_harga)
print("Apakah total harga lebih dari 50.000?", total_harga > 50000)

# Latihan 1
panjang = 10
lebar = 5
luas = panjang * lebar
print("Luas persegi panjang:", luas)

# latihan 2
nilai = 80
print("Apakah nilai lebih dari 75?", nilai >= 75)
print("Apakah nilai kurang dari 60?", nilai < 60)

# Latihan 3
uang = 100000
belanja = 75000
print("Apakah uang cukup untuk belanja?", uang >= belanja)
