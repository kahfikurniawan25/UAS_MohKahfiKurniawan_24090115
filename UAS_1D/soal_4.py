class Buah:
    def _init_(self, nama="", warna="", rasa=""):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

    def displayInfo(self):
        print(f"Nama Buah  : {self.nama}")
        print(f"Warna Buah : {self.warna}")
        print(f"Rasa Buah  : {self.rasa}")

if _name_ == "_main_":
    buah1 = Buah()

    buah1.setNama("Mangga")
    buah1.setWarna("Hijau")
    buah1.setRasa("Manis")

    print("Informasi Buah:")
    buah1.displayInfo()