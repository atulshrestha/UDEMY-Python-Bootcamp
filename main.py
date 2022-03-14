#from replit import clear
import random

from hangman_word import word_list

from hangman_art import title, stages

print(title)

selected_word = random.choice(word_list)
print(f'Psst, the solution is {selected_word}')
word_length = len(selected_word)

end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"
# print(display)


while not end_of_game:
    user_guess = input("enter a letter: ").lower()

    clear()

    if user_guess in display:
        print(f"You have already guessed {user_guess}")

    for position in range(word_length):
        letter = selected_word[position]
        # print(f"Current position: {position} \n Current letter: {letter}\n Guessed letter: {user_guess}")
        if letter == user_guess:
            display[position] = letter

    if user_guess not in selected_word:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!!")

    print(stages[lives])


