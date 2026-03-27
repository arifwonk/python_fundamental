# 2️⃣ MENULIS FILE (write)
with open("C:/Users/ASUS/Documents/Hello World/gpt/data.txt", "w") as file:
    file.write("hello wordl\n")

# 🧠 Penjelasan:
# "w" = write (menulis, menghapus isi lama)
# \n = baris baru
# with = otomatis menutup file (BEST PRACTICE)

# 3️⃣ MENAMBAH DATA (append)
with open("C:/Users/ASUS/Documents/Hello World/gpt/data.txt", "a") as file:
    file.write("baris baru\n")

# 4️⃣ MEMBACA FILE (read)
with open("C:/Users/ASUS/Documents/Hello World/gpt/data.txt", "r") as file:
    isi = file.read()
    print(isi)



# Latihan 1
nama = input("Nama :")
print(nama)
with open("C:/Users/ASUS/Documents/Hello World/gpt/data.txt", "w") as file:
    file.write(nama)

# latihan 2
with open("C:/Users/ASUS/Documents/Hello World/gpt/data.txt", "r") as file:
    isi_nama = file.read()
    print(isi_nama)

# Latihan 3
def hitung_total(harga_list):
    return sum(harga_list)

def hitung_diskon(total):
    if total >= 200000:
        return total * 0.2
    return 0

harga_list = []
barang = []
jumlah = int(input("Masukan jumlah barang: "))

for i in range(jumlah):
    harga = float(input(f"Harga barang ke- {i+1}: "))
    nama_barang = input(f"Masukan Nama Barang ke- {i+1}:")
    barang.append(nama_barang)
    harga_list.append(harga) 

total = hitung_total(harga_list)
diskon = hitung_diskon(total)
bayar = total - diskon


with open("C:/Users/ASUS/Documents/Hello World/gpt/data.txt", "a") as file:
    file.write("\n--- STRUK ---\n")
    
    for i in range(len(barang)):
        file.write(f"{i+1}. {barang[i]} - RP. {harga_list[i]}\n")

    file.write(f"Total: {total}\n")
    file.write(f"diskon: {diskon}\n")
    file.write(f"bayar: {bayar}\n")
    file.write("\n")
with open("C:/Users/ASUS/Documents/Hello World/gpt/data.txt", "r") as file:
    isi = file.read()
    print(isi)


