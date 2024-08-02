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

def load_words():
    # Add more words to make the game more challenging
    words = [
        "python", "java", "kotlin", "javascript", "hangman", "programming", "developer",
        "algorithm", "function", "variable", "constant", "dictionary", "tuple", "list",
        "comprehension", "iterator", "generator", "expression", "exception", "module"
    ]
    return words

def get_hint(word, guessed_letters):
    # Provide a hint by revealing one of the letters not yet guessed
    available_letters = [letter for letter in word if letter not in guessed_letters]
    if available_letters:
        return random.choice(available_letters)
    return ""

def hangman():
    words = load_words()
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)
    attempts = 6
    guessed_letters = set()
    incorrect_guesses = []

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(display_hangman(attempts))
        print("Guessed word: " + " ".join(guessed_word))
        print("Incorrect guesses: " + ", ".join(incorrect_guesses))
        
        if attempts <= 2:
            hint = get_hint(word_to_guess, guessed_letters)
            if hint:
                print(f"Hint: The word contains the letter '{hint}'")

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter. Try again.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            for idx, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[idx] = guess
            if "_" not in guessed_word:
                print(display_hangman(attempts))
                print("Guessed word: " + " ".join(guessed_word))
                print("Congratulations! You've guessed the word.")
                break
        else:
            guessed_letters.add(guess)
            incorrect_guesses.append(guess)
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")

    if "_" in guessed_word:
        print(display_hangman(attempts))
        print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()
