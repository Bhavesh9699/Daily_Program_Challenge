def find_zero_sum_subarrays(arr):
    prefix_sum_map = {}
    prefix_sum = 0
    result = []
    
    for i in range(len(arr)):
        prefix_sum += arr[i]
        
        if prefix_sum == 0:
            result.append((0, i))
        
        if prefix_sum in prefix_sum_map:
            for start in prefix_sum_map[prefix_sum]:
                result.append((start + 1, i))
        
        if prefix_sum not in prefix_sum_map:
            prefix_sum_map[prefix_sum] = []
        
        prefix_sum_map[prefix_sum].append(i)
    
    return result

arr = [1, 2, -3, 3, -1, 2]
result = find_zero_sum_subarrays(arr)
print(result)
