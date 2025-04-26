myset = {1, 2, 3, 4, 5}
print(myset) # {1, 2, 3, 4, 5}

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # {'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", True, 1, 2} # True is equal to 1    

print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0} # False is equal to 0

print(thisset)

print(len(thisset)) # 5

print(type(thisset)) # <class 'set'>

set1_str = {"apple", "banana", "cherry"}
set2_int = {1, 2, 3}
set3_float = {1.1, 2.2, 3.3}
set4_bool = {True, False}
set5_none = {None}
set6_mixed = {"apple", 1, 2.2, True, None}
set7_empty = set() # empty set
set8_mixed = {1, 2, 3, "apple", True, None} # mixed set with different data types
set9_nested = {1, 2, 3, (4, 5), {6, 7}} # nested set with a tuple and a set
set10_frozenset = {1, 2, 3, frozenset({4, 5})} # set with a frozenset
set11_frozenset = frozenset({1, 2, 3, 4, 5}) # frozenset

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) # {'banana', 'cherry', 'apple'}

