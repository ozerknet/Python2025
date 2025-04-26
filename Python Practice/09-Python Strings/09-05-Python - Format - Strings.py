age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# Example 1: Using format() method with multiple placeholders
quantity = 3
itemno = 567    
price = 49.95
myorder = " I want {} pieces of item {} for {} dollars." 
print(myorder.format(quantity, itemno, price))
# Example 2: Using format() method with named placeholders      

myorder = "I want to pay {price} dollars for {quantity} pieces of item {itemno}."
print(myorder.format(quantity = quantity, itemno = itemno, price = price))      

age = 36
txt = f"My name is John, and I am {age}"
print(txt)
# The f-string is a new and improved way to format strings in Python. It was introduced in Python 3.6 and is now the preferred way to format strings.
# The f-string is a more concise and readable way to format strings compared to the format() method. It allows you to embed expressions inside string literals, using curly braces {}.
# The expressions are evaluated at runtime and formatted using the format() method.
# Example 3: Using f-string with multiple placeholders  

quantity = 3
itemno = 567    
price = 49.95
myorder = f"I want {quantity} pieces of item {itemno} for {price} dollars."
print(myorder)
# Example 4: Using f-string with named placeholders
myorder = f"I want to pay {price} dollars for {quantity} pieces of item {itemno}."
print(myorder)
# Example 5: Using f-string with expressions
x = 5   
y = 10
z = x + y
myorder = f"The sum of {x} and {y} is {z}."
print(myorder)
# Example 6: Using f-string with functions
def add(x, y):
    return x + y

myorder = f"The sum of {x} and {y} is {add(x, y)}."
print(myorder)
