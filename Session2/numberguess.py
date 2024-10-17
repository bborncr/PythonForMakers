import random

gameover = False

choice = random.randint(1, 10)
print(choice)

print("I am thinking of a number from 1 to 10. ")
print()

tries = 3

while gameover == False:
    guess = int(input("What is your guess? "))
    if guess == choice:
        print("You are right!")
        gameover = True
    else:
        print("Wrong! Try again!")
        tries = tries - 1
        if tries == 0:
            gameover = True
            print(f"Too many tries. You lose! The number was {choice}.")
    
print("Game Over!!")