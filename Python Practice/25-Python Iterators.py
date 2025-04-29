mytuple = ("apple", "banana","cherry")

myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

str = "apple"

myit_str = iter(str)

print(next(myit_str))
print(next(myit_str))
print(next(myit_str))
print(next(myit_str))


my_fruits = ("apple","cherry","banana","blubery","watermelon")

for fruit in my_fruits:
    print(fruit)
    
mystr = "banana"

for x in mystr:
  print(x)


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

