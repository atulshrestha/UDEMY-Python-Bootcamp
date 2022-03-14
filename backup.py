import random

stages = ['''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''

+---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ["ardvark","baboon","camel"]
selected_word = random.choice(word_list)
print(f"fffffs.. the random word is {selected_word}")


display = []
for letter in selected_word:
    display += "_"
print(display)

end_of_game = False
lives = 6
while not end_of_game:
    user_guess = input("Guess the letter .....  ").lower()
    for position in range(len(selected_word)):
        letter = selected_word[position]
        if letter == user_guess:
            display[position] = letter

    if user_guess not in selected_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose.")

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win !!!!!!")

    print(stages[lives])