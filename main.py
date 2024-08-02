#!/usr/bin/env python3

import random

def display_hangman(attempts):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |
        ---------
        """,
        """
           ------
           |    |
           |    
           |    
           |    
           |
        ---------
        """
    ]
    return stages[attempts]

def hangman():
    words = ["python", "java", "kotlin", "javascript"]
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(display_hangman(attempts))
        print(" ".join(guessed_word))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            for idx, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[idx] = guess
            if "_" not in guessed_word:
                print(display_hangman(attempts))
                print(" ".join(guessed_word))
                print("Congratulations! You've guessed the word.")
                break
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")

    if "_" in guessed_word:
        print(display_hangman(attempts))
        print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()
