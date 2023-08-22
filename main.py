# print("Welcome to my amazing band name generator.")
# city = input("What city where you born in?\n")
# pet = input("What is the name of your childhood pet?\n")
# print(f"Your band name could be {city} {pet}!")

# ------------------

# inputStr = input("Enter a 2-digit number, and I will add it for you.\n")
# resultStr = int(inputStr[0]) + int(inputStr[1])
# print(resultStr)

# ------------------

# h = 1.778
# w = 91
# print("Welcome to the BMI calculator.")
# height = float(input("Enter your height(m) "))
# weight = float(input("Enter your weight(kg) "))
# bmiStr = str(round(weight / height ** 2, 1))
# print(f"{bmiStr} is your BMI.")

# ------------------

# print("Your life in weeks.")
# age = int(input("What is your current age?\n"))
# years_remaining = 90 - age
# days_left = years_remaining * 365
# weeks_left = years_remaining * 52
# months_left = years_remaining * 12
# print(f"You have {days_left} days left")
# print(f"You have {weeks_left} weeks left")
# print(f"You have {months_left} months left")

# ------------------

# print("Welcome to the tip calculator.")
# billTotal = float(input("What was the total bill? $"))
# diners = int(input("How many people split the bill? "))
# tipPercent = 100 + int(input(
#     "What percentage of tip would you like to give 15, 20, or 25? "))
# result = round((billTotal * tipPercent/diners)/100, 2)
# print(f"Each person should pay ${str(result)}")

# ------------------

# print("Welcome to Odd or Even")
# print("I can tell you if a number is even or...odd...")
# userNum = int(input("Enter a whole number "))
# if (userNum % 2 == 0):
#     print(f"{userNum} is an even number.")
# else:
#     print(f"{userNum} is an odd number")

# ------------------

# h = 1.778
# w = 91
# print("Welcome to BMI calculator v2.0.1")
# height = float(input("Enter your height(m) "))
# weight = float(input("Enter your weight(kg) "))
# bmi = round(weight / height ** 2, 1)
# bmiStr = str(bmi)
# weightClass = ""
# if (bmi < 18.5):
#     weightClass = "underwight"
# elif (bmi < 25):
#     weightClass = "normal weight"
# elif (bmi < 30):
#     weightClass = "overweight"
# elif (bmi < 35):
#     weightClass = "obese"
# else:
#     weightClass = "clinically obese"
# print(f"{bmi} is your BMI. Your weight is classified as: {weightClass}")


# ------------------

# print("Welcome to: IsLeapYear?")
# inputYear = int(input("Please enter a four digit year\n"))
# if (inputYear % 4 == 0):
#     if (inputYear % 100 == 0):
#         if (inputYear % 400 == 0):
#             print("Leap!")
#         else:
#             print("Not Leap")
#     else:
#         print("Leap")
# else:
#     print("Not Leap")

# ------------------

print("Welcome to Giancarlo's Python Pizza")
print("Prices: Small-$15 / Medium-$20 / Large-$25")
user_pizza_size = input(
    "What size pizza would you like? (S/M/L)\n").upper()
add_pepperoni = input("Do you want pepperoni? (S+$2 M/L+$3) Y or N\n").upper()
extra_cheese = input(
    "Would you like to add extra cheese? (+$3) Y or N\n").upper()
final_bill = 0
if (user_pizza_size == "S"):
    final_bill += 15
elif (user_pizza_size == "M"):
    final_bill += 20
elif (user_pizza_size == "L"):
    final_bill += 25
else:
    print("That is NOT a valid pizza size. Do you even want pizza?")
if (add_pepperoni == "Y"):
    if (user_pizza_size == "S"):
        final_bill += 2
    else:
        final_bill += 3
if (extra_cheese == "Y"):
    final_bill += 3
print(f"Your final bill is ${final_bill}")
