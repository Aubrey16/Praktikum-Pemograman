# Menampilkan bilangan genap
Bilangan = [1,2,3,4,5,6,7,8,9,10]
for i in Bilangan:
    if i % 2 == 0 :
        print(i)

# Input dan Output array
jumlah = int(0)
Kata = int(input("masukan brp kata : "))
array = []
while jumlah != Kata :
    jumlah += 1
    Jawaban = input("masukan kata : ")
    array.append(Jawaban)

print (array)


Jaw = (input("yang mana : "))
if Jaw not in array :
    print("ga ada")
else:
    arrarJ = array.index(Jaw)
    print("dia ada di posisi indeks array ke",arrarJ)

# Mencari predikat
Predikat = ["A"," B", "C", "D", "E"]
Nilai1 = int(input("Masukan nilai Matkul ke 1 : "))
Nilai2 = int(input("Masukan nilai Matkul ke 2 : "))
Nilai3 = int(input("Masukan nilai Matkul ke 3 : "))
Nilai4 = int(input("Masukan nilai Matkul ke 4 : "))
Nilai5 = int(input("Masukan nilai Matkul ke 5 : "))
Nila = Nilai1 + Nilai2 + Nilai3 + Nilai4 + Nilai5
Nilai = Nila / 5
def TotNil():
    print()
    print("dengan nilai Matkul 1 : ",Nilai1)
    print("dengan nilai Matkul 2 : ",Nilai2)
    print("dengan nilai Matkul 3 : ",Nilai3)
    print("dengan nilai Matkul 4 : ",Nilai4)
    print("dengan nilai Matkul 5 : ",Nilai5)
if Nilai1 > 100 or Nilai2 > 100 or Nilai3 > 100 or Nilai4 > 100 or Nilai5 > 100 or Nilai1 < 1 or Nilai2 < 1 or Nilai3 < 1 or Nilai4 < 1 or Nilai5 < 1 :
    print("Tidak valdi")
elif Nilai == 100 or Nilai >= 90:
    print()
    print("antum dapet ", Predikat[0])
    TotNil()
elif Nilai < 90 and Nilai >= 70  :
    print()
    print("antum dapet ", Predikat[1])
    TotNil()
elif Nilai < 70 and Nilai >= 50 :
    print()
    print("antum dapet ", Predikat[2])
    TotNil()
elif Nilai < 50 and Nilai >= 30 :
    print()
    print("antum dapet ", Predikat[3])
    TotNil()
elif Nilai < 30 and Nilai >= 0 :
    print()
    print("antum dapet ", Predikat[4])
    TotNil()














