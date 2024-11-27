# hangman.py
import random

words = ["lion", "tiger", "puma", "bobcat", "cougar"]

word = random.choice(words)
word_length = len(word)
guessed = set()
tries = word_length + 2
show_word = list("-" * word_length)

print("Welcome to Hangman")

while True:
    print("".join(show_word))
    guess = input("Guess a letter: ")

    # check if previously guessed
    if guess in guessed:
        print(f"You already guessed `{guess}`")
        continue
    guessed.add(guess)
    
    # if the guess is equal to the letter replace the "-" with the letter
    for i in range(word_length):
        if word[i] == guess:
            show_word[i] = guess
    
    # check for win condition        
    if "-" not in show_word:
        print("You won!")
        break
    
    # too many tries
    tries = tries - 1
    if tries < 1:
        print("Too many tries! You lose!")
        break  