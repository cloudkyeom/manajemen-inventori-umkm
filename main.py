from dataDummy import dataBarang
# from menuMain import menu
from editBarang import editBarang
from deleteBarang import delBarang
from searchBarang import cariBarang
from addBarang import tambah_barang
from stockReport import laporan_stok

def main ():
    print("--- welcome to app ---")
    menu = {
    1 : "add product",
    2 : "update product",
    3 : "delete product",
    4 : "stock report"
    }
    def mMenu():
        for n, d in menu.items() :
            print(f"-{n}: {d}")
    mMenu()
    try:
        input_menu = int(input("pilih menu apa? *masukkan dengan angka "))
    except ValueError:
        print("inputnya angka kak")

    if input_menu == 1:
        tambah_barang()
    elif input_menu == 2:
        editBarang()
    elif input_menu == 3:
            delBarang()
    elif input_menu == 4:
        laporan_stok()
    elif input_menu == 5:
        cariBarang()
    else:
        print("menu tidak ditemukan")

if __name__ == "__main__":
    main() 