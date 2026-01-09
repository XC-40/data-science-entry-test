def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Check if lst is a list 
    if not isinstance(lst, list):
        return -1

    # Replace all occurrences of find_val with replace_val 
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst



# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5

result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print("Task 2 #1:", result1)
#Task 2 #1: [1, 5, 3, 4, 5, 5]

# - ["apple", "banana", "apple"], "apple", "orange"

result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print("Task 2 #2:", result2)
#Task 2 #2: ['orange', 'banana', 'orange']
