# mengambil data pada data dummy 
from dataDummy import dataBarang

def delBarang():
    print("\n ---- hapus produk ----")
    nama = input("masukkan nama produk yang ingin dihapus: ")
    # pencarian barang berdasarkan nama untuk dihapus
    for i in dataBarang:
        if i["nama"] == nama:
            # penghapusan barang
            dataBarang.remove(i)
            print(f"produk {i['nama']} berhasil dihapus.")
            return
    # ketika barang tidak ditemukan, program akan melaksanakan kode berikut
    print("product not found")
