#Copy a Dictionary

dict1 = {
    "name": "John",     # string    # key   value pair                      
    "age": 30,         # integer   # key   value pair
    "city": "New York" # string    # key   value pair   
}

mydict = dict1.copy() # copy the dictionary
print(mydict) # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydictx= dict(thisdict) # copy the dictionary
print(mydictx) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
