# List and Set member check with if

# Example list and set
example_list = [1, 2, 3, 4, 5]
example_set = {10, 20, 30, 40, 50}

# Check if an element exists in the list
element_to_check_list = 3
if element_to_check_list in example_list:
    print(f"{element_to_check_list} is in the list.")
else:
    print(f"{element_to_check_list} is not in the list.")

# Check if an element exists in the set
element_to_check_set = 25
if element_to_check_set in example_set:
    print(f"{element_to_check_set} is in the set.")
else:
    print(f"{element_to_check_set} is not in the set.")

