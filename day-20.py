def sortedInsert(stack, value):
    if len(stack) == 0 or stack[-1] <= value:
        stack.append(value)
    else:
        temp = stack.pop()
        sortedInsert(stack, value)
        stack.append(temp)

def sortStack(stack):
    if len(stack) > 0:
        temp = stack.pop()
        sortStack(stack)
        sortedInsert(stack, temp)

# Test cases
stack1 = [3, 1, 4, 2]
sortStack(stack1)
print(stack1)

stack2 = [7, 1, 5]
sortStack(stack2)
print(stack2)

stack3 = [5]
sortStack(stack3)
print(stack3)

stack4 = [-3, 14, 8, 2]
sortStack(stack4)
print(stack4)

stack5 = []
sortStack(stack5)
print(stack5)

stack6 = [3, 3, 3]
sortStack(stack6)
print(stack6)
