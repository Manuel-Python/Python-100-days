print("Welcome to the tip calculator\n") #
bill = input("What was the total bill? $") #124.54
people = input("How many people to split the bill? ") #5
tip_percent = input("What pecentage tip would you like to give? 10, 12, or 15? ") #12

total_bill = (float(bill) + (float(bill) * (float(tip_percent)*0.01)))

print("Each person should pay: ${:0.2f}".format(total_bill/float(people))) #$27.9
