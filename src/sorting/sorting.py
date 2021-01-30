# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements 

    # Your code here
    # initializing pointers for each array
    # a = 0
    # b = 0
    a, b = 0, 0

    for item in range(elements):
        # if arrA is complete
        if a >= len(arrA):
            merged_arr[item] = arrB[b]
            b += 1
        # if arrayB is complete
        elif b >= len(arrB):
            merged_arr[item] = arrA[a]
            a += 1
        # if element in array A is smaller than element in array B
        elif arrA[a] < arrB[b]:
            merged_arr[item] = arrA[a]
            a += 1
        # if element in array B is smaller than element in array A
        else:
            merged_arr[item] = arrB[b]
            b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    # base case
    if len(arr) > 1:
        # recursive case
        # recursively split array until each list has length of 1
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])

        # call merge function and pass in sub arrays
        arr = merge(left, right)
    return arr

arr1 = [1, 3, 8, 4, 2, 9, 7, 0, 5, 6]
print(arr1)
print(merge_sort(arr1))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
