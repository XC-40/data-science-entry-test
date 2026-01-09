def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if both x and y are numeric 
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))): 
        return -1 
        print("Swap values:", x, y) 
    return x, y

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

#1: "Apple", 10 
result1 = swap("Apple", 10) 
print("Task 2 #1:", result1) 

#2: -9, 17 
result2 = swap(-9, 17) 
print("Task 2 #2:", result2)
