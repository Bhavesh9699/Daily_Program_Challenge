def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev2 = 0
    prev1 = 1

    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current 
    
    return prev1

print(fibonacci(5))
