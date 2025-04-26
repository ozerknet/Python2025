fruits = ("apple", "banana", "cherry")
# unpacking a tuple
(green, yellow, red) = fruits
print(green) # apple
print(yellow) # banana  
print(red) # cherry


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)