def calculator(a, b, operator='add'):
    if operator == 'add':
        return a + b 
    elif operator == 'subtract':
        return a - b 
    elif operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return a / b
    else:
        raise Exception('invalid operator, use add, subtract, multiply, or divide')
