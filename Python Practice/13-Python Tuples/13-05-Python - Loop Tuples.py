thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) # apple banana cherry

thistuple = ("apple", "banana", "cherry")
for x in range(len(thistuple)):
  print(thistuple[x]) # apple banana cherry

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1 # apple banana cherry
  