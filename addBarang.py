# primanisaa: perubahan nama file dari laporan_stock1.py -> addBarang.py

from dataDummy import dataBarang #Primanisaa: import data dari dummy
def tambah_barang():
    print("\n===== TAMBAH BARANG =====")
    nama    = input("Masukkan nama barang: ")
    kode    = input("Masukkan kode barang: ")
    jumlah  = int(input("Masukkan jumlah barang: "))
    expired = input("Masukkan tanggal expired: ")
    print("\nKondisi barang: rusak/ penyok/ kemasan terbuka/ bau/ berubah warna")
    kondisi = input("Masukkan kondisi barang: ").lower()

    # Cek kondisi barang
    if kondisi in ["rusak", "penyok", "kemasan terbuka", "bau", "berubah warna"]:
        kategori = "Reject"
        print("Barang Reject")
    else:
        kategori = "Gudang Umum"
        print("Barang masuk ke gudang umum")

    # Tambahkan ke daftar barang
    # Primanisaa: perubahan sedikit pada var data_barang -> dataBarang menyesuaikan dummy 

    dataBarang.append({
        "nama": nama,
        "kode": kode,
        "jumlah": jumlah,
        "expired": expired,
        "kondisi": kondisi,
        "kategori": kategori
    })
    dataBarang.append(dataBarang[-1].copy()) 

    print("Barang berhasil ditambahkan!\n")

# made by zahra aulia