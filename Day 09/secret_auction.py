#clear terminal
"""import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')"""

from art import logo
print(logo)

bids = {}
end = False

def highest(record):
    highest_bid = 0
    winner = ""

    for bidder in record:
        bid_amount = record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is '{winner}' with a bid of '${highest_bid}'")


while not end:
    name = input("What is your name ? \n")
    bid = int(input("What is your bid ? \n$"))

    bids[name] = bid
    again = input("Are there any other bidders ? Yes / No \n").lower()
    if again == "no":
        end = True
        highest(bids)
    #elif again == "yes":
       #clear()


