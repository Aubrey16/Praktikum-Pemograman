# Function
Sisi = int(input("masukan sisi :"))

def Hitung_Keliling(Sisi):
    hasil = (4 * Sisi)
    return hasil

print (Hitung_Keliling(Sisi))

def Hitung_Luas(Sisi):
    hasil = (Sisi * Sisi)
    return hasil

print (Hitung_Luas(Sisi))

# Mencari angka paling gede
Masukan_angka1 = int(input("Masukan angka :"))
Masukan_angka2 = int(input("Masukan angka :"))


def Hitung_Perbandingan():
    if Masukan_angka1 > Masukan_angka2 :
        print (Masukan_angka1,",", Masukan_angka2)
    else :
        print (Masukan_angka2,",", Masukan_angka1)
    
Hitung_Perbandingan()