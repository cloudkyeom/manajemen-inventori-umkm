from dataDummy import dataBarang
import os #Apuila : Impor modul os

def delBarang():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n ---- Hapus Produk ----")

    print("\n----Daftar Barang----") #Apuila : menampilkan semua input 
    for i, item in enumerate(dataBarang, start=1):
        print(f"{i}. Nama     : {item['nama']}")
        print(f"   Kode     : {item['kode']}")
        print(f"   Jumlah   : {item['jumlah']}")
        print(f"   Expired  : {item['expired']}")
        print(f"   Kondisi  : {item['kondisi']}")
        print(f"   Kategori : {item['kategori']}\n")

    nama = input("Masukkan nama produk yang ingin dihapus: ")
    for i in dataBarang:
        if i["nama"] == nama:
            dataBarang.remove(i)
            print(f"\nproduk {i['nama']} berhasil dihapus.")
            return
        
    print("\nProduk tidak ditemukan.")
