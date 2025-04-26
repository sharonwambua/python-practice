# factorial_recursive.py

def factorial_recursive(n):
    """
    This function computes factorial of a number using recursion.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)


print(factorial_recursive(5))  
