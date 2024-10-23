# datatypes.py
# Basic data types: integers, floats, strings, booleans
# integer = whole number. count = 3
count = 3
print(count)
# Addition
count = count + 2
print(count)
# Multiplication
count = count * 2
print(count)
# Division returns a float!!!
count = count / 3
print(count)
# Floor Division returns an integer!!!
count = 10
count = count // 3
print(count)
# float = decimal number. temperature = 23.5
# string = String of characters. name = "Brad"
first_name = "John"
last_name = "Smith"
age = 25
# String concatenation
full_name = first_name + " " + last_name
print(full_name)
# f-strings (the best way to concatenate)
full_name = f"My name is {full_name}. I am {age} years old."
print(full_name)
# boolean = True or False
the_light_is_on = False
if the_light_is_on:
    print("The light is on")
    # this is the code block
else:
    print("The light is off")
        