class VendingMachineFSM:
    def __init__(self):
        self.state = "Idle"
        self.transitions = {
            "Idle": {"masukkan_uang": "MenungguProduk"},
            "MenungguProduk": {"pilih_produk": "MengeluarkanProduk", "reset": "Idle"},
            "MengeluarkanProduk": {"keluarkan_produk": "Selesai"},
            "Selesai": {"reset": "Idle"}
        }

    def ubah_state(self, aksi):
        if aksi in self.transitions[self.state]:
            self.state = self.transitions[self.state][aksi]
            print(f"Transisi ke: {self.state}")
        else:
            print(f"Aksi '{aksi}' tidak valid dari state '{self.state}'")

    def jalankan(self):
        while self.state != "Selesai":
            aksi = input(f"State saat ini: {self.state}. Masukkan aksi: ")
            if aksi.lower() == "exit":
                break
            self.ubah_state(aksi)

# Jalankan mesin
mesin = VendingMachineFSM()
mesin.jalankan()