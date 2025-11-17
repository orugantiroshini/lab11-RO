import math

def square_root(a):
    try:
        math.sqrt(a)
    except ValueError:
        print("Invalid input")

def hypotenuse(a,b):
        math.hypot(a,b)

def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a * b

def divide(a, b):
    if a == 0: raise ZeroDivisionError
    else: return a / b

def logarithm(a, b):
    if a == 0: raise ValueError
    else: return math.log(b, a)

def exponent(a, b):
    return a**b



