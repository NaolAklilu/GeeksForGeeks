def select(arr, i):
    return i

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = select(arr, i)
        j = i + 1

        while ( j < n):
            if(arr[j] < arr[min_index]):
                min_index = j
            j += 1

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(*arr)
