def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if s is a string
    if not isinstance(s, str):
        return -1
    
    # Reverse the string
    return s[::-1]



# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
result1 = string_reverse("Hello World")
print("Task 2 #1:", result1)

# - "Python"
result2 = string_reverse("Python")
print("Task 2 #2:", result2)
