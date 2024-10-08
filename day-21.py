def push_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        push_bottom(stack, item)
        stack.append(temp)

def reverse_stack_recursive(stack):
    if len(stack) > 0:
        temp = stack.pop()
        reverse_stack_recursive(stack)
        push_bottom(stack, temp)

# Test Cases
stack1 = [1, 2, 3, 4]
reverse_stack_recursive(stack1)
print(stack1)

stack2 = [3, 2, 1]
reverse_stack_recursive(stack2)
print(stack2)

stack3 = [5]
reverse_stack_recursive(stack3)
print(stack3)

stack4 = [-5, -10, -15]
reverse_stack_recursive(stack4)
print(stack4)

stack5 = []
reverse_stack_recursive(stack5)
print(stack5)

stack6 = [3, 3, 3]
reverse_stack_recursive(stack6)
print(stack6)
