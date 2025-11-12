# stok_module.py
# Program Manajemen Stok Sederhana
# Menggunakan: input/output, percabangan, perulangan, dictionary, dan list (array)

# Data produk disimpan dalam list of dictionary
stok_produk = []

def tambah_produk():
    print("\n=== Tambah Produk ===")
    kode = input("Masukkan kode produk: ")
    nama = input("Masukkan nama produk: ")
    try:
        jumlah = int(input("Masukkan jumlah stok awal: "))
    except ValueError:
        print("Input jumlah harus angka!")
        return
    
    # Simpan sebagai dictionary
    produk = {
        "kode": kode,
        "nama": nama,
        "stok": jumlah
    }
    stok_produk.append(produk)
    print(f"Produk '{nama}' berhasil ditambahkan!\n")

def tampilkan_stok():
    print("\n=== Daftar Stok Produk ===")
    if not stok_produk:
        print("Belum ada produk yang disimpan.")
        return
    for i, p in enumerate(stok_produk):
        print(f"{i+1}. {p['kode']} - {p['nama']} (Stok: {p['stok']})")

def cari_produk():
    print("\n=== Cari Produk ===")
    keyword = input("Masukkan nama/kode produk: ").lower()
    ditemukan = False
    for p in stok_produk:
        if keyword in p["nama"].lower() or keyword in p["kode"].lower():
            print(f"Ditemukan: {p['kode']} - {p['nama']} (Stok: {p['stok']})")
            ditemukan = True
    if not ditemukan:
        print("Produk tidak ditemukan.")

def update_stok():
    print("\n=== Update Stok Produk ===")
    kode = input("Masukkan kode produk: ")
    for p in stok_produk:
        if p["kode"] == kode:
            print(f"Produk ditemukan: {p['nama']} (Stok sekarang: {p['stok']})")
            print("1. Tambah stok")
            print("2. Kurangi stok")
            pilihan = input("Pilih (1/2): ")
            try:
                jumlah = int(input("Masukkan jumlah: "))
            except ValueError:
                print("Input harus angka!")
                return
            if pilihan == "1":
                p["stok"] += jumlah
                print(f"Stok bertambah. Sekarang: {p['stok']}")
            elif pilihan == "2":
                if jumlah <= p["stok"]:
                    p["stok"] -= jumlah
                    print(f"Stok berkurang. Sekarang: {p['stok']}")
                else:
                    print("Stok tidak cukup!")
            else:
                print("Pilihan tidak valid.")
            return
    print("Produk tidak ditemukan.")

def hapus_produk():
    print("\n=== Hapus Produk ===")
    kode = input("Masukkan kode produk yang akan dihapus: ")
    for p in stok_produk:
        if p["kode"] == kode:
            stok_produk.remove(p)
            print(f"Produk {p['nama']} berhasil dihapus.")
            return
    print("Produk tidak ditemukan.")

# ===============================
# Bagian utama program (main loop)
# ===============================
if __name__ == "__main__":
    while True:
        print("\n=== Aplikasi Manajemen Stok Sederhana ===")
        print("1. Tambah Produk")
        print("2. Tampilkan Stok")
        print("3. Cari Produk")
        print("4. Update Stok")
        print("5. Hapus Produk")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            tampilkan_stok()
        elif pilihan == "3":
            cari_produk()
        elif pilihan == "4":
            update_stok()
        elif pilihan == "5":
            hapus_produk()
        elif pilihan == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")
