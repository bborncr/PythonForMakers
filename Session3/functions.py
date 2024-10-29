# functions.py

# a = 1
# b = 2
# c = a + b
# 
# print(c)

# define function
def adder1():
    a = 1
    b = 2
    c = a + b
    print(c)
    
adder1()
    
# function with parameters
def adder2(a, b):
    c = a + b
    print(c)
    
adder2(2, 3)

# function with parameters and return value
def adder3(a, b):
    c = a + b
    return c

adder3(3,4)
total = adder3(5, 6)
print(total)
    