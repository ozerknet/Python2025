thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "electric": False,  
    }

for x in thisdict:
    print(x) # thisdict.keys() #Output: ['brand', 'model', 'year']

for x in thisdict.values():
  print(x)
# thisdict.values() #Output: ['Ford', 'Mustang', 1964, False]for x in thisdict.values():


for x in thisdict.keys():
  print(x)
# thisdict.keys() #Output: ['brand', 'model', 'year', 'electric']

for x, y in thisdict.items():
  print(x, y)