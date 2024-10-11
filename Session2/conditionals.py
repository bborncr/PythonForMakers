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
    
temperature = 28.5

if temperature <= 25:
    print("It's too cold!")
elif temperature > 25 and temperature <= 27:
    print("It's getting warm!")
elif temperature > 27:
    print("It's getting hot!")