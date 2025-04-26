#Adding Items

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,     
}

thisdict["color"] = "red" # add item
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

thisdict.update({"color": "blue"}) # update item
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'blue'}


thisdict["Made in"] = "UK" # add item
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'blue', 'Made in': 'UK'}  
