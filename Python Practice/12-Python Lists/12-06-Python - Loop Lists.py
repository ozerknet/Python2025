thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)  # Output: apple banana cherry

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])  # Output: apple banana cherry

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])  # Output: apple banana cherry
    i += 1  # Output: apple banana cherry
# The above code demonstrates how to loop through a list in Python using different methods.

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]  # Output: apple banana cherry

