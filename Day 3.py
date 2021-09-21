# print('''*******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************
# ''')
#
# print("Welcome to Treasure Island. \nYour mission is to find the treasure")
# direction = str.lower(input("While walking down a spooky path, the road ahead of you forks in 2 directions. \nIt's up to you to make a choice. Do you pick Left or Right? \n"))
# if direction == 'left':
#     river = str.lower(input("The left path leads you to a river. \nA boat arrives in a while, so you have two choices: Swim or Wait\n"))
#     if river == 'wait':
#         door = str.lower(input("You have arrived at an Island with 3 doors, a yellow, a red and a blue door. \nWhich door would you pick?\n"))
#         if door == 'yellow':
#             print("You Win! \nYou possess the Treasure of King Arthur")
#         elif door == 'red':
#             print("You picked the red door! \nPrepare to be cooked by fire!\n Game Over!")
#         else:
#             print("Oops, you've picked the blue door! \nPrepare to be devoured by Nautilus the dragon! Game Over")
#     else:
#         print("Ooops, you chose to swim and have now been devoured by man eating piranhas. \nGame Over")
# else:
#     print("Oops, the right road was the wrong choice.\n You have been clobbered by Mogus the troll! \nGame Over")


# print("Welcome to the Love Calculator!")
# name1 = str.lower(input("What is your name? \n"))
# name2 = str.lower(input("What is their name> \n"))
# name = name1 + name2
# t = name.count('t')
# r = name.count('r')
# u = name.count('u')
# e = name.count('e')
# true = t + r + u + e
#
# l = name.count('l')
# o = name.count('o')
# v = name.count('v')
# e = name.count('e')
# love = l + o + v + e
#
# true_love = str(true) + str(love)
# true_love = int(true_love)
#
# if true_love<10 or true_love>90:
#     print(f"Your score is {true_love}%, you go together like coke and mentos.")
# elif true_love>=40 and true_love<=50:
#     print(f"Your score is {true_love}%, you are alright together.")
# else:
#     print(f"Your score is {true_love}%")







# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L\n")
# pepperoni = input("Do you want pepperoni? Y or N\n")
# cheese = input("Do you want extra cheese? Y or N\n")
# if str.lower(size)=="s":
#     price = 15
#     print(f"Small Pizza: ${price}")
# elif str.lower(size)=="m":
#     price = 20
#     print(f"Medium Pizza: ${price}")
# else:
#     price = 25
#     print(f"Large Pizza: ${price}")
# if str.lower(pepperoni) == 'y':
#     if str.lower(size) == 's':
#         price += 2
#         pepperoni_small = 2
#         print(f"Pepperoni for Small Pizza is ${pepperoni_small}")
#     else:
#         price += 3
#         pepperoni_medium_large = 3
#         print(f"Pepperoni for Medium or Large Pizza is ${pepperoni_medium_large}")
# if str.lower(cheese) == "y":
#     price += 1
#     print(f"Your final bill is: ${price}")
# else:
#     print(f"Your final bill is: ${price}")



# print("Welcome to the rollercoaster!")
# height=int(input("What is your height in cm? "))
#
# if height>=120:
#   print("You are tall enough to ride the roller coaster!")
#   age=int(input("How old are you? "))
#   if age<12:
#     price = 5
#     print(f"Child tickets are ${price}")
#   elif age<=18:
#     price = 7
#     print(f"Youth tickets are ${price}")
#   elif age>=45 and age<=55:
#       price = 0
#       print(f"Everything is going to be ok. Have a free ride on us!")
#   else:
#     price = 12
#     print(f"Adult tickets are ${price}")
#   if  not 45<=age<=55:
#     photos = input("Do you want pictures? Y or N: ")
#     if str.lower(photos) == 'y':
#         price += 3
#         print(f"Your total bill is ${price}")
#     else:
#       print(f"Your total bill is ${price}")
# else:
#   print("You are too short for the roller coaster!")








# year = int(input("Which year do you want to check? "))
# if year%4==0:
#   if year%100==0:
#     if year%400==0:
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")
#   else:
#       print(f"{year} is a leap year")
# else:
#   print(f"{year} is not a leap year")

