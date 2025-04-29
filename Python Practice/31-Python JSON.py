import json
import practicemodule 

x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"])

practicemodule.drawline()
#------------------------------------------------------


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)
print(y)

'''
When you convert from Python to JSON, 
Python objects are converted into 
the JSON (JavaScript) equivalent:

Python	JSON
dict	Object
list	Array
tuple	Array
str	    String
int	    Number
float	Number
True	true
False	false
None	null

'''
practicemodule.drawline()
#------------------------------------------------------
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
practicemodule.drawline()

print(json.dumps(x, indent=4))
practicemodule.drawline()

print(json.dumps(x, indent=4, separators=(". ", " = ")))
practicemodule.drawline()

print(json.dumps(x, indent=4, sort_keys=True))



