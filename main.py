# print("Welcome to my amazing band name generator.")
# city = input("What city where you born in?\n")
# pet = input("What is the name of your childhood pet?\n")
# print(f"Your band name could be {city} {pet}!")

# ------------------

# inputStr = input("Enter a 2-digit number, and I will add it for you.\n")
# resultStr = int(inputStr[0]) + int(inputStr[1])
# print(resultStr)

# ------------------

# print("Welcome to the tip calculator.")
# billTotal = int(input("What was the total bill? $"))
# diners = int(input("How many people split the bill? "))
# tipPercent = 100 + int(input(
#     "What percentage of tip would you like to give 15, 20, or 25? "))
# result = round((billTotal * tipPercent/diners)/100, 2)
# print(f"Each person should pay ${str(result)}")

# ------------------

# print("Welcome to the BMI calculator.")
# height = float(input("Enter your height(m) "))
# weight = float(input("Enter your weight(kg) "))
# bmiStr = str(round(weight / height ** 2, 1))
# print(f"{bmiStr} is your BMI.")


# ------------------


print("Your life in weeks.")

age = int(input("What is your current age?\n"))

years_remaining = 90 - age

days_left = years_remaining * 365
weeks_left = years_remaining * 52
months_left = years_remaining * 12

print(f"You have {days_left} days left")
print(f"You have {weeks_left} weeks left")
print(f"You have {months_left} months left")

# print(f"You have X days, Y weeks, and Z months left.")
