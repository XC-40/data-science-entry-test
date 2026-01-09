def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Ensure dct is a dictionary
    if not isinstance(dct, dict):
        return -1

    # If key exists, print original value
    if key in dct:
        print("Original value for key '{}': {}".format(key, dct[key]))

    # Update dictionary with new value
    dct[key] = value

    return dct



# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"

result1 = update_dictionary({}, "name", "Alice")
print("Task 2 #1:", result1)
#Task 2 #1: {'name': 'Alice'}

# - {"age": 25}, "age", 26

result2 = update_dictionary({"age": 25}, "age", 26)
print("Task 2 #2:", result2)
#Original value for key 'age': 25
#Task 2 #2: {'age': 26}
