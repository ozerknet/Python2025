#Python - List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist =[]
for x in fruits:
    if "a" in x:
        newlist.append(x)   
print(newlist)
#Output: ['banana', 'mango']


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]   
print(newlist)
#Output: ['banana', 'mango']
print(fruits)

newlist = [x for x in fruits if x != "apple"]
print(newlist)
#Output: ['banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in range(10)]
print(newlist)
#Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

newlist = [x for x in range(10) if x < 5]
print(newlist)
#Output: [0, 1, 2, 3, 4]

newlist = [x.upper() for x in fruits]
print(newlist)
#Output: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

newlist = ['hello' for x in fruits]
print(newlist)
#Output: ['hello', 'hello', 'hello', 'hello', 'hello']

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
#Output: ['apple', 'orange', 'cherry', 'kiwi', 'mango']