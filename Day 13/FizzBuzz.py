print(""" ______ _         ____                
|  ____(_)       |  _ \               
| |__   _ _______| |_) |_   _ ________
|  __| | |_  /_  /  _ <| | | |_  /_  /
| |    | |/ / / /| |_) | |_| |/ / / / 
|_|    |_/___/___|____/ \__,_/___/___|""")
num = int(input("Sayı Giriniz.\n"))

for FizzBuzz in range(1, num +1):
    if FizzBuzz % 3 == 0 and FizzBuzz % 5 ==0:
        print("'FizzBuzz'")
    elif FizzBuzz % 3 == 0:
        print("'Fizz'")
    elif FizzBuzz % 5 == 0:
        print("'Buzz'")
    else:
        print(FizzBuzz)