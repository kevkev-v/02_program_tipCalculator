# Program: Tip Calculator 
# Description: To obtain the tip amount that will be paid by each person 

print("<<< WELCOME TO THE TIP CALCULATOR >>>")
totalBill = input("What was the total bill? $")
tipPercentage = input("What percentage tip would you like to give? (Only type the number): ")
numPeople = input("How many people to split the bill? ")

# Formulas
totalTip = (float(totalBill) * float(tipPercentage)) / 100
finalResult = float(totalTip) / float(numPeople)

#Output
print("\nEach person will have to pay $" + str(round(finalResult , 2)))