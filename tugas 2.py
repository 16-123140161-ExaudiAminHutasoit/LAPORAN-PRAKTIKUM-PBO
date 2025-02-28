data = {}
i = 0

jumlah = int(input("jumlah siswa :"))

while i < jumlah:
    siswa = input(f"masukkan nama siswa ke-{i+1}:")
    nilai = input(f"masukkan nilai {siswa}: ")
    data[siswa] = nilai
    i+= 1
    
print("dictionary = ",data)