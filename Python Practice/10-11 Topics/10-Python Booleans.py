print(5>2)
print(5<2)
print(5==2)
print(5!=2)


a = 200
b = 33
if a > b:
    print("a is greater than b")    
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")  


print(bool(5)) # True
print(bool("Hello")) # True
print(bool(0)) # False


bool(False) # False
bool(None) # False
bool(0) # False
bool("") # False
bool(()) # False
bool([]) # False
bool({}) # False
bool(set()) # False
bool(range(0)) # False  
bool(True) # True
bool(1) # True
bool("Hello") # True
bool((1, 2)) # True
bool([1, 2]) # True


class myclass:
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj)) # False


def my_function() : 
    return True
print(my_function()) # True
print(bool(my_function())) # True


def my_function() :
    return True

if my_function() :
    print("YES!")
else:
    print("NO!")
# Output: YES!

x = 200
print(isinstance(x, int)) # True
print(isinstance(x, str)) # False   
print(isinstance(x, float)) # False
print(isinstance(x, bool)) # False
print(isinstance(x, list)) # False
print(isinstance(x, tuple)) # False