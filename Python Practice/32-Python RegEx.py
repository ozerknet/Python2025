import re

txt = txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES We have a match")
else:
    print ("No match")
    
'''

RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string


'''

#The findall() Function
txt = "The rain in Spain"
x = re.findall("i", txt)
print(x)


txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

#The search() Function
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

#The split() Function
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#The sub() Function
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

#Match Object
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())