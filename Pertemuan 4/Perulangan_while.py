# i = 0
# while i <= 7:
#     print("hello world")
#     i += 1

# i = 8
# while i >=10 :
#         print(i)
#         i += 1

#         if i == -130:
#                 break
#         if i == 120:
#                 continue
#         if i == 150:
#                 break

# a = 1
# b = 11
# while a < b :
#     print("Step ke-", a)
#     a += 1

while True:

    nama = (input("Masukan nama mu :"))
    password = (input("Masukan password :"))

    Masukannama = (input("username :"))
    masukanpassword = (input("password :"))

    data = (nama , password)
    while Masukannama not in data and masukanpassword not in password :
        print("ulang")
        Masukannama = (input("isi lagi :"))
        masukanpassword = (input("isi lagi :"))
        
    if Masukannama == nama and masukanpassword == password :
        print("selamat datang")
        break
    break