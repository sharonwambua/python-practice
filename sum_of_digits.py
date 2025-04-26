# sum_of_digits.py

def sum_of_digits(number):
    """
    This function sums the digits of a given number.
    """
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total


print(sum_of_digits(1234))  
