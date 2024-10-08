def sliding_window_max(arr, k):
    n = len(arr)
    if n == 0 or k == 0:
        return []

    result = []
    
    for i in range(n - k + 1):

        current_max = arr[i]
        for j in range(1, k):
            if arr[i + j] > current_max:
                current_max = arr[i + j]
        result.append(current_max)
    
    return result

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(arr, k)) 
