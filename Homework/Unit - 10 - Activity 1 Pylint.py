def factorial (x)
    if x == 1:
        return 1

    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num)) 



#Pylint identified the following error:
"""
************* Module Unit10
Unit10.py:1:18: E0001: Parsing failed: 'expected ':' (<unknown>, line 1)' (syntax-error)
"""