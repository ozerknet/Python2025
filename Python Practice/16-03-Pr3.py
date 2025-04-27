list = [1, 2, 3, 4, 5]
def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
print(sum_list(list))
# The code defines a list of integers and a recursive function `sum_list` that calculates the sum of the elements in the list.



z = 4

if z % 2 == 0:
    print("even")
else:
    print("odd")    
# The code checks if the variable `z` is even or odd and prints the result.


def is_even(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even(n - 2) 
  
print(is_even(4))

def is_odd(n):
    if n == 0:
        return False
    elif n == 1:
        return True
    else:
        return is_odd(n - 2)
