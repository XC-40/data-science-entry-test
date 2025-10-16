def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if not isinstance(dct, dict):
        return -1
    
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    
    dct[key] = value
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
task_2p1 = update_dictionary({}, "name", "Alice")
print(task_2p1)
# - {"age": 25}, "age", 26
task_2p2 = update_dictionary({"age": 25}, "age", 26)
print(task_2p2)
