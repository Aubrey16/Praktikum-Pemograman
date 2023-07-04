def bubbleSort(data):
    for i in range(len(data)):
        for j in range (len(data) - i - 1):
            if data[j] > data[j + 1] :
                data[j], data[j+1] = data[j+1],data[j]
    return data

def linear_search(keyword, data):
    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower() :
            print("Plat nomernya ada nih", keyword)
            return i
    print("hmmm sepertinya plat nomer", keyword,"ga ada deh")
    return -1

def binary_search(data, Key):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == Key:
            return mid
        elif data[mid] < Key:
            left = mid + 1
        else:
            right = mid - 1

    return -1 

# Pak polisi nyari plat

PlatNomer =  ["R 2477 SR", "R 1234 DJ","R 7015 LP","R 0201 RR", "R 3304 DA", "R 2401 SK","R 2103 RT", "R 1708RI", "R 1111 SR", "R 4987 LH"]
Nomer = input("Input Platnomer :")
linear_search(Nomer, PlatNomer)

# Nyari nim

Nim = [20103023, 20103002, 20103019, 20103001, 20103017, 20103005, 20103011, 20103003, 20103009, 20103021, 20103006, 20103015, 20103013, 20103007]

bubbleSort(Nim)
key = int(input("masukan nimnya : "))

Hasil = binary_search(Nim, key)

if Hasil != -1:
    print(f"ada nih cuy di index {Hasil}.")
else:
    print("Ga ada cuy")

# gacha bilangan
Bilacak = [17, 2, 15, 7, 72, 31, 12, 57, 63, 71, 23, 92, 1]

bubbleSort(Bilacak)
Bilangan = int(input("Masukan bilangannya : "))

cari = binary_search(Bilacak, Bilangan)

if cari != -1 :
    print (f"ada nih cuy di index {cari}")
else :
    print ("ga ada cuy")