list = [5, 2, 9, 1, 5, 6];
print("Original list:", list)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
     for j in range(0, n-i-1):
         if arr[j] > arr[j+1]:
             swap(arr, j, j+1)

bubble_sort(list)
print("Sorted list:", list)