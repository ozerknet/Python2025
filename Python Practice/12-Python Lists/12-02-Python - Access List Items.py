thislist = ["apple", "banana", "cherry"]
print(thislist[1])  # Output: banana

print(thislist[-1])  # Output: cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # Output: ['cherry', 'orange', 'kiwi']
print(thislist[:4])  # Output: ['apple', 'banana', 'cherry', 'orange']
print(thislist[2:])  # Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[-4:-1])  # Output: ['orange', 'kiwi', 'melon']
print(thislist[-1:])  # Output: ['mango']

print(thislist[1:5:2])  # Output: ['banana', 'orange']

print(thislist[::2])  # Output: ['apple', 'cherry', 'kiwi', 'mango']
print(thislist[::-1])  # Output: ['mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # Output: ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])  # Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
  print("No, 'apple' is not in the fruits list")        