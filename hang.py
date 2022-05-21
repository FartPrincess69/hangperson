import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import random
end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
display=["_"] * len(chosen_word)
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if '_' in display:
      for ind, letter in enumerate(chosen_word):
        if letter in guess:
          display[ind] = letter
      print(*display)
    if not '_' in display:
        print("You win!")
    if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        end_of_game=True
        print("you lose")
    print(stages[lives])
