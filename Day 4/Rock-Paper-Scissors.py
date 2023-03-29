import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)______
          ________)
          _________)
         _________)
---.____________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
ascii = (rock, paper, scissors)

user = int(input("What do you choose? Type 0 for Rock , Type 1 for Paper, Type 2 for Scissors : \n"))
computer = random.randint(0,2)

print("Your Choose: ", user)
print(ascii[user])

print("Computer Choose: ", computer)
print(ascii[computer])


if user < 0 or user > 2:
    print("You typed an invalid number, you lose!")
elif user == 0 and computer == 2:
    print("You win!!")
elif computer == 0 and user == 2:
    print("Computer win , You Lose :(")
elif user > computer:
    print("You Win !")
elif computer > user:
    print("Computer Win. You Lose :( ")
else:
    print("Draw")
