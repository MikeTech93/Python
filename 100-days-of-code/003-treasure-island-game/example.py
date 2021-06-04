## Coding exercise #1 - Ticket stand
print("Welcome to the rollercoaster!")
height=float(input("How tall are you in CM "))
bill = 0

if height >= 120:
    print("Well done, you are tall enough to go on the ride!")
    age=int(input("But... How old are you? "))
    
    if age > 18 and (age <45 or age >55):
        print("Adult tickets are $12")
        bill = 12
    elif age >=12 and age <= 18:
        print("Youth tickets are $7")
        bill = 7
    elif age >=45 and age <=55:
        print("Are you having a midlife crisis? Your ticket is free :)")
    else:
        print("Child tickets are $5")
        bill = 5

    photo = input("Do you want a photo taken? Y or N ")
    if photo == "Y":
        bill += 5

    print(f"Your finall bill is ${bill}")

else:
    print("Sorry, you are not tall enough to go on this ride")

## coding exercise #2 - Is the number Odd or Even?
number = int(input("Enter a whole number to check if it is odd or even"))
if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

# coding exercise #3 - BMI Calculator 2.0
h = float(input("Enter your height in m: "))
w = float(input("Enter your weight in kg: "))
bmi = (w / (h**2))

if bmi < 18.5:
    weight = "Underweight"
elif bmi < 25:
    weight = "Normal Weight"
elif bmi < 30:
    weight = "Overweight"
elif bmi < 35:
    weight = "Obese"
else:
    wieght = "Clinically Obese"

print("Your BMI is " + str(round(bmi,2)) + " and you are currently " + weight)

# coding exercise #4 - Leap Year Challenge

year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    print("This year is divisible by 4, continue onto further checks")
    if year % 100 == 0:
        print("this year is divisible by 4 and 100, continue onto further checks")
        if year % 400 == 0:
            print("This year is divisible by 4, 100 and 400 so it is a leap year")
        else:
            print("This year is divisible by 4 and 100 but not 400 so it is not a leap year")
    else:
        print("The year is evenly divisible by 4 and not divisble by 100 so it is a leap year")
else:
    print("This year is not divisble by 4 so it is not a leap year")

# coding exercise #5 - Pizza Order Calculator
print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y, N ")
extra_cheese = input("Do you want extra cheese? Y, N ")
cost = 0

if size == "S":
    cost += 15
    if add_pepperoni == "Y":
        cost += 2
elif size == "M":
    cost += 20
    if add_pepperoni == "Y":
        cost += 3
elif size == "L":
    cost += 25
    if add_pepperoni == "Y":
        cost += 3
else:
    print("You entered an incorrect size pizza")

if extra_cheese == "Y":
    cost += 1

print(f"Your final bill is: ${cost}")

# coding exercise #6 - Love Calculator

## TO DO