import random

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


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
                swap(arr, j-1, j)
                flag = True
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[min] > arr[j]:
                min = j
        swap(arr, i, min)
    return arr


def merge(a, b):
    res = []
    if len(a) is 0:
        res = res + b
        return res
    if len(b) is 0:
        res = res + a
        return res
    if a[0] > b[0]:
        return res + [b[0]] + merge(a, b[1:])
    if a[0] < b[0]:
        return res + [a[0]] + merge(a[1:], b)


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        n = int(len(arr) / 2)
        return merge(merge_sort(arr[:n]), merge_sort(arr[n:]))

def random_quick_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    p_arr, pivot = particition(arr)
    res = random_quick_sort(p_arr[:pivot]) + [arr[pivot]] + random_quick_sort(p_arr[pivot + 1 : n])
    return res

def particition(arr):
    n = len(arr)
    pivot = random.randint(0, n - 1)
    swap(arr, -1, pivot)
    i = 0
    j = n-2
    while i <= j:
        if arr[j] < arr[-1] < arr[i]:
            swap(arr, i, j)
        if arr[i] < arr[-1]:
            i += 1
        if arr[j] > arr[-1]:
            j -= 1
    swap(arr, -1, i)
    return arr, i



a = [2,4,1,3,5,7,6,0,9,8]
b = [1, 0]
print(random_quick_sort(a))