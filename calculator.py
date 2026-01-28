def calculator(a, b, operator='add'):
    if operator == 'add':
        return a + b 
    elif operator == 'subtract':
        return a - b 
    else:
        raise Exception('invalid operator, use add or subtract')