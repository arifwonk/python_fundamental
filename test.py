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
            if harga < 0:
                print("Harga Tidak Boleh Negatif")
                continue
            break
        except ValueError:
            print("Input Harus Angka")

    nama_barang = input(f"Masukan Nama Barang ke- {i+1}:")
    barang.append(nama_barang)
    harga_list.append(harga)

total = hitung_total(harga_list)
diskon = hitung_diskon(total)
bayar = total - diskon

with open("data.txt", "a") as file:
    file.write("\n--- STRUK ---\n")

    for i in range(len(barang)):
        file.write(f"{i+1}. {barang[i]} - RP. {harga_list[i]}\n")

    file.write(f"Total: {total}\n")
    file.write(f"diskon: {diskon}\n")
    file.write(f"bayar: {bayar}\n")
    file.write("\n")
with open("data.txt", "r") as file:
    isi = file.read()
    print(isi)
