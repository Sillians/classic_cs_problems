arr = [-2, 3, 4, 7, 8, 9, 11, 13]
target = 11

def linear_search(arr: list, target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return(i, target)
        
print(linear_search(arr, target))

