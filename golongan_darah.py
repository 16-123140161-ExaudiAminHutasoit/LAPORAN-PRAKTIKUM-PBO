import random
# Definisikan class father
class Father:
    def __init__(self, blood_types):
        self.blood_types = list(blood_types)
# Definisikan class mother
class Mother:
    def __init__(self, blood_types):
        self.blood_types = list(blood_types)
# Definisikan class child
class Child:
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother
        self.blood_type = self.determine_blood_type()
# definisikan method determine_blood_type
    def determine_blood_type(self):
        father_allele = random.choice(self.father.blood_types)
        mother_allele = random.choice(self.mother.blood_types)
        alleles = father_allele + mother_allele
        alleles = "".join(sorted(alleles)) #untuk mengurutkan gen dari A ke O
        if alleles in ["AA", "AO"]:
            return "A"
        elif alleles in ["BB", "BO"]:
            return "B"
        elif alleles in ["AB"]:
            return "AB"
        elif alleles in ["OO"]:
            return "O"
        else:
            return "Unknown"

# Contoh penggunaan
ayah = Father("AB")
ibu = Mother("O")
anak = Child(ayah, ibu)
print(f"Golongan darah ayah: {ayah.blood_types}")
print(f"Golongan darah ibu: {ibu.blood_types}")
print(f"Golongan darah anak: {anak.blood_type}")