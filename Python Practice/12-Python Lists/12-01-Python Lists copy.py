'''
There are four collection data types in the Python programming language:

List        is a collection which is            ordered and     changeable.                     Allows duplicate members.
Tuple       is a collection which is            ordered and     unchangeable.                   Allows duplicate members.
Set         is a collection which is            unordered,      unchangeable*, and unindexed.   No duplicate members.
Dictionary  is a collection which is            ordered** and   changeable.                     No duplicate members.


*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

'''

myList = [1, 2, 3, 4, 5]
print(myList)  # [1, 2, 3, 4, 5]
print(type(myList))  # <class 'list'>
print(len(myList))  # 5
print(myList[0])  # 1
print(myList[1])  # 2



# List Methods
# append()  Adds an element at the end of the list
# clear()  Removes all the elements from the list
# copy()  Returns a copy of the list
# count()  Returns the number of elements with the specified value
# extend()  Add the elements of a list (or any iterable), to the end of the current list
# index()  Returns the index of the first element with the specified value
# insert()  Adds an element at the specified position
# pop()  Removes the element at the specified position
# remove()  Removes the first item with the specified value
# reverse()  Reverses the order of the list
# sort()  Sorts the list

thislist = ["apple", "banana", "cherry", "apple"]

list1 = ["apple", "banana", "cherry", 1,2,3, True, False, 1.5, 2.5, 3.5]

print(list1)  # ['apple', 'banana', 'cherry', 1, 2, 3, True, False, 1.5, 2.5, 3.5]
print(type(list1))  # <class 'list'>
print(len(list1))  # 10
print(list1[6])  # True

print(type(list1()))  # <class 'list'>

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)  # ['apple', 'banana', 'cherry']
print(type(thislist))  # <class 'list'>
print(len(thislist))  # 3
print(thislist[0])  # apple

