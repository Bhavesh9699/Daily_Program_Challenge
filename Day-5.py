def find_leaders(arr):
    n = len(arr)
    leader = []
    last_digit = arr[n-1]
    leader.append(arr[n-1])
    for i in range(n-2, -1, -1):
        if arr[i] > last_digit:
            last_digit = arr[i]
            leader.append(last_digit)
    return leader[::-1]
arr = list(map(int, input().split(",")))
ans = find_leaders(arr)
print(ans)
