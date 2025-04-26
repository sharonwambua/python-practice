# even_or_odd.py

def check_even_odd(number):
    """
    This function checks if a number is even or odd.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
print(check_even_odd(10))  # Output: Even
print(check_even_odd(7))   # Output: Odd
