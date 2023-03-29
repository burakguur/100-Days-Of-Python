import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PasswordGenerator")
let = int(input("How many letters would you like in your password?\n"))
num = int(input(f"How many numbers would you like?\n"))
sym = int(input("How many symbols would you like?\n"))

#Easy Version
"""password =""

for i in range(1,let +1):
    password += random.choice(letters)
for i in range(1,num +1):
    password += random.choice(numbers)
for i in range(1,sym +1):
    password += random.choice(symbols)
print(password)"""

#Hard Version
#Password List = passwordL
passwordL = []
for i in range(1,let +1):
    passwordL += random.choice(letters)
for i in range(1,num +1):
    passwordL += random.choice(numbers)
for i in range(1,sym +1):
    passwordL += random.choice(symbols)

#reorganize the order of the items.
random.shuffle(passwordL)

#pw = password
pw = ""
for i in passwordL:
    pw += i
print("Your password is: " + pw)

