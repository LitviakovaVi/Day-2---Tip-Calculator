#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
number_tip = input("How much tip would you like to give? 10, 12, or 15? ")
number_people = input("How many people to split the bill? ")
tip = 1 + int(number_tip) / 100
total_tip = int(total_bill) / int(number_people)*tip
new_tip = "{:.2f}".format(total_tip)
print(f"Each person should pay: ${new_tip}")