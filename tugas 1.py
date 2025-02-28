def print_piramida(tinggi):
    for i in range(tinggi):
        spasi = ' '* (tinggi - i - 1)
        bintang = '*' * (2 * i + 1)
        
        print(spasi + bintang)
        
        
        
tinggi = int(input("masukkan tinggi yang anda mau : "))
print_piramida(tinggi)