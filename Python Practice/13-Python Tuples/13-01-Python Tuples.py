mytuple = ("apple", "banana", "cherry")
print(mytuple)
#Output: ('apple', 'banana', 'cherry')


thistuple = ("apple", "banana", "cherry", "apple", "wine", "cola")
print(thistuple)
#Output: ('apple', 'banana', 'cherry', 'apple', 'wine', 'cola')

print(len(thistuple)) # 6

thistuple = ("apple",)
print(type(thistuple)) # <class 'tuple'>

thistuple = ("apple")
print(type(thistuple)) # <class 'str'>
# To create a tuple with one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# This is known as a "singleton" tuple.
# A tuple can also be created without parentheses, but it is not recommended as it can lead to confusion.   

# For example:
# thistuple = "apple", "banana", "cherry"
# print(thistuple) # ('apple', 'banana', 'cherry')
# Output: ('apple', 'banana', 'cherry')

tuple1_str = ("apple", "banana", "cherry")
tuple2_int = (1, 2, 3)
tuple3_float = (1.1, 2.2, 3.3)
tuple4_bool = (True, False, True)
tuple5_mixed = ("apple", 1, 2.2, True)
tuple6_nested = (("apple", "banana"), (1, 2, 3), (1.1, 2.2, 3.3), (True, False, True))
tuple7_empty = ()
tuple8_singleton = ("apple",)
tuple9_singleton_no_comma = ("apple")
tuple10_singleton_no_parentheses = "apple", "banana", "cherry"


print(type(tuple1_str)) # <class 'tuple'>

thistuple = tuple(("apple", "banana", "cherry")) # note the double round brackets
print(thistuple) # ('apple', 'banana', 'cherry')
