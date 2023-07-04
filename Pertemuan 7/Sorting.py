import timeit

print("Ascending")
print("")

# Insertion Sort
def insertionSort(array):
    start = timeit.default_timer()
    for i in range(1, len(array)):
        item = array [i]
        j = i - 1

        while j >= 0 and array[j] > item:
            array [j + 1] = array[j]
            j -= 1

        array[j + 1] = item

    stop = timeit.default_timer()
    print(f"Insertion time : + {stop - start}")
    return array


# Buble sort

def bubbleSort(array):
    start = timeit.default_timer()
    for i in range(len(array)):
        for j in range (len(array)):
            for j in range(len (array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1],array[j]

    stop = timeit.default_timer()
    print("bubble sort time : +",stop - start)
    return array

# Selection Sorting

def selectionSort(array):
    start = timeit.default_timer()
    for i in range(len(array)):
        min = i
        for j in range (i+1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    
    stop = timeit.default_timer()
    print("selection sort time : +", stop - start)
    return array


list_1 = [1,5,9,12,4,2,100,69]
list_2 = [1,5,9,12,4,2,100,69]
list_3 = [1,5,9,12,4,2,100,69]
print("before ", list_1)
print("before ", list_2)
print("before ", list_3)
insertionSort(list_1)
bubbleSort(list_2)
selectionSort(list_3)
print("after ", list_1)
print("after ", list_2)
print("after ", list_3)