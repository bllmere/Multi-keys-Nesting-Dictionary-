import datetime
import random
import string

# Nested dictionary utama untuk menyimpan data buku
# Struktur: { "KEY_BUKU": { "judul": ..., "penulis": ..., "tahun": ..., "tgl_pinjam": ..., "tersedia": ... } }
data_buku = {
    "BK-A1B2": {
        "judul": "Laskar Pelangi",
        "penulis": "Andrea Hirata",
        "tahun": 2005,
        "tgl_pinjam": datetime.date(2026, 10, 15),
        "tersedia": True,
    },
    "BK-C3D4": {
        "judul": "Bumi Manusia",
        "penulis": "Pramoedya Ananta Toer",
        "tahun": 1980,
        "tgl_pinjam": datetime.date(2026, 11, 10),
        "tersedia": False,
    },
}


def generate_key(prefix="BK"):
    """Membuat key unik multi-karakter yang belum terpakai."""
    while True:
        acak = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
        key = f"{prefix}-{acak}"
        if key not in data_buku:
            return key


def tambah_buku():
    """Menambahkan buku baru ke dalam nested dictionary."""
    print("\n=== TAMBAH BUKU BARU ===")
    judul = input("Judul Buku     : ").strip()
    penulis = input("Penulis        : ").strip()

    while True:
        try:
            tahun = int(input("Tahun Terbit   : ").strip())
            break
        except ValueError:
            print("Tahun harus berupa angka (contoh: 2024). Coba lagi.")

    tgl_input = input(
        "Tanggal Terakhir Pinjam (YYYY-MM-DD, kosongkan jika belum pernah): "
    ).strip()
    if tgl_input:
        try:
            tgl_pinjam = datetime.date.fromisoformat(tgl_input)
        except ValueError:
            print("Format tanggal tidak valid, diset menjadi '-' (belum pernah).")
            tgl_pinjam = None
    else:
        tgl_pinjam = None

    while True:
        status_input = input("Apakah buku tersedia? (ya/tidak): ").strip().lower()
        if status_input in ("ya", "y", "tersedia", "true", "1"):
            tersedia = True
            break
        elif status_input in ("tidak", "t", "tdk", "false", "0"):
            tersedia = False
            break
        else:
            print("Masukkan 'ya' atau 'tidak'.")

    key_baru = generate_key()
    data_buku[key_baru] = {
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun,
        "tgl_pinjam": tgl_pinjam,
        "tersedia": tersedia,
    }

    print(f"\nBuku '{judul}' berhasil ditambahkan dengan KEY: {key_baru}")


def tampilkan_buku():
    """Menampilkan seluruh buku dalam format tabel sesuai kolom yang diminta."""
    header = (
        f"{'KEYS':<10} "
        f"{'JUDUL BUKU':<28} "
        f"{'PENULIS':<24} "
        f"{'TAHUN TERBIT':<14} "
        f"{'TANGGAL TERAKHIR PINJAM':<25} "
        f"{'STATUS (TERSEDIA / TIDAK)':<26}"
    )
    garis_pemisah = "- " * 60

    print("\n" + garis_pemisah.strip())
    print(header)
    print(garis_pemisah.strip())

    if not data_buku:
        print("Belum ada data buku di dalam sistem.")
        print(garis_pemisah.strip())
        return

    for key, info in data_buku.items():
        judul = info["judul"]
        penulis = info["penulis"]
        tahun = str(info["tahun"])
        tgl_str = (
            info["tgl_pinjam"].strftime("%Y-%m-%d")
            if isinstance(info["tgl_pinjam"], datetime.date)
            else "-"
        )
        status_str = "TERSEDIA" if info["tersedia"] else "TIDAK"

        baris = (
            f"{key:<10} "
            f"{judul:<28} "
            f"{penulis:<24} "
            f"{tahun:<14} "
            f"{tgl_str:<25} "
            f"{status_str:<26}"
        )
        print(baris)

    print(garis_pemisah.strip())


def main():
    while True:
        print("\n=== SISTEM MANAJEMEN PERPUSTAKAAN ===")
        print("1. Tampilkan Semua Buku")
        print("2. Tambah Buku Baru")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == "1":
            tampilkan_buku()
        elif pilihan == "2":
            tambah_buku()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem perpustakaan.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")


if __name__ == "__main__":
    main()