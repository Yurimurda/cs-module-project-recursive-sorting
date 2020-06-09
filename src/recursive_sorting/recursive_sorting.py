# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements


    a = 0
    b = 0
    # Your code here
    for k in range(0, elements):
        if a >= len(arrA):
            merged_arr[k] = arrB[b]
            b += 1

        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a += 1

        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1

        else:
            merged_arr[k] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:

        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])

        arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
