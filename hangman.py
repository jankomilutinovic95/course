import random
from words import words


def get_word():
    return (random.choice(words)).upper()


def hangman():
    word = get_word()
    guesses = ''
    attempts = 10
    correctletters = 0
    guessedletters = []

    while True:

        # print guessed letters in a word
        for char in word:
            if char in guesses:
                print(f"{char}", end="")
            else:
                print("_", end="")
        print("\t")

        print(f"You have {attempts} guesses left")

        # list all guessed letters
        if len(guessedletters) != 0:
            print("Letters guessed: ", end='')
            print(", ".join(guessedletters))
        guess = input("Guess a character: ").upper()

        # check for multiple or no char entry
        if len(guess) > 1:
            print("Enter only one character!")
            print("\n")
            continue
        elif guess == '':
            print("Enter a character!")
            print("\n")
            continue

        # check for duplicate char entries
        if guess not in guessedletters:
            guessedletters.append(guess)
        else:
            print("You already guessed that letter")
            continue

        if guess in word:
            print("Correct!")
            print("\t")
            guesses += guess
            correctletters += 1
        else:
            print("Wrong letter!")
            print("\t")
            attempts -= 1

        # game over conditions
        if attempts == 0:
            print(f"Sorry you used up all your attempts! The correct word is {word}.")
            break
        elif correctletters == len(word):
            print(word)
            print("Bravo legendice!")
            break


hangman()
