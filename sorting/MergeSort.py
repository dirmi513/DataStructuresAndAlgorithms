def merge_sort(arr):
    return divide_and_conquer(arr)


def divide_and_conquer(arr):
    # base case
    if len(arr) <= 1:
        return arr
    l, r = 0, len(arr)
    mid = (l+r)//2
    left = divide_and_conquer(arr[:mid])
    right = divide_and_conquer(arr[mid:])
    return merge_sort_arrays(left, right)


def merge_sort_arrays(arr1, arr2):
    if arr1 and not arr2:
        return arr1
    if arr2 and not arr1:
        return arr2
    p1 = p2 = 0
    merged_sorted_list = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            merged_sorted_list.append(arr1[p1])
            p1 += 1
        else:
            merged_sorted_list.append(arr2[p2])
            p2 += 1
    return merged_sorted_list + arr1[p1:] + arr2[p2:]


unsorted_array = [10, 43, 2, 5, 24, 8, 4]
sorted_array = merge_sort(unsorted_array)
print(unsorted_array, sorted_array, sep='\n')

# unsorted_array = [10, 43, 2, 5, 24, 8, 4]
# divide_and_conquer will first sort the left half of the array:
#   [10, 43, 2]
#   it will first sort the left half of that array: [10], which is already sorted
#   then the right half of that array: [43, 2]
#       it will first sort the left half of the array: [43], which is already sorted
#       it will then sort the right half of the array: [2], which is already sorted
#       then run merge_sort_arrays on the left [43] and right [2] half to get [2, 43]
#   then it will run merge_sort_arrays on the left [10] and right [2, 43] half to get
#   [2, 10, 43]
# divide_and_conquer will then sort the right half of the array: [5, 24, 8, 4]
#   [5, 24, 8, 4]
#   it will first sort the left half of that array: [5, 24]
#       left and right = [5] and [24] and then merged = [5, 24]
#   then the right half of that array: [8, 4]
#       left and right = [8] and [4] and then merged = [4, 8]
#   then it will run merge_sort_arrays on the left [5, 24] and right [4, 8] half to get
#   [4, 5, 8, 24]
# finally, merge_sort_arrays on the left [2, 10, 43] and right [4, 5, 8, 24] half to get
# [2, 4, 5, 8, 10, 24, 43]
