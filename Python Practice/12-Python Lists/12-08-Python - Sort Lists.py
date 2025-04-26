#Sort List Alphanumerically
thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.sort()
print(thislist)
#Output: ['Kiwi', 'Orange', 'banana', 'cherry']

thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.sort(reverse = True)
print(thislist)
#Output: ['kiwi', 'orange', 'banana', 'cherry']


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#Output: [23, 50, 65, 82, 100]

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#Output: [100, 82, 65, 50, 23]
#Sort List Descending


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = [ "banana", "Orange", "Kiwi", "cherry" ]
thislist.sort(key = str.lower)  
print(thislist)
#Output: ['banana', 'cherry', 'Kiwi', 'Orange']

thislist.reverse()
print(thislist)
#Output: ['Orange', 'Kiwi', 'cherry', 'banana']