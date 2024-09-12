import math

def merge_in_place(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    def next_gap(gap):
        if gap <= 1:
            return 0
        return math.ceil(gap / 2)

    gap = m + n

    while gap > 0:
        gap = next_gap(gap)
        
        i = 0
        while i + gap < m:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

        j = max(0, gap - m)
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        if j < n:
            j = 0
            while j + gap < n:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merge_in_place(arr1, arr2)
print("Test Case 1 - arr1:", arr1)
print("Test Case 1 - arr2:", arr2)

arr1 = [10, 12, 14]
arr2 = [1, 3, 5]
merge_in_place(arr1, arr2)
print("Test Case 2 - arr1:", arr1)
print("Test Case 2 - arr2:", arr2)

arr1 = [2, 3, 8]
arr2 = [4, 6, 10]
merge_in_place(arr1, arr2)
print("Test Case 3 - arr1:", arr1)
print("Test Case 3 - arr2:", arr2)

arr1 = [1]
arr2 = [2]
merge_in_place(arr1, arr2)
print("Test Case 4 - arr1:", arr1)
print("Test Case 4 - arr2:", arr2)

arr1 = list(range(1, 50001))
arr2 = list(range(50001, 100001))
merge_in_place(arr1, arr2)
print(f"Test Case 5 - arr1 first number: {arr1[0]}, arr1 last number: {arr1[-1]}")
print(f"Test Case 5 - arr2 first number: {arr2[0]}, arr2 last number: {arr2[-1]}")

