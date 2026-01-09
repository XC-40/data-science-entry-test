def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    # Ensure lst is a list
    if not isinstance(lst, list):
        return -1
    
    i = 0
    while i < len(lst):
        if isinstance(lst[i], (int, float)) and lst[i] < 0:
            return lst[i]
        i += 1
    
    return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print("Task 2 #1:", result1)
#Task2 #1: -1

# - [2, 10, 7, 0]
result2 = find_first_negative([2, 10, 7, 0])
print("Task 2 #2:", result2)
#Task 2 #2: No negatives
