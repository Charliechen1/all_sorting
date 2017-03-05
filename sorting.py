import random

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


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
    n = len(arr)/
                swap(arr, j-1, j)
                # here the flag = false means we find that the array has already been sorted, then nothing useless need to be doneuIKm.,
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
    res = random_quick_sort(p_arr[:pivot]) + \
          [arr[pivot]] + \
          random_quick_sort(p_arr[pivot + 1 : n])
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

def max_heap_sort(arr):
    heap_size = len(arr)
    build_max_heap(arr)
    for i in range(1, heap_size):
        swap(arr, 0, heap_size - i)
        arr = max_heapify(arr[0 : heap_size - i], 0) + \
              arr[heap_size - i : heap_size]
    return arr

def max_heapify(arr, i):
    heap_size = len(arr)
    largest = i
    left, right = 2*i+1, 2*i+2
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        swap(arr, i, largest)
        max_heapify(arr, largest)
    return arr

def build_max_heap(arr):
    for i in reversed(range(0, int(len(arr) / 2))):
        max_heapify(arr, i)
    return arr

def count_sort(arr, k=0):
    mina = min(arr)
    maxa = max(arr)
    if k == 0:
        k = maxa - mina + 1
    l = len(arr)
    B = [0] * l
    C = [0] * k
    for a in arr:
        index = a - mina
        C[index] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for i in reversed(range(l)):
        index = arr[i] - mina
        B[C[index]-1] = arr[i]
        C[index] -= 1
    return B




a = [2,4,1,3,5,5,5,5,7,6,0,9,8,-1,-3]
b = [1, 0]
print(count_sort(a))