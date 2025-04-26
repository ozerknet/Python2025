#Join Two Lists

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = list1 + list2
print(list3) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list1 = [ "quick", "brown", "fox"]
list2 = [ 1,2,3,4,5]
for x in list2:
    list1.append(x)
print(list1) # ['quick', 'brown', 'fox', 1, 2, 3, 4, 5]

models = [ "bmw", "audi", "mercedes"]
years = [ 2000, 2001, 2002]

models.extend(years)
print(models) # ['bmw', 'audi', 'mercedes', 2000, 2001, 2002]
#Output: ['bmw', 'audi', 'mercedes', 2000, 2001, 2002]
