thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#Output: ['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
#Output: ['apple', 'banana', 'cherry']


thislist = ["apple", "banana", "cherry"]
otherlist = thislist[:]
print(otherlist)
#Output: ['apple', 'banana', 'cherry']