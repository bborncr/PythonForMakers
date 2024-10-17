# conditionals.py
# Conditionals (making decisions)
the_light_is_on = True

if the_light_is_on:
    print("The light is on")
else:
    print("The light is off")
    
if the_light_is_on == True:
    print("The light is on")
else:
    print("The light is off")
    
temperature = 30.0

if temperature <= 25.0:
    # this is the cold section
    print("It's too cold!")
elif temperature > 25.0 and temperature <= 27.0:
    print("It's getting warm!")
elif temperature > 27.0:
    print("It's getting hot!")
print("done")