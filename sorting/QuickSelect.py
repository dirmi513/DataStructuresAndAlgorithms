from QuickSort import partition


def quick_select(arr, k):
    return split(0, len(arr)-1, [num for num in arr], k)


def split(l, r, arr, k):
    if l >= r:
        return arr
    pivot = partition(l, r, arr)
    if pivot == k:
        return
    elif pivot < k:
        split(pivot+1, r, arr, k)
    else:
        split(l, pivot-1, arr, k)
    return arr


# want Kth smallest element
unsorted_array = [10, 43, 2, 5, 24, 8, 4]
k = 5
quick_select_arr = quick_select(unsorted_array, k)
print(unsorted_array,
      quick_select_arr,
      f'{k}th smallest element: {quick_select_arr[k-1]}',
      sep='\n'
      )
