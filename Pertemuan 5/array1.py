angka = [1,2,3,4,5,6,7,8,9,10,11]
angka2 = ["satu", "dua", "tiga", "empat"]

a = angka[3]
print (a)

# print array

print (angka)
print (angka2)

# menambahkan element array di akhir

angka2.append("Lima")
print(angka2)

# mengganti element array

angka2[1] = "Sepuluh"
print (angka2)

# menentukan panjang array

panjang = len(angka2)
print(panjang)

# looping array

for i in angka2:
    print(i)

# menghapus element array

angka2.pop(2) #memanggil index 
angka2.remove("satu") #memanggil data

print(angka2)