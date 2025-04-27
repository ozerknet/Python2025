fruits = ['apples', 'oranges', 'bananas', 'grapes']

for fruit in fruits:
    print(fruit)
    
for i in "Mike":
    print(i)
    
fruits = ['apples', 'oranges', 'bananas', 'grapes']
for fruit in fruits:
    print(fruit)
    if fruit == 'bananas':
        break

fruits = ['apples', 'oranges', 'bananas', 'grapes']
for fruit in fruits:
    print(fruit)
    if fruit == 'bananas':
        continue
    print("This will not be printed")

print("Loop ended") 
    
for x in range(6):
    print(x)
  
print("Loop ended")
    
for x in range(2, 6):
    print(x)
    
print("Loop ended")

for x in range(2, 30, 3):
    print(x)    
    
print("Loop ended")

for x in range(6):
    print(x)    
else:
    print("Finally finished")
    
    
print("Loop ended")

for x in range(6):
    if x == 3: break
    print(x)
else:
  print("Finally finished!")
  
print("Loop ended")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
        
print("Loop ended")

for x in [0, 1, 2]:
    pass