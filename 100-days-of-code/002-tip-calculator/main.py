## Main project - build a tip calculator

print("Welcome to the tip calculator!")
total_bill = float(input("What was your total bill? $"))
tip_percent = int(input("What perecent tip would you like to leave? 10, 12 or 15? "))
split = int(input("How many people does the bill need to be split by? "))
per_person = round((total_bill * ((tip_percent / 100) + 1) / split),2)
human_readable_per_person = "{:.2f}".format(per_person)
print(f"Each person needs to pay {human_readable_per_person}")