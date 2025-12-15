import os #Apuila : Import OS agar tampilan bisa di clear

from dataDummy import dataBarang
# from menuMain import menu
from editBarang import editBarang
from deleteBarang import delBarang
from searchBarang import cariBarang
from addBarang import tambah_barang
from stockReport import laporan_stok

def main():
    print("\n--- Informasi Update Stok ---") #Apuila : memperbaiki titel &  opsi aplikasi
    Menu = {
        1 : "Tambahkan Produk",
        2 : "Perbarui Daftar Produk",
        3 : "Hapus Produk",
        4 : "Informasi Stok"
    }
    
    def theMenu():
        for n, d in Menu.items() :
            print(f"-{n}: {d}")

    while True : 
#Apuila: Menambahkan perulangan while untuk antisipasi pengguna masukkan angka selain menu
        theMenu()

        try:
            
            input_menu = int(input("Pilih satu menu (masukkan dengan angka): "))
        except ValueError:
            print("Inputnya WAJIB angka kak")
            input("\nTekan ENTER untuk kembali.") #Apuila : biar ga error kalo dimasukin huruf
            os.system('cls' if os.name == 'nt' else 'clear') #Apuila : biar tampilan layar kosong lagi
            continue

        if input_menu == 1:
            tambah_barang()
        elif input_menu == 2:
            editBarang()
        elif input_menu == 3:
            delBarang() #Apuila: Indentasi salah
        elif input_menu == 4:
            laporan_stok()
        elif input_menu == 5:
            cariBarang()
        else:
            print("\nMenu tidak ditemukan")
            input("\nTekan ENTER untuk kembali ke menu...")
            os.system('cls' if os.name == 'nt' else 'clear') #Apuila : membersihkan tampilan
        
if __name__ == "__main__":
    main()