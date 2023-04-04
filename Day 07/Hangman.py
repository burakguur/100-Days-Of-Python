import random
from art import logo, stages
from words import word_list

print(logo)

word = random.choice(word_list)

display = ["_"] * len(word)

live = 5

while live > 0:

    guess = input("guess a letter: ").lower()


    for loc in range(len(display)):
        letter = word[loc]
        if letter == guess:
            display[loc] = letter

    print(" ".join(display))

    if guess not in word:
        live -= 1
        print(f"Wrong choice, you lost a live.\n{live}")

    if live == 0:
        print("You lose")

    print(stages[live])
