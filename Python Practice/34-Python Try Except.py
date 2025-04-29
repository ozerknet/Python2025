import practicemodule

try:
    print(x)
except:
    print("An exception occurred")

practicemodule.drawline()

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
practicemodule.drawline()
  
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
practicemodule.drawline()
 
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")  
  
practicemodule.drawline()

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  
practicemodule.drawline()


x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")


practicemodule.drawline()

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")