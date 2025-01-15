class AntrianRestoran:
    def _init_(self):
        self.antrian = []  # List untuk menyimpan data antrian

    def enqueue(self, nama_pelanggan):
        """Menambahkan pelanggan ke dalam antrian."""
        self.antrian.append(nama_pelanggan)
        print(f"{nama_pelanggan} telah ditambahkan ke dalam antrian.")

    def dequeue(self):
        """Menghapus pelanggan dari antrian."""
        if len(self.antrian) > 0:
            pelanggan = self.antrian.pop(0)
            print(f"{pelanggan} telah dilayani dan dihapus dari antrian.")
            return pelanggan
        else:
            print("Antrian kosong, tidak ada pelanggan untuk dilayani.")
            return None

    def tampilkan_antrian(self):
        """Menampilkan daftar antrian."""
        if len(self.antrian) > 0:
            print("Daftar antrian saat ini:")
            for i, pelanggan in enumerate(self.antrian, start=1):
                print(f"{i}. {pelanggan}")
        else:
            print("Antrian kosong.")

if _name_ == "_main_":
    restoran = AntrianRestoran()

    while True:
        print("\n=== Sistem Antrian Restoran ===")
        print("1. Tambah ke antrian (Enqueue)")
        print("2. Layani pelanggan (Dequeue)")
        print("3. Tampilkan antrian")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()

        if pilihan == "1":
            nama = input("Masukkan nama pelanggan: ").strip()
            restoran.enqueue(nama)
        elif pilihan == "2":
            restoran.dequeue()
        elif pilihan == "3":
            restoran.tampilkan_antrian()
        elif pilihan == "4":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
