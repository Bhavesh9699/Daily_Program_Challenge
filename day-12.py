def validate_brackets(input_string):
    temp_stack = []
    matching_pairs = {')': '(', '}': '{', ']': '['}
    for symbol in input_string:
        if symbol in '({[':
            temp_stack.append(symbol)
        elif symbol in ')}]':
            if not temp_stack or temp_stack[-1] != matching_pairs[symbol]:
                return False
            temp_stack.pop()
    return not temp_stack
print(validate_brackets("()"))        
print(validate_brackets("([)]"))       
print(validate_brackets("[{()}]"))     
print(validate_brackets(""))           
print(validate_brackets("{[}"))
