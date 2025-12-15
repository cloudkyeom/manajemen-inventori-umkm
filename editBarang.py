import dataDummy
import os


def editBarang ():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Edit Stok Barang ---")

    dataBarang = dataDummy.dataBarang
    if not dataBarang:
        print("\nBelum ada barang.")
        print()
        return
    
    print("\n----Daftar Barang----") #Apuila : menampilkan semua input 
    for i, item in enumerate(dataBarang, start=1):
        print(f"{i}. Nama     : {item['nama']}")
        print(f"   Kode     : {item['kode']}")
        print(f"   Jumlah   : {item['jumlah']}")
        print(f"   Expired  : {item['expired']}")
        print(f"   Kondisi  : {item['kondisi']}")
        print(f"   Kategori : {item['kategori']}\n")


    EditBarang = input("Masukkan nama barang yang akan diubah: ")
    found = False 
    
    for item in dataBarang:
        if item["nama"] == EditBarang:
            found = True
            print(f"Produk ditemukkan: {item['nama']}, (stok sekarang: {item['jumlah']})") 
            print("1. Tambah")
            print("2. Kurang")
            
            try:
                iInput = int(input("Pilih 1 atau 2? "))
                if iInput <= 2:
                    inJumlah = int(input("Jumlah: "))
                else:
                    print("Input tidak sesuai!")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return EditBarang
                    
            except ValueError:
                print("Input tidak sesuai!")
                input("Tekan ENTER untuk kembali ke menu utama...")
                return EditBarang

            if iInput == 1:
                    item['jumlah'] += inJumlah
                    print(f"Jumlah stok berhasil ditambahkan: {item['jumlah']}")
            elif iInput == 2:
                    if inJumlah <= item['jumlah']:
                        item['jumlah'] -= inJumlah
                        print(f"Stok berhasil dikurangi, sekarang: {item['jumlah']}")
                    else: 
                        print("stok kurang")
            else: 
                    print("pilihan tdk valid")           
            
            break
        
            
    if not found:
        print(f"\nBarang '{EditBarang}' tidak ditemukan")
        
    input("\nTekan ENTER untuk kembali ke menu.")
    os.system('cls' if os.name == 'nt' else 'clear')