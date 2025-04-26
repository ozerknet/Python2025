thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)  # Output: ['apple', 'blackcurrant', 'cherry']
print(thislist[1:2]) # Output: ['blackcurrant']


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# Output: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
print(thislist[1:3]) # Output: ['blackcurrant', 'watermelon']

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)  # Output: ['apple', 'watermelon']
print(thislist[1:3]) # Output: ['watermelon']

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "watermelon")
print(thislist)  # Output: ['apple', 'watermelon', 'banana', 'cherry']

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])  # Output: 'banana'
print(mylist)  # Output: ['kiwi', 'banana', 'cherry']


mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])  
# Output: 'mango'
print(mylist)  # Output: ['apple', 'kiwi', 'mango', 'cherry']