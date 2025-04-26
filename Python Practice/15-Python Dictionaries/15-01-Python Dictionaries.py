thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

print(thisdict["brand"]) # Ford

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

print(len(thisdict))
# 3 

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
# {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

print(type(thisdict))
# <class 'dict'>

thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

