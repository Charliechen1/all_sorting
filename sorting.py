def insertion_sort(arr):
    if len(arr) < 1:
        return arr
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def  bubble_sort(arr):
    n = len(arr)
    for i in range (n):
        for j in range(1, n - i):
            j = n - j
            if arr[j] < arr[j-1]:
                tmp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = tmp
    return arr


def better_bubble_sort(arr):
    n = len(arr)
    flag = True
    for i in range(n):
        if flag is False:
            return arr
        flag = False
        for j in range(1, n - i):
            j = n - j
            if arr[j] < arr[j - 1]:
                tmp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = tmp
                flag = True
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[min] > arr[j]:
                min = j
        tmp = arr[min]
        arr[min] = arr[i]
        arr[i] = tmp
    return arr

a = [5,3,2,1,4]

#b = insertion_sort(a)
#c = bubble_sort(a)
#d = selection_sort(a)
e = better_bubble_sort(a)
print(e)

