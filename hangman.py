"""
=========================================================
Project: Hangman Game 🎮
Internship: CodeAlpha Python Programming Internship
Task: 1 - Hangman Game
Author: [Your Name]
Date: [Today's Date]

Description:
------------
This is a simple text-based Hangman game where:
- The player guesses a hidden word letter by letter.
- The game randomly chooses a word from a predefined list.
- The player has 6 chances to make wrong guesses.
- The game ends when the word is guessed or attempts run out.

Key Concepts Used:
------------------
- random module
- while loop
- if-else conditions
- string & list operations
- input/output handling

=========================================================
"""

import random

def get_random_word():
    
    words = ["python", "hangman", "program", "internship", "project"]
    return random.choice(words)

def display_progress(word, guessed_letters):
   
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    
    word = get_random_word()
    guessed_letters = []
    attempts = 6

    print("===================================")
    print("        Welcome to Hangman        ")
    print("===================================")
    print("Rules: You have 6 chances to guess the word.\n")

    while attempts > 0:
        
        print("Word:", display_progress(word, guessed_letters))

        
        if all(letter in guessed_letters for letter in word):
            print("\n Congratulations! You guessed the word:", word)
            break

        
        guess = input(" Enter a letter: ").lower()

        
        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single alphabet letter.")
            continue
        if guess in guessed_letters:
            print(" You already guessed this letter.")
            continue

        
        guessed_letters.append(guess)
        if guess in word:
            print(" Good guess!\n")
        else:
            attempts -= 1
            print(f" Wrong guess! Remaining attempts: {attempts}\n")

    
    if attempts == 0:
        print(" Game Over! The word was:", word)


if __name__ == "__main__":
    hangman()
