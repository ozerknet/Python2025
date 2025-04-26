set1 = {'a', 'b', 'c'}  # Create a set with some elements
set2 = {'d', 'e', 'f'}  # Create another set with some elements


set3 = set1.union(set2)  # Join sets using union() method  
print(set3)  # Output: {a, b, c, d, e, f}

set4 = set1 | set2  # Join sets using the | operator
print(set4)  # Output: {a, b, c, d, e, f}

myset = set1.union(set2,set3,set4)  # Join multiple sets using union() method
print(myset)  # Output: {a, b, c, d, e, f}

x = {'apple', 'banana', 'cherry'}
y = (1, 2, 3)

z = x.union(y)  # Join a set and a tuple using union() method
print(z)  # Output: {1, 2, 3, 'apple', 'banana', 'cherry'}

set1 = {'a', 'b', 'c'}
set2 = {1,2,3}

set1.update(set2)  # Join sets using update() method
print(set1)  # Output: {1, 2, 3, 'a', 'b', 'c'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)  # Join sets using intersection() method
print(set3)  # Output: {'apple'}

set3 = set1 & set2  # Join sets using the & operator
print(set3)  # Output: {'apple'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)  # Output: {'banana', 'cherry'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)  # Output: {'banana', 'cherry'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)  # Output: {'banana', 'cherry', 'google', 'microsoft'}

set3 = set1 ^ set2  # Join sets using the ^ operator
print(set3)  # Output: {'banana', 'cherry', 'google', 'microsoft'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)  # Output: {'banana', 'cherry', 'google', 'microsoft'}
