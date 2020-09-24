def quick_sort(arr):
    return split(0, len(arr)-1, [num for num in arr])


def split(l, r, arr):
    if l >= r:
        return arr
    pivot = partition(l, r, arr)
    split(l, pivot-1, arr)
    split(pivot+1, l, arr)
    return arr


def partition(i, j, arr):
    pivot = arr[i]
    oi = i
    i += 1
    while True:
        while i < j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i >= j:
            break
        oj = arr[j]
        arr[j] = arr[i]
        arr[i] = oj
    oj = arr[j]
    arr[j] = arr[oi]
    arr[oi] = oj
    return j


unsorted_array = [10, 43, 2, 5, 24, 8, 4]
sorted_array = quick_sort(unsorted_array)
print(unsorted_array, sorted_array, sep='\n')
