from dataDummy import dataBarang

def editBarang ():
    print("--- update stock barang ---")
    try:
        EditBarang = input("masukkan nama barang yang ingin diubah: ")
    except ValueError:
        print("benerin ketikannya")
    found = False 
    
    for item in dataBarang:
        if item["nama"] == EditBarang:
            found = True
            try: 
                print(f"produk ditemukkan: {item['nama']}, (stok sekarang: {item['jumlah']})") 
                print("1. tambah")
                print("2. kurang")
                iInput = int(input("pilih 1 atau 2? "))
                inJumlah = int(input("jumlah: "))

                if iInput == 1:
                    item['jumlah'] += inJumlah
                    print(f"stock bertambah")
                elif iInput == 2:
                    if inJumlah <= item['jumlah']:
                        item['jumlah'] -= inJumlah
                        print(f"stok kurang, sekarang: {item['jumlah']}")
                    else: 
                        print("stok kurang")
                else: 
                    print("pilihan tdk valid")
                    return
            except ValueError: 
                print("ketikan salah")
                break
        if not found:
            print(f"Barang '{item['nama']}' tidak ditemukan")
