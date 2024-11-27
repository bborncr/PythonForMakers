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

    if guess in guessed:
        print(f"You already guessed `{guess}`")
        continue
    guessed.add(guess)
    for i in range(word_length):
        if word[i] == guess:
            show_word[i] = guess
    if "-" not in show_word:
        print("You won!")
        break
    tries = tries - 1
    if tries < 1:
        print("Too many tries! You lose!")
        break  