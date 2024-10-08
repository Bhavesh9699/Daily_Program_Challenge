def evaluate_postfix_expression(expression):
    stack = []
    
    
    def calculate(op1, op2, operator):
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        elif operator == '*':
            return op1 * op2
        elif operator == '/':
            return int(op1 / op2)  
    
    operators = set(['+', '-', '*', '/'])
    
    for element in expression.split():
        if element not in operators:
            stack.append(int(element))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = calculate(operand1, operand2, element)
            stack.append(result)
    
    return stack[0]

# Test cases
print(evaluate_postfix_expression("2 1 + 3 *"))                 # Output: 9
print(evaluate_postfix_expression("5 6 +"))                      # Output: 11
print(evaluate_postfix_expression("-5 6 -"))                     # Output: -11
print(evaluate_postfix_expression("15 7 1 - 1 + 3 / 2 * 1 + -"))  # Output: 5
print(evaluate_postfix_expression("5"))
