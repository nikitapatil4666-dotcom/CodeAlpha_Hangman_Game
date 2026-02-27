# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 20:12:35 2026

@author: Nikita Patil
"""

import random

# Step 1: Create a list of 5 predefined words
word_list = ["apple", "tiger", "table", "mango", "chair"]

# Step 2: Randomly choose a word from the list
secret_word = random.choice(word_list)

# Step 3: Create display with underscores
display = ["_"] * len(secret_word)

# Step 4: Set number of attempts
attempts = 6

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect attempts.\n")

# Step 5: Start the game loop
while attempts > 0 and "_" in display:
    
    print("Word:", " ".join(display))
    guess = input("Enter a letter: ").lower()
    
    # Check if letter is already guessed
    if guess in display:
        print("You already guessed that letter.\n")
        continue
    
    # Step 6: Check if guessed letter is in the word
    if guess in secret_word:
        print("Correct Guess!\n")
        
        # Replace underscores with correct letter
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Attempts left:", attempts, "\n")

# Step 7: Final Result
if "_" not in display:
    print("Congratulations! You Won!")
    print("The word was:", secret_word)
else:
    print("Game Over! You Lost!")
    print("The word was:", secret_word)