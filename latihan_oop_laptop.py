class Laptop:
    def __init__(self):
        self.power = 0  # Daya awal 0%

    def charge(self, duration):
        self.power += duration * 1  # 1% per menit
        if self.power > 100:
            self.power = 100

    def play_game(self, duration):
        self.power -= duration * 1  # 1% per menit
        if self.power < 0:
            self.power = 0

    def coding(self, duration):
        self.power -= duration * 0.1  # 1% per 10 menit
        if self.power < 0:
            self.power = 0

    def browsing(self, duration):
        self.power -= duration * 0.2  # 2% per 10 menit
        if self.power < 0:
            self.power = 0

    def play_audio(self, duration):
        self.power -= duration * 0.5  # 5% per 10 menit
        if self.power < 0:
            self.power = 0


laptop = Laptop()

laptop.charge(120)  #  (120 menit)
laptop.play_game(60)  # (60 menit)
laptop.browsing(60)  #  (60 menit)
laptop.charge(20)  # (20 menit)
laptop.coding(120)  # (120 menit)
laptop.play_audio(120)  # (120 menit)

print("Daya laptop setelah semua tindakan:", laptop.power, "%")
