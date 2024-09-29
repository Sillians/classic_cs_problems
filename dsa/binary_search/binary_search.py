arr = [-2, 3, 4, 7, 8, 9, 11, 13]
target = 11

def binary_search(arr: list, target: int) -> int:
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(binary_search(arr, target))

# Time complexity
# A binary search is significantly faster than a simple search for sorted lists.
# Big O notation `(O(log n))` helps quantify how algorithm efficiency scales with input size, 
# compared to linear notation `(O(n))`. 