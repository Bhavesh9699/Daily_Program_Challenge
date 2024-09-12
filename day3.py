def findDuplicate(arr):
    tortoise = arr[0]
    hare = arr[0]

    while True:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
        if tortoise == hare:
            break

    tortoise = arr[0]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]

    return hare

print(findDuplicate([1, 3, 4, 2, 2]))
print(findDuplicate([3, 1, 3, 4, 2]))
print(findDuplicate([1, 1]))
print(findDuplicate([1, 4, 4, 2, 3]))

n = 99999
arr = list(range(1, n+1)) + [50000]
print(findDuplicate(arr))
