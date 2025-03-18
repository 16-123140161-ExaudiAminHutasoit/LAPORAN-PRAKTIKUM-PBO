#defenisi class kalkulator
class Kalkulator:
    def __init__(self, angka):
        self.angka = angka
    def __add__(self, angka_lain):
        
         Kalkulator(self.angka + angka_lain.angka)

    def __sub__(self, angka_lain):
        return Kalkulator(self.angka - angka_lain.angka)

    def __mul__(self, angka_lain):
        return Kalkulator(self.angka * angka_lain.angka)

    def __truediv__(self, angka_lain):
        if angka_lain.angka == 0:
            return "Pembagian dengan nol gabisa"
        return Kalkulator(self.angka / angka_lain.angka)

    def __str__(self):
        return str(self.angka)

# Contoh penggunaan
angka1 = Kalkulator(9)
angka2 = Kalkulator(3)

print(angka1 + angka2) 
print(angka1 - angka2) 
print(angka1 * angka2)
print(angka1 / angka2)  
print(Kalkulator(8) / Kalkulator(2)) # Output: Pembagian dengan nol tidak diizinkan