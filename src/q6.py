def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
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
task_2p1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(task_2p1)
# - [2, 10, 7, 0]
task_2p2 = find_first_negative([2, 10, 7, 0])
print(task_2p2)
