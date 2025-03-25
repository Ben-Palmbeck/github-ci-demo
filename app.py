def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division durch Null ist nicht erlaubt.")
    return a / b
