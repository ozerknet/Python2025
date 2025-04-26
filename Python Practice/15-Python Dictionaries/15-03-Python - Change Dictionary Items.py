thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,           
}

thisdict["year"] = 2020 # change value

print(thisdict) # {'brand': 'Ford', 'model': 'Mustang',

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
