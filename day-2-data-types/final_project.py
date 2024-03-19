print("Welcome to the tip calculator!")

totalBill = float(input("What was the total bill? $"))
tip =  (totalBill * int(input("How much tip would you like to give? 10, 12, or 15? "))) / 100
totalPeople = int(input("How many people to split the bill? "))

payByPerson = round((totalBill + tip) / totalPeople, 2)

print(f"Each person should pay: ${payByPerson}")

