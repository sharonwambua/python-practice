# factorial_loop.py

def factorial_loop(n):
    """
    This function computes the factorial of a number using a loop.
    """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(factorial_loop(5))  
