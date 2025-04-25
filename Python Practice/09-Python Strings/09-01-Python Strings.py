print("Mike")

name = "John"
print(name)

paragraph = """Hey Mike, How are you,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(paragraph)

#Strings are Arrays

name = "Mike"

print(name[0]) # [0] mean M

#Looping Through a String

for x in name:
    print(x)


#String Length

print(len(name))

#Check String
txt = "The best things in life are free!"
#print("free" in txt)

if "free" in txt:
    global status 
    status = True
    #print("Yes, 'free' is present")

print(status)


txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")