# primanisaa: perubahan file dari laporan_stock1.py -> stockReport.py
from dataDummy import dataBarang # primanisaa: import data dari dummy

def laporan_stok():
    print("\n===== LAPORAN STOK BERDASARKAN KATEGORI =====")

    # primanisaa: perubahan variabel dari daftar_barang -> dataBarang menyesuaikan dummy 
    
    reject = [barang for barang in dataBarang if barang["kategori"] == "Reject"]
    gudang_umum = [barang for barang in dataBarang if barang["kategori"] == "Gudang Umum"]
    prioritas = [barang for barang in dataBarang if barang["kategori"] == "Gudang Prioritas"] if "Gudang Prioritas" in dataBarang else []

    print("\n----- Barang Reject -----")
    if reject:
        for barang in reject:
            print(f"{barang['kode']} - {barang['nama']} - {barang['jumlah']} pcs")
    else:
        print("Tidak ada.")
    
    print("\n----- Gudang Umum -----")
    if gudang_umum:
        for barang in gudang_umum:
            print(f"{barang['kode']} - {barang['nama']} - {barang['jumlah']} pcs")
    else:
        print("Tidak ada.")

    print("\n----- Gudang Prioritas -----")
    if prioritas:
        for barang in prioritas:
            print(f"{barang['kode']} - {barang['nama']} - {barang['jumlah']} pcs")
    else:
        print("Tidak ada.")

    print()

# made by zahra aulia