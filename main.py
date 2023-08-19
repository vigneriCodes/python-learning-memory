# print("Welcome to my amazing band name generator.")

# city = input("What city where you born in?\n")
# pet = input("What is the name of your childhood pet?\n")

# print("Your band name could be " + city + " " + pet + "!")


print("Welcome to the tip calculator.")

billTotal = int(input("What was the total bill? $"))

diners = int(input("How many people split the bill? "))

tipPercent = 100 + int(input(
    "What percentage of tip would you like to give 15, 20, or 25? "))

result = str((billTotal * tipPercent/diners)/100)

print("Each person should pay $" + result)
