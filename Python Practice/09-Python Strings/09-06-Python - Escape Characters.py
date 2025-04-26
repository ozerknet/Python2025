 # wrong txt = "We are the so-called "Vikings" from the north."
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = 'It\'s alright.'
print(txt) 

txt = "This will insert one \\ (backslash)."
print(txt) 

txt = "Hello\nWorld!" # \n is a newline character
print(txt)

txt = "Hello\tWorld!" # \t is a tab character
print(txt)

txt = "Hello\rWorld!" # \r is a carriage return character
print(txt)


txt = "Hello\bWorld!" # \b is a backspace character
print(txt)

txt = "Hello\tWorld!"
print(txt) # \t is a tab character

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) # \110 is H, \145 is e, \154 is l, \154 is l, \157 is o
#A backslash followed by an x and a hex number results in a hex value:

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 