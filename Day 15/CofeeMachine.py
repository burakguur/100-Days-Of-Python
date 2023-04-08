from art import logo
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {"water": 300,
             "milk": 200,
             "coffee":100,}

#Returns True when order can be made, False if ingredients are insufficient.
#Siparişler yapılabiliyorsa True, malzeme eksikse False döndürür.
def resources_suffiecient(order_ingredients):
    for item in (order_ingredients):
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True

#Return the total calculated from coins inserted
#Toplam madeni paraları döndürür
def coins():

    print("Please insert coins.")
    total = int(input("How many quarters?:  ")) * 0.25
    total += int(input("How many dimes?:  ")) * 0.1
    total += int(input("How many nickles?:  ")) * 0.05
    total += int(input("How many pennies?:  ")) * 0.01
    return total

#Return True when the payment is accepted, or False if money is insufficient.
#Ödeme başarılıysa True, para yetersizse False döndürür.
def process(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that not enough money. Money refunded.")
        return False

def coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True

while is_on:
    print(logo)
    choice = input("What would you like? espresso/latte/cappuccino\n")
    if choice == "off":
        is_on = False
        print("GoodByee!..")
    elif choice == "report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']} g")
        print(f"Money:${profit} ")
    else:
        drink = MENU[choice]
        if resources_suffiecient(drink["ingredients"]):
            payment = coins()
            if  process(payment, drink["cost"]):
                coffee(choice, drink["ingredients"])
