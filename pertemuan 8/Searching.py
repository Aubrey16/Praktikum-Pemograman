import timeit
# Linear search
def linear_search(keyword, data):
    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower() :
            print("keyword", keyword, "has found at index", i)
            return i

    print("keyword", keyword,"not found")
    return -1

data = [23,3,4,38,581,59]
print(data)
keyword = input("Input keyword :")
linear_search(keyword, data)

# binary search

def bubbleSort(data):
    for i in range(len(data)):
        for j in range (len(data) - i - 1):
            if data[j] > data[j + 1] :
                data[j], data[j+1] = data[j+1],data[j]
    return data

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



data = [2, 5, 8, 12, 16, 23, 98, 55, 14, 21]
bubbleSort(data)
print(data)
key = int(input("apa yang mau di pilih :"))

Hasil = binary_search(data, key)

if Hasil != -1:
    print(f"ada di index ke {Hasil}.")
else:
    print("Ga ada cuy")

