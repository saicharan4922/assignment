# implementation of binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
arr = [1, 3, 4, 6, 8, 9, 11]
target = 4

index = binary_search(arr, target)

if index != -1:
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found in the list.")

# implementation of merge sort
def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr
arr = [6, 2, 7, 3, 8, 9, 1, 5, 4]
sorted_arr = merge_sort(arr)

print(f"The sorted array is: {sorted_arr}")


# implementation of quick sort

def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
arr = [6, 2, 7, 3, 8, 9, 1, 5, 4]
sorted_arr = quick_sort(arr)

print(f"The sorted array is: {sorted_arr}")


# implementation of insertion sort

def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
arr = [6, 2, 7, 3, 8, 9, 1, 5, 4]
sorted_arr = insertion_sort(arr)

print(f"The sorted array is: {sorted_arr}")

# Write a program to sort list of strings (similar to that of dictionary)
def sort_strings(lst):
    
    split_lst = [s.split() for s in lst]
    sorted_lst = sorted(split_lst, key=lambda x: x[0])
    sorted_strings = [' '.join(lst) for lst in sorted_lst]

    return sorted_strings

lst = ['Banana','Apple','Orange','Carrot','Kiwi','Jack']
sorted_lst = sort_strings(lst)

print(f"The sorted list is: {sorted_lst}")
