#Python Conditions and If statements

a=33
b=200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
#Output: b is greater than a


if a>b: print("a is greater than b")
#Output: a is greater than b

print("A") if a > b else print("B")
#Output: A

print("A") if a > b else print("=") if a == b else print("B")
#Output: A

c = 500

if a > b and c > a:
    print("Both conditions are True")
#Output: Both conditions are True

if a > b or a > c:
    print("At least one of the conditions is True") 
#Output: At least one of the conditions is True

if not(a > b):
    print("a is NOT greater than b")
#Output: a is NOT greater than b

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
#Output: Above ten, and also above 20!

a = 33
b = 200

if b > a:
    pass  # Do nothing
