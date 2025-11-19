from dataDummy import dataBarang

def cariBarang():
    print("\n--- search barang ---")
    try:
        key = input("masukkan nama barang: ").lower()
        found = False
        for s in dataBarang:
            if key in s["nama"].lower() or key in s["kode"].lower():
                print(f"found: {s['kode']} - {s['nama']} (stok: {s['stok']})")
                found = True
    except ValueError:
        if not found:
            print("barang tidak ditemukan.")
