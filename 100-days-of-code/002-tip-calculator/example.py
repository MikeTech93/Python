### Challenge #1 - Prompt user for 2 digit number and then add the digits together
x = input("Please enter a two digit number:")
print(int(x[0]) + int(x[1]))

### Challenge #2 - BMI Calculator
h = float(input("Enter your height in m: "))
w = float(input("Enter your weight in kg: "))
bmi = int(w / (h**2))
print("Your BMI is " + str(bmi))

### Challenge #3 - Your Life in weeks - How many weeks left you have if you were to live to 90 years old
a = int(input("What is your current age in years: "))
yearsRemaining = 90 - a
daysRemaining = yearsRemaining * 365
weeksRemaining = yearsRemaining * 52
MonthsRemaining = yearsRemaining * 12
print(f"You have {daysRemaining} days, {weeksRemaining} weeks and {MonthsRemaining} months to live")
