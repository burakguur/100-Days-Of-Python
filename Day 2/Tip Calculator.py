print("****Calculating the tip to be paid per person.*****")

bill =float(input("What is the total account amount? $" ))
tip = int(input("How much tip would you like  to give ? %10, %12, %15 "))
people = int(input("How many people are there in total? "))


tipPercent = tip / 100
bill_with_tip = (bill * tipPercent) + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person)

print(f"Each person should pay : ${final_amount}")


