# Simple Python Hangman program || ! problems known: duplicate letters do not show in turn 0, if guess is the entire alphabet you win game

from words import word_list
import random

word = random.choice(word_list)
guesses = ''
turns = 10
length = len(word)

print('Welcome to Hangman!\n')
print('Your word has', length, ' characters')
print("Start guessing...")
#print('debug: word = ', word)  # debug only!


while turns > 0:
    failed = 0
    print(word[0])
    for char in word[1:]:
        if char in guesses:
            print(char)

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You won")
        break

    guess = input("Your guess:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have %s more guesses" % turns)
        if turns == 0:
            print("You Lose")
