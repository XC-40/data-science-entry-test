def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Ensure both num and divisor are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return -1
    
    # Avoid division by zero
    if divisor == 0:
        return -1
    
    # Check divisibility
    return num % divisor == 0

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2

result1 = check_divisibility(10, 2)
print("Task2 #1:", result1)
#Task2 #1: True

# - 7, 3

result2 = check_divisibility(7, 3)
print("Task2 #2:", result2)
#Task2 #2: False
