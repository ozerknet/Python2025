#Upper Case
str1 = "hello world"
str2 = str1.upper()
print(str2) #HELLO WORLD

#Lower Case 
str1 = "HELLO WORLD"
str2 = str1.lower()
print(str2) #hello world

#Remove Whitespace
str1 = "   Hello World   "
str2 = str1.strip()
print(str2) #Hello World

#Replace String
str1 = "Hello World"
str2 = str1.replace("H", "J")
print(str2) #Jello World

#Split String
str1 = "Hello World"
str2 = str1.split(",")
print(str2) #['Hello World']

#Join String
str1 = "Hello World"
str2 = str1.split(",")
str3 = " ".join(str2)
print(str3) #Hello World

#Count String
str1 = "Hello World"    
str2 = str1.count("o")
print(str2) #2

#Find String
str1 = "Hello World"
str2 = str1.find("o")
print(str2) #4

#Index String
str1 = "Hello World"
str2 = str1.index("o")
print(str2) #4