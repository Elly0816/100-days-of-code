# def multiply(num1, num2):
#  return num1 * num2
#
#
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# print(multiply(num1, num2))

# def format_name(f_name = input("What is your first name? "), l_name = input("What is your last name? ")):
#  """Takes a first and last name and formats it to
#  a title case version full name"""
#  if f_name == "" or l_name == "":
#   return print("You did not enter valid inputs")
#  else:
#   full_name = f"{f_name} \n{l_name}".title()
#   return print(full_name)
#
#
# format_name()


# def is_leap(year):
#  if year % 4 == 0:
#   if year % 100 == 0:
#    if year % 400 == 0:
#     return True
#    else:
#     return False
#   else:
#    return True
#  else:
#   return False
#
# def days_in_month(year, month):
#  if type(year) != int or type(month) != int:
#   return print("Invalid datatypes for year or month")
#  if month > 12 or month < 1:
#   return print("Invalid month")
#  month -= 1
#  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#  if is_leap(year) and month == 1:
#   return print(29)
#  else:
#   return print(month_days[month])
#
# days_in_month(3084, 2)


#Calculator

#Add
def add(n1, n2):
 return n1 + n2

#Subtract
def subtract(n1, n2):
 return n1 - n2

#Multiply
def multiply(n1, n2):
 return n1 * n2

#Divide
def divide(n1, n2):
 return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }
def calculator():
 num1 = float(input("What is the first number?: "))
 for key in operations:
  print(key)
 symbol = input("Pick an operation from the line above: ")
 num2 = float(input("What is the second number?: "))
 calculation = operations[symbol]
 answer = calculation(num1, num2)
 print(f"{num1} {symbol} {num2} = {answer}")
 cont_calc  = True
 while cont_calc:
  next_calc = input(f"Type 'y' to continue calculating with {answer}, type 'a' for new calculation"
                     f" or type 'n' to exit.: ")
  if next_calc.lower() == 'n':
   cont_calc = False
  elif next_calc.lower() == 'y':
   symbol = input("Pick another operation: ")
   num3 = float(input("What is the next number?: "))
   calculation = operations[symbol]
   second_answer = calculation(answer, num3)
   print(f"{answer} {symbol} {num3} = {second_answer}")
   answer = second_answer
  elif next_calc.lower() == 'a':
   cont_calc = False
   calculator()

calculator()


