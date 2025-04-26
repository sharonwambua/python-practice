# sum_list.py

def sum_list(numbers):
    """
    This function takes a list of numbers and returns their sum.
    """
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15
