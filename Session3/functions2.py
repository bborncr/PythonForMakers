# functions2.py

# define function
def adder1():
    a = 1
    b = 2
    c = a + b
    print(c)
    
# function with parameters
def adder2(a, b):
    c = a + b
    print(c)

# function with parameters and return value
def adder3(a, b):
    c = a + b
    return c

def main():
    adder1()
    adder2(3,4)
    print(adder3(4,5))    

if __name__ == "__main__":
    main()
    