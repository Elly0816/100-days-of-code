import random

# random_integer = random.randint(0,10)
# print(random_integer)

# test_seed = int(input("Create a seed number:\n"))
# random.seed(test_seed)
#
# #Get names as a csv
# namesasCSV = input("Enter the names separated by commas and a space: ")
# names = namesasCSV.split(", ")
# num_to_pay = random.randint(0, len(names)-1)
# pay = names[num_to_pay]
# print(f"{str.capitalize(pay)} is going to buy the meal today!.")


# row1 = [" ", " ", " "]
# row2 = [" ", " ", " "]
# row3 = [" ", " ", " "]
# map = [row1, row2, row3]
#
# position = input("Where do you want to place the X?")
#
#first number in position is index for map
#second number in position is index for row
#
# horizontal = int(position[0])
# vertical = int(position[1])
# map[vertical-1][horizontal-1] = "X"
#print(f"{row1}\n{row2}\n{row3}")

# user_choice = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors:\n"))
# bot_choice = random.randint(0,2)
# if user_choice == 2:
#     print("""
#         _______
#     ---'   ____)____
#               ______)
#            __________)
#           (____)
#     ---.__(___)
#     """)
#     if bot_choice == 1:
#         print("""Computer chose\n
#              _______
#         ---'    ____)____
#                    ______)
#                   _______)
#                  _______)
#         ---.__________)
#         """)
#         print("Scissors beats paper! You win")
#     elif bot_choice == 0:
#         print("""Computer chose \n
#             _______
#         ---'   ____)
#               (_____)
#               (_____)
#               (____)
#         ---.__(___)
#         """)
#         print("You lose, rock beats scissors")
#     else:
#         print("""Computer chose \n
#             _______
#         ---'   ____)____
#                   ______)
#                __________)
#               (____)
#         ---.__(___)
#         """)
#         print ("It's a draw")
# elif user_choice == 1:
#     print("""
#          _______
#     ---'    ____)____
#                ______)
#               _______)
#              _______)
#     ---.__________)
#     """)
#     if bot_choice == 2:
#         print("""Computer chose\n
#             _______
#         ---'   ____)____
#                   ______)
#                __________)
#               (____)
#         ---.__(___)
#         """)
#         print("You lose, scissors beats paper")
#     elif bot_choice == 1:
#         print("""Computer chose\n
#              _______
#         ---'    ____)____
#                    ______)
#                   _______)
#                  _______)
#         ---.__________)
#         """)
#         print("It's a draw")
#     else:
#         print("""Computer chose \n
#             _______
#         ---'   ____)
#               (_____)
#               (_____)
#               (____)
#         ---.__(___)
#         """)
#         print("Paper beats rock, You win!")
# elif user_choice == 0:
#     print("""
#         _______
#     ---'   ____)
#           (_____)
#           (_____)
#           (____)
#     ---.__(___)
#     """)
#     if bot_choice == 2:
#         print("""Computer chose \n
#             _______
#         ---'   ____)____
#                   ______)
#                __________)
#               (____)
#         ---.__(___)
#         """)
#         print("Rock beats scissors, You win!")
#     elif bot_choice == 1:
#         print("""Computer chose \n
#              _______
#         ---'    ____)____
#                    ______)
#                   _______)
#                  _______)
#         ---.__________)
#         """)
#         print("Paper beats rock, You lose!")
#     else:
#         print("""Computer chose \n
#             _______
#         ---'   ____)
#               (_____)
#               (_____)
#               (____)
#         ---.__(___)
#         """)
#         print("It's a draw!")
# else:
#     print("You made an invalid choice!")


