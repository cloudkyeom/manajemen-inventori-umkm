from dataDummy import dataBarang

def delBarang():
    print("\n ---- hapus produk ----")
    nama = input("masukkan nama produk yang ingin dihapus: ")
    for i in dataBarang:
        if i["nama"] == nama:
            dataBarang.remove(i)
            print(f"produk {i['nama']} berhasil dihapus.")
            return
    print("product not found")
