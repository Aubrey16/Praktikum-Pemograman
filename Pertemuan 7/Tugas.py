import time
# masukan nilai menggunakan bubble sort
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range (len(arr)):
            for j in range(len (arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1],arr[j]
    return array

jumlah = int(0)
Kata = int(input("masukan brp Nilai : "))
array = []
while jumlah != Kata :
    jumlah += 1
    Jawaban = int(input("masukan nilai : "))
    array.append(Jawaban)

print("before",array)
bubbleSort(array)
print("after",array)

# mengurutkan nama menggunakan selection sort

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range (i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

jumlah2 = int(0)
Kata2 = int(input("masukan brp Nama yang akan dimasukan : "))
array2 = []
while jumlah2 != Kata2:
    jumlah2 += 1
    Jawaban2 = input("masukan nama : ")
    array2.append(Jawaban2)


print("before", array2)
selectionSort(array2)
print("after", array2)

# mengurutkan buku menggunakan insertion sort

def insertionSortASC(arr):
    for i in range(1, len(arr)):
        item = arr [i]
        j = i - 1

        while j >= 0 and arr[j] > item:
            arr [j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item
    return arr

def insertionSortDSC(arr):
    for i in range(1, len(arr)):
        item = arr [i]
        j = i - 1

        while j >= 0 and arr[j] < item :
            arr [j + 1] = arr [j]
            j -= 1
            arr[j + 1]= item
    return arr


jumlah3 = int(0)
Kata3 = int(input("masukan brp buku yang akan dimasukan : "))
jawaban = (1, 2)
array3 = []
counter = 0
while jumlah3 != Kata3:
    jumlah3 += 1
    Jawaban2 = input("masukan nama buku : ")
    array3.append(Jawaban2)
print()
print("<------------------------>")
print("1. insertion ascending")
print("2. insertion descending")
print("<------------------------>")
print()
pengurutan = int(input("Pengurutan : "))

while pengurutan < 1 or pengurutan > 2 :
    counter += 1
    print ("salah : ", counter)
    pengurutan = int(input("salah, masukan lagi : "))
    if counter == 2 :
        print("salah : ", counter + 1)
        print("self destruct in ")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        print("duarr")
        break

if pengurutan == 1 :
    print ("sorting buku secara ascending")
    insertionSortASC(array3)
    print (array3)
elif pengurutan == 2 : 
    print ("sorting buku descending")
    insertionSortDSC(array3)
    print (array3)