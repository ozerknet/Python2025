print(10+5) # 115
print(10-5) # 5

#Python Assignment Operators
x = 5

x+= 3 # x = x + 3
print(x) # 8
x-= 3 # x = x - 3   
print(x) # 5
x*= 3 # x = x * 3
print(x) # 15
x/= 3 # x = x / 3
print(x) # 5.0
x%= 3 # x = x % 3   
print(x) # 2.0
x//= 3 # x = x // 3
print(x) # 0.0
x**= 3 # x = x ** 3
print(x) # 0.0

# x&= 3 # x = x & 3
print(x) # 0.0

# x|= 3 # x = x | 3
print(x) # 3.0

# x^= 3 # x = x ^ 3
print(x) # 0.0

# x>>= 3 # x = x >> 3
print(x) # 0.0

#x<<= 3 # x = x << 3
print(x) # 0.0

#Python Comparison Operators
x = 5
y = 10
print(x == y) # False
print(x != y) # True
print(x > y) # False
print(x < y) # True
print(x >= y) # False
print(x <= y) # True
print(x is y) # False   
print(x is not y) # True
#print(x in y) # False
#print(x not in y) # True

#Python Bitwise Operators
x = 5 # 0101
y = 3 # 0011

print(x & y) # 1  (0001)
print(x | y) # 7  (0111)
print(x ^ y) # 6  (0110)
print(~x) # -6 (1010)
print(x << 2) # 20 (10100)
print(x >> 2) # 1 (0001)

#Operator Precedence
# 1. Parentheses
example = (10 + 5) * 2 # 30
print(example) # 30
# 2. Exponentiation
example = 2 ** 3 + 5 # 13
print(example) # 13
# 3. Multiplication, Division, Floor Division, Modulus
example = 10 * 5 + 2 # 52
print(example) # 52
# 4. Addition, Subtraction
example = 10 + 5 - 2 # 13
print(example) # 13
# 5. Bitwise Shift Operators
example = 10 << 2 # 40
print
# 6. Bitwise AND
example = 10 & 5 # 0    
print(example) # 0
# 7. Bitwise XOR
example = 10 ^ 5 # 15
print(example) # 15    
# 8. Bitwise OR
example = 10 | 5 # 15

# 9. Comparison Operators
# 10. Assignment Operators
# 11. Identity Operators
# 12. Membership Operators
# 13. Logical Operators
# 14. Conditional Operators
# 15. Lambda Operators
# 16. Ternary Operators
# 17. Comma Operators
# 18. Yield Operators
# 19. Await Operators
# 20. Async Operators
# 21. With Operators

