# TODO 1: Randomly choose a word from the word_list
# TODO 2: Ask the user to guess a letter and assign their - - - - -
# TODO 3: Check if the letter the user guessed is one of the letters in the chosen word. Print if letter is present else don't
import random
from hangman_words import word_list
from hangman_art import stages

lives = 6
random_word = random.choice(word_list)
fill_letter = ""
word_length = len(random_word)
print(random_word)

for char in range(word_length):
    fill_letter += "- "
print(fill_letter)

correct_letters = []
game_over = False

while not game_over:
    display = ""
    print(f"**********| {lives} LIVES LEFT |**********")
    guess_letter = input("Guess a letter: ").lower()

    if guess_letter in correct_letters:
        print(f"You have already guessed {guess_letter}")

    for letter in random_word:
        if letter == guess_letter:
            display += letter
            correct_letters.append(guess_letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess_letter not in random_word:
        lives -= 1
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("**********| You Lose! |**********")

    if "_" not in display:
        game_over = True
        print("**********| You Win! |**********")

    print(stages[lives])