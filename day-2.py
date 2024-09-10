def missing_num(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    mis_num = total_sum - actual_sum

    return mis_num


arr = [1, 2, 4, 5]

print(missing_num(arr))