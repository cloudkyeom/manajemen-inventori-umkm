# primanisaa: perubahan nama file dari laporan_stock1.py -> addBarang.py

import dataDummy #Primanisaa: import data dari dummy
from datetime import datetime, timedelta #Apuila : import format kalender
import os

def tambah_barang():
    print("\n===== TAMBAH BARANG =====")
    nama    = input("Masukkan nama barang: ")
    kode    = input("Masukkan kode barang: ")

    while True: #Apuila: mengubah agar program melakukan looping ketika inputnya bukan angka
        try:
            jumlah  = int(input("Masukkan jumlah barang: "))
            break
        except ValueError:
            print("Tulis jumlahnya pake angka.")

    while True: #Apuila: memvalidasi tanggal expired agar format selalu sama
        expired = input("Masukkan tanggal expired (dd-mm-yyyy): ")
        try:
            data = datetime.strptime(expired, "%d-%m-%Y") # primansaa: mengubah format tanggal dari string ke date time
            today = datetime.today() # primanisaa: menetapkan data untuk tanggal hari ini
            tomorrow = today + timedelta(days=1) # primanisaa: menetapkan data untuk tanggal hari ini
            if data <= tomorrow : # primanisaa: apabila expired bsk maka masuk ke gudang prioritas
                print("masuk gudang prioritas")
            else:
                print("masuk gudang")
            break
        except ValueError:
            print("Format tanggal salah. Benerin formatnya.")
    
    #Apuila : mengubah validasi kondisi barang ke boolean
    while True:
        kondisi_input = input("Apakah barang rusak (penyok, berbau, berubah warna, kemasan terbuka)? (ya/tidak): ").lower()
        if kondisi_input == "ya":
            kondisi = "rusak"
            kategori = "Reject"
            break
        elif kondisi_input == "tidak":
            kondisi = "normal/bagus"
            kategori = "Gudang Umum"
            break
        else:
            print("Jawaban cuma 'ya' atau 'tidak'.")
            
    # Tambahkan ke daftar barang
    # Primanisaa: perubahan sedikit pada var data_barang -> dataBarang menyesuaikan dummy 

    dataDummy.dataBarang.append({
        "nama": nama,
        "kode": kode,
        "jumlah": jumlah,
        "expired": expired,
        "kondisi": kondisi,
        "kategori": kategori
    })

    os.system('cls' if os.name == 'nt' else 'clear')
    #dataBarang.append(dataBarang[-1].copy()) 

    print("Barang berhasil ditambahkan!\n")
    print(f"Nama     : {nama}")
    print(f"Kode     : {kode}")
    print(f"Jumlah   : {jumlah}")
    print(f"Expired  : {expired}")
    print(f"Kondisi  : {kondisi}")
    print(f"Kategori : {kategori}\n")

    input("Tekan ENTER untuk kembali ke menu utama...") #Apuila: menambahkan opsi kembali ke menu utama
    os.system('cls' if os.name == 'nt' else 'clear') #Apuila: Membersihkan tampilan
    return

# made by zahra aulia