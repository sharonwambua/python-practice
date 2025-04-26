# reverse_string.py

def reverse_string(s):
    """
    This function reverses a string without using [::-1] or built-in reversed().
    """
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s


print(reverse_string("hello"))  
