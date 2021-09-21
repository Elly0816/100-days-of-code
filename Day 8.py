#
# # def greet():
# #  print("Hello There")
# #  print("How are you?")
# #  print("I hope you're alright!")
# #
# #
# # def greet_with_name(name):
# #  print(f"Hello {name}!")
# #  print(f"How do you do {name}?")
# #  print(f"Isn't the weather nice today {name}?")
# #
# #
# # def greet_with(name, location):
# #  print(f"Hello {name}")
# #  print(f"What is it like in {location}?")
# #
# # greet_with(location= "Cyprus", name= "Eleazar")
#
# # def paint_calc(height, width):
# #  import math
# #  height= int(height)
# #  width= int(width)
# #  no_of_cans = (height * width)/5
# #  print(f"You'll need {math.ceil(no_of_cans)} cans of paint. ")
# #
# #
# # paint_calc(height = 5, width = 20)
#
# # n = int(input("Check this number: "))
# # def prime_checker(number):
# #  for i in range (2, number):
# #   if number%i == 0:
# #    return print("It's not a prime number.")
# #  return print("It is a prime number.")
# #
# #
# #
# # prime_checker(number = n)
#
# print("""""")
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # direction  = input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
# # text = input("Type your message:\n").lower()
# # shift = int(input("Type the shift number:\n"))
#
# def encrypt(plain_text, shift):
#  cipher_text = ""
#  for letter in plain_text:
#   position = alphabet.index(letter)
#   new_position = position+shift
#   new_letter = alphabet[new_position]
#   cipher_text += new_letter
#  return print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(cipher_text, shift):
#  decipher_text = ''
#  for letter in cipher_text:
#   position = alphabet.index(letter)
#   new_position = position - shift
#   new_letter = alphabet[new_position]
#   decipher_text += new_letter
#  return print(f"The decoded text is {decipher_text}")
#
#
# def caesar(text, shift, direction):
#  play_again = True
#  while play_again == True:
#   new_text = ""
#   while shift >= 26:
#    if shift % 25 == 0:
#     shift /= 25
#    else:
#     shift = round(shift / 25)
#   if direction.lower() == 'decode':
#    shift *= -1
#   for letter in text.lower():
#    if letter not in alphabet:
#     position = text.index(letter)
#     new_text += text[position]
#    else:
#     position = alphabet.index(letter)
#     new_position = position + shift
#     new_text += alphabet[new_position]
#   print(f"The {direction}d text is {new_text}")
#   result = input("Type 'yes' if you want to go again, otherwise type 'no':\n")
#   if result.lower() == 'no':
#    play_again = False
#    print("Goodbye")
#

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
 end_text = ""
 if cipher_direction == "decode":
  shift_amount *= -1
 for char in start_text:
  # TODO-3: What happens if the user enters a number/symbol/space?
  # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
  # e.g. start_text = "meet me at 3"
  # end_text = "•••• •• •• 3"
  if char not in alphabet:
   position = start_text.index(char)
   end_text += start_text[position]
  else:
   position = alphabet.index(char)
   new_position = position + shift_amount
   end_text += alphabet[new_position]

 print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
#from art import logo

#print(logo)

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
play_again = True
while play_again:
 direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
 text = input("Type your message:\n").lower()
 shift = int(input("Type the shift number:\n"))

 # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
 # Try running the program and entering a shift number of 45.
 # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
 # Hint: Think about how you can use the modulus (%).
 while shift >= 26:
  if shift % 25 == 0:
   shift /= 25
  else:
   shift = round(shift / 25)
 caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
 answer = input("Type 'yes' if you want to go again, otherwise type 'no':\n")
 if answer.lower() == 'no':
  play_again = False
  print("Goodbye")

#
#
#
#
#
# caesar('hello', 5, 'encode')
# caesar('mjqqt', 5, 'decode')
# decrypt('mjqqt',5)
# encrypt('hello', 5)
#
