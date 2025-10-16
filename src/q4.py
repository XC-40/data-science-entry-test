def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        return -1
    
    return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
task_2p1 = string_reverse("Hello World")
print(task_2p1)
# - "Python"
task_2p2 = string_reverse("Python")
print(task_2p2)
