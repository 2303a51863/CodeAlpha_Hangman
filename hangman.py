# Created by Bhavya Reddy for CodeAlpha Internship - Task 1: Hangman Game
# Concepts Used: random, while loop, if-else, strings, lists

import random

# List of hidden mystery words (you can change later)
guess_bank = ['python', 'coding', 'planet', 'rocket', 'flower']
secret_word = random.choice(guess_bank)

display = ['_' for _ in secret_word]  # underscore for each letter
turns = 6
attempted_letters = []

print("🧠 Welcome to Mystery Word Challenge!")
print("🔍 Your word:", ' '.join(display))

while turns > 0 and '_' in display:
    letter = input("🔡 Type a letter: ").lower()

    if not letter.isalpha() or len(letter) != 1:
        print("⚠️ Enter only one alphabet character.")
        continue

    if letter in attempted_letters:
        print("❗ You already tried that one!")
        continue

    attempted_letters.append(letter)

    if letter in secret_word:
        print("✅ Good job!")
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                display[i] = letter
    else:
        print("❌ Nope, not in the word.")
        turns -= 1

    print("🔠 Current word:", ' '.join(display))
    print("❤️ Remaining lives:", turns)
    print("📝 Tried so far:", ', '.join(attempted_letters))
    print("-" * 30)

if '_' not in display:
    print("🎉 YOU WON! The word was:", secret_word)
else:
    print("😢 YOU LOST. The word was:", secret_word)
