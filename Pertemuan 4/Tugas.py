# Program Menghitung Jumlah Total Bilangan

# Bilangan = int(input("Masukan bilangan :"))
# total = 0

# for i in range(Bilangan, 0, -1):
#     print (i, end="")
#     if i != 1 :
#         print(" + ", end="")
#     elif i == 1 :
#         print(" = ", end="")
#     total = total + i
# print (total, end="")


# # end
# print("")
# print("")
# Program Penghitung Pangkat


# Bilangan1 = int(input("Masukan bilangan ="))
# Bilangan2 = int(input("Masukan bilangan ="))
# Bilangan12 = Bilangan1 + Bilangan2
# Pangkat = int(input("Masukan Pangkat ="))

# print(Bilangan12 ** Pangkat)

# # atau

# Bilangan1 = int(input("Masukan bilangan ="))
# Bilangan2 = int(input("Masukan bilangan ="))
# Bilangan12 = Bilangan1 + Bilangan2
# Pangkat = int(input("Masukan Pangkat ="))
# HasilPangkat = Bilangan12

# for a in range (Pangkat - 1):
#     HasilPangkat *= Bilangan12
# print (HasilPangkat)

# # end
# print()
# print()
# mencari kpk

Bila = int(input ("Masukan Bilangan ="))
Bilb = int(input ("Masukan Bilangan ="))
BilC = Bila * Bilb


for k in range(1,BilC + 1):
    if(k%Bila==0 and k%Bilb==0):
        print(k)
        break
# # end



