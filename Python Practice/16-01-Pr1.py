family1 = {
    "Man":[
        {
            "name": "Mike",
            "age": 30,  
        } 
    ],
    "Woman" : [
        {
            "name": "Sarah",
            "age": 30,  
        }
    ],
    "Marrried": True,
    "Married_year": 2015,
    "children": [
        {
            "name": "Henry",
            "age": 5,
            "gender": "Male",
            }       
    ]
}

family2 = {
    "Man":[
        {
            "name": "Jack",
            "age": 40,  
        } 
    ],
    "Woman" : [
        {
            "name": "Elly",
            "age": 37,  
        }
    ],
    "Marrried": True,
    "Married_year": 2015,
    "children": [
        {
            "name": "Lara",
            "age": 1,
            "gender" : "Female",
            }       
    ]
}

if family1["Marrried"] == True:
    print("Married")
else:
    print("Not married")



if family1["children"] == []:
    print("No children")
else:   
    print("Has children")
    for child in family1["children"]:
        print(f"Child name: {child['name']}, age: {child})")


print(f"Family1: {family1}")
print(f"Family2: {family2}")

list1 = [1, 2, 3, 4, 5]

tuple1 = (1, 2, 3, 4, 5)

set1 = {1, 2, 3, 4, 5}

dict1 = {
    "name": "Mike",
    "age": 30,
}


if list1 == tuple1:
    print("List and tuple are equal")
else:
    print("List and tuple are not equal")   

if list1 == set1:
    print("List and set are equal")     
else:
    print("List and set are not equal") 

