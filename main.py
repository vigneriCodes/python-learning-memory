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

# print("Welcome to Giancarlo's Python Pizza")
# print("Prices: Small-$15 / Medium-$20 / Large-$25")
# user_pizza_size = input(
#     "What size pizza would you like? (S/M/L)\n").upper()
# add_pepperoni = input("Do you want pepperoni? (S+$2 M/L+$3) Y or N\n").upper()
# extra_cheese = input(
#     "Would you like to add extra cheese? (+$3) Y or N\n").upper()
# final_bill = 0
# if (user_pizza_size == "S"):
#     final_bill += 15
# elif (user_pizza_size == "M"):
#     final_bill += 20
# elif (user_pizza_size == "L"):
#     final_bill += 25
# else:
#     print("That is NOT a valid pizza size. Do you even want pizza?")
# if (add_pepperoni == "Y"):
#     if (user_pizza_size == "S"):
#         final_bill += 2
#     else:
#         final_bill += 3
# if (extra_cheese == "Y"):
#     final_bill += 3
# print(f"Your final bill is ${final_bill}")

# ------------------

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name?\n").lower()
# name2 = input("What is their name?\n").lower()
# names = name1 + name2
# t_str = "true"
# l_str = "love"
# score1 = 0
# score2 = 0

# for letter in names:
#     if letter in t_str:
#         score1 += 1
# for letter in names:
#     if letter in l_str:
#         score2 += 1
# # for letter in t_str:
# #     score1 += names.count(letter)
# # for letter in l_str:
# #     score2 += names.count(letter)

# total_score = int(str(score1) + str(score2))

# if (total_score <= 50 and total_score >= 40):
#     print(f"Your score is {total_score}, you are alright together.")
# elif (total_score < 10 or total_score > 90):
#     print(
#         f"Your score is {total_score}, you go together like coke and mentos.")
# else:
#     print(f"Your score is {total_score}.")

# ------------------

# import random
# print("Welcome to Treasure Island!?")
# print("Your mission is to find the treasure?")
# choice1 = input(
#     "You are walking along a wooded trail. You come to a crossorads. Which direction do you choose; 'left' or 'right'?)\n").lower()
# if (choice1 == "left"):
#     choice2 = input(
#         "You've chosen the left path. It leads to a pier on the bank of a grand lake. Would you like to 'swim' or 'wait'?\n").lower()
#     if (choice2 == "wait"):
#         choice3 = input("While waiting on the pier, three doors appear in front of you. One blue, one red, and one yellow. You feel compelled to enter one of them. Which door will you enter; 'blue' 'red' or 'yellow'?\n").lower()
#         if (choice3 == "yellow"):
#             print("Wow! You found the treasure. What an adventure. You win!?")
#         elif (choice3 == "red"):
#             print("Wrong door. It leads to a room full of fire. You're dead. Game Over.")
#         elif (choice3 == "blue"):
#             print("Wrong door. An immense volume of water rushes out of the door and knocks you into the lake. The Gator eats you. Game Over")
#         else:
#             print("That wasn't even one of your choices! Game Over.")
#     else:
#         print("You've been eaten by a big ol' Gator. Game Over.")
# else:
#     print("You fell into a hole. Game Over.")

# ------------------

# import random
# coin_int = random.randint(0, 1)
# if coin_int == 0:
#     print("Heads🧕")
# else:
#     print("Tails🦖")

# ------------------

# import random
# print("Welcome to Banker Roulette!")
# names_string = input("Enter everyone's name who is playing\n")
# names = names_string.split(", ")
# rand_int = random.randint(0, len(names)-1)
# print(f"{names[rand_int]} is paying the bill. Thanks!")

# ------------------

# print("Welcome to the Treasure Map")
# row1 = ["🔲", "🔲" ,"🔲"]
# row2 = ["🔲", "🔲" ,"🔲"]
# row3 = ["🔲", "🔲" ,"🔲"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}\n")
# position = input("Where do you want to put the treasure?\n")
# if int(position) < 11 or int(position) > 33:
#     print("Nope!")
# else:
#     cords = [int(item) for item in position]
#     x_axis = cords[0] - 1
#     y_axis = cords[1] - 1
#     map[y_axis][x_axis] = "X"
#     print(f"{row1}\n{row2}\n{row3}\n")


# ------------------

# import random
# print("Let's play Rock, Paper, Scissors")
# icons = ["🥌", "🧻", "✂"]
# user_turn = int(input("Rock = 0 | Paper = 1 | Scissors = 2\n"))
# comp_turn = random.randint(0, 2)
# print(f"You: {icons[user_turn]}")
# print(f"Opponent: {icons[comp_turn]}")
# if (user_turn == 0 and comp_turn == 2) or (user_turn == 2 and comp_turn == 1) or (user_turn == 1 and comp_turn == 0):
#     print("You Win!")
# elif (user_turn == comp_turn):
#     print("It's a Draw")
# else:
#     print("You Lose!")

# ------------------

# high_score = 0
# score_input = input(
#     "Enter some scores (single space between them)\n").split(" ")
# scores = [int(string) for string in score_input]
# # SCORES = [78, 65, 89, 55, 91, 64, 89]
# # for score in SCORES:
# for score in scores:
#     if (score > high_score):
#         high_score = score
# print(f"The highest score of the class is: {high_score}")

# ------------------

# sum = 0
# for number in range(1, 101, 2):
#     sum += number
# print(sum)

# sum = 0
# for number in range(1, 101):
#     if (number % 2 == 0):
#         sum += number
# print(sum)

# ------------------

# print("Welcome to FIZZBUZZ!")

# for number in range(1, 101):
#     if (number % 3 == 0) and (number % 5 == 0):
#         print("FizzBuzz")
#     elif (number % 5 == 0):
#         print("Buzz")
#     elif (number % 3 == 0):
#         print("Fizz")
#     else:
#         print(number)


# ------------------

import random
print("Welcome to the py_password generator!")
user_letter_amt = int(
    input("How many letters would you like in your password?\n"))
user_symbol_amt = int(input("How many symbols would you like?\n"))
user_number_amt = int(input("How many numbers would you like?\n"))
LETTERS_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS_LIST = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
NUMBERS_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def get_chars(user_input, chars_list, output_list):
    for number in range(1, (user_input + 1)):
        rand_index = random.randint(0, (len(chars_list) - 1))
        output_list.append(chars_list[rand_index])


all_chars = []
get_chars(user_letter_amt, LETTERS_LIST, all_chars)
get_chars(user_symbol_amt, SYMBOLS_LIST, all_chars)
get_chars(user_number_amt, NUMBERS_LIST, all_chars)
random.shuffle(all_chars)
password = str.join("", all_chars)
print(f"Here is your password:\n{password}")

# ------------------
# ------------------
# ------------------
# ------------------
# ------------------
# ------------------
# ------------------
# ------------------
# ------------------
# ------------------
# ------------------
# ------------------
# ------------------
# ------------------
# ------------------
# ------------------
