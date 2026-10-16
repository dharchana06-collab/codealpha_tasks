
import random

words = ["python", "apple", "school", "phone", "table"]
word = random.choice(words)
guessed = []
wrong = 0

print("Welcome to Hangman")

while wrong < 6:
    display = ""
    for letter in word:
        if letter in guessed:
            display = display + letter + " "
        else:
            display = display + "_ "
    print(display)

    if "_" not in display:
        print("You won! The word is", word)
        break

    guess = input("Enter a letter: ").lower()    

    if guess in guessed:
        print("You already guessed that")
    elif guess in word:
        guessed.append(guess)
        print("Correct")
    else:
        guessed.append(guess)
        wrong = wrong + 1
        print("Wrong. Chances left:", 6 - wrong)

if wrong == 6:
    print("You lost. The word was", word)
