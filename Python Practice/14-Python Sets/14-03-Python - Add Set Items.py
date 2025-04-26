thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print(thisset) # {'banana', 'cherry', 'orange', 'apple'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) # {'banana', 'cherry', 'mango', 'apple', 'papaya', 'pineapple'}

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) # {'banana', 'cherry', 'kiwi', 'orange', 'apple'}


fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits) # {'banana', 'cherry', 'kiwi', 'orange', 'apple'}