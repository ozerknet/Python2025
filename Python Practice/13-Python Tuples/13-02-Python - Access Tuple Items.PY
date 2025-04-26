thistuple = ("apple", "banana", "cherry")
print(thistuple[0]) # apple

print(thistuple[-1]) # cherry
print(thistuple[1:]) # ('banana', 'cherry')
print(thistuple[:2]) # ('apple', 'banana')
print(thistuple[1:3]) # ('banana', 'cherry')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) # ('orange', 'kiwi', 'melon')
print(thistuple[-4:]) # ('orange', 'kiwi', 'melon', 'mango')

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
# Yes, 'apple' is in the fruits tuple
# Output: Yes, 'apple' is in the fruits tuple