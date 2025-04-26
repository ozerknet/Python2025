thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # Output: ['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  # Output: ['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop()  # Removes the last item
print(thislist)  # Output: ['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[0]  # Removes the first item
print(thislist)  # Output: ['banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist  # Deletes the entire list
# print(thislist)  # Raises NameError: name 'thislist' is not defined

thislist = ["apple", "banana", "cherry"]
thislist.clear()  # Empties the list
print(thislist)  # Output: []
