#Scope



#Local Scope

# def drink_potion():
#  potion_strength = 2
#  print(potion_strength)
#
#
# drink_potion()


#Global Scope

# player_health = 10
#
# def drink_potion():
#  potion_strength = 2
#  print(player_health)
#
# drink_potion()
# print(player_health)



# enemies = 1
#
# def increase_enemies():
#  print(f"enemies inside function: {enemies}")
#  return enemies + 1
#
#
# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")


#Global Constants

# PI = 3.14159
# URL = "https://www."`

logo = (""" __          __  _                            _                  _   _                 _                  _____                     _                _____
 \ \        / / | |                          | |                | \ | |               | |                / ____|                   (_)              / ____|
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___     __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \   / _` | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \|
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | (_| | | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__,_| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                                                                                             __/ |
                                                                                                                                            |___/                               """)

def compare():
 if user_guess > number:
   print ("Guess too high")
   return False
 elif user_guess < number:
  print("Guess too low")
  return False
 elif user_guess == number:
  print(f"You got it! The answer was {number}")
  l= input("Press Enter to Quit")
  return True
 else:
  return False

import random

print(logo)
#Pick random number between 1 and 100
number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")
# print(f"The correct answer is {number}")

#Ask user for difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'hard':
 guess = 5
else:
 guess = 10

ask = False

while not ask:
 if guess > 0:
  user_guess = int(input(f"You have {guess} attempts remaining.\nMake a guess: "))
  guess -= 1
  ask = compare()

 else:
  print(f"You lose! Out of guesses, the number is {number}")
  l = input("Press Enter to Quit")
  ask = True

