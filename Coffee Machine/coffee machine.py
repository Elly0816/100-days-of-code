from main import MENU
from main import resources


# TODO 1: Create functions for each menu item
def total():
 """This calculates the total for the coins added"""
 total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
 return total

def espresso():
 """This returns the cost for an espresso"""
 global resources
 global money
 remaining_water = resources['water'] - MENU['espresso']['ingredients']['water']  #Calculate remaining water
 resources['water'] = remaining_water
 remaining_coffee = resources['coffee'] - MENU['espresso']['ingredients']['coffee']  #Calculate remaining coffee
 resources['coffee'] = remaining_coffee
 cost = round((MENU['espresso']['cost'g]), 2)  #Get the cost
 change = 0  # Set change to zero for each item chose
 if total() >= cost:  # Check if the money paid is enough for an espresso
  change += (total() - cost)  # Calculate the change
  money += cost  # Update the amount of money left in the machine
  print(f"Here is ${round(change, 2)} in change.")
  print(f"Here is your {prompt} ☕ Enjoy!")
 else:
  print("Sorry that's not enough money. Money refunded.")



def cappuccino():
 """This returns the cost for a cappuccino"""
 global resources
 global money
 remaining_water = resources['water'] - MENU['cappuccino']['ingredients']['water']  #Calculate remaining water
 resources['water'] = remaining_water
 remaining_coffee = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']  #Calculate remaining coffee
 resources['coffee'] = remaining_coffee
 remaining_milk = resources['milk'] - MENU['cappuccino']['ingredients']['milk']  #Calculate remaining milk
 resources['milk'] = remaining_milk
 cost = round((MENU['cappuccino']['cost']), 2)   #Get the cost
 change = 0  # Set change to zero for each item chose
 if total() >= cost:  # Check if the money paid is enough for a cappuccino
  change += (total() - cost)  # Calculate the change
  money += cost  # Update the amount of money left in the machine
  print(f"Here is ${round(change, 2)} in change.")
  print(f"Here is your {prompt} ☕ Enjoy!")
 else:
  print("Sorry that's not enough money. Money refunded.")

def latte():
 """This returns the cost for a latte"""
 global resources
 global money
 remaining_water = resources['water'] - MENU['latte']['ingredients']['water']  #Calculate remaining water
 resources['water'] = remaining_water
 remaining_coffee = resources['coffee'] - MENU['latte']['ingredients']['coffee']  #Calculate remaining coffee
 resources['coffee'] = remaining_coffee
 remaining_milk = resources['milk'] - MENU['latte']['ingredients']['milk']  #Calculate remaining milk
 resources['milk'] = remaining_milk
 cost = round((MENU['latte']['cost']), 2)   #Get the cost
 change = 0  # Set change to zero for each item chose
 if total() >= cost:  # Check if the money paid is enough for a latte
  change += (total() - cost)  # Calculate the change
  money += cost  # Update the amount of money left in the machine
  print(f"Here is ${round(change, 2)} in change.")
  print(f"Here is your {prompt} ☕ Enjoy!")
 else:
  print("Sorry that's not enough money. Money refunded.")




def resources_left():
 """Checks if the amount or resources left are enough"""
 for key in resources.keys() and MENU[prompt]['ingredients'].keys():
   if MENU[prompt]['ingredients'][key] > resources[key]:
    print(f"Sorry, there is not enough {key} left")
    return False
   else:
    return True



# TODO 2: Prompt user by asking what they would like between
#  espresso/ latte/ cappucino.(Show the prompt after every completed action).






# print(latte())
# print(resources)

make_coffee = True   #Set flag for which to run the coffee maker

money = 0   #Initialise the amount of money in the coffee maker


while make_coffee:
 prompt = input(" What would you like? (espresso/latte/cappuccino):").lower()
 if prompt == 'report':
  print(f"Water:{resources.get('water')}ml")
  print(f"Milk:{resources.get('milk')}ml")
  print(f"Coffee:{resources.get('coffee')}g")
  print(f"Money:${money}")
 elif prompt == 'off':
  make_coffee = False
 elif (prompt in MENU) and resources_left():
   # Check if the prompt exists in MENU there are enough resources for the prompt input
  print("Please insert coins.")   #Ask for coins
  quarters = int(input("How many quarters?: "))
  dimes = int(input("How many dimes?: "))
  nickels = int(input("How many nickels?: "))
  pennies = int(input("How many pennies?: "))
  if prompt == 'espresso':
   espresso()
  elif prompt == 'latte':
   latte()
  elif prompt == 'cappuccino':
   cappuccino()
 else:
  print("Invalid choice")





