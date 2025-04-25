rate = "awesome"

def myfunc():
    rate = "fantastic"
    print ("Python is " + rate)

myfunc()

print ("Python is " + rate)

#The global Keyword

def otherfunc():
    global rate
    rate = "good"

otherfunc()

print("Python is " +  rate)