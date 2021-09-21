import random
import string
# fruits = ['Apple', 'Peach', 'Pear']
# for fruit in fruits:
#     print(fruit)
#     print(f"{fruit} Pie")
# print(fruits)

# student_heights = input("Enter the heights of students:\n").split()
# total_height = 0
# for height in student_heights:
#     height = int(height)
#     total_height += height
# avg = total_height/len(student_heights)
# print(f"Average height is {avg}")

# student_scores = input("Input a list of student scores:\n").split()
# max_score = 0
# min_score = 100
# for score in student_scores:
#     score = int(score)
#     if score > max_score:
#         max_score = score
#     if score < min_score:
#         min_score = score
# print(f"The highest score is {max_score}\nThe lowest score is {min_score}")

# total = 0
# for number in range(0,101,2):
#     total += number
# print(f"The sum of all even number from 1 to 100 is: {total}")

# for number in range(1,101):
#     if number%3 == 0 and number%5 == 0:
#         print("FizzBuzz")
#     elif number%3 == 0:
#         print("Fizz")
#     elif number%5 ==0:
#         print("Buzz")
#     else:
#         print(number)

letters = list(map(str, string.ascii_letters))
numbers = list(map(str, string.digits))
symbols = list(map(str, string.punctuation))

#Ask user for numbers of different data types
print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))

password = ""
#pick num_data_type random data_types
for i in range (1, num_letters+1):
    password += (random.choice(letters))
for i in range (1, num_numbers+1):
    password += (random.choice(numbers))
for i in range (1, num_symbols+1):
    password += (random.choice(symbols))

#Shuffle characters in password
pass_list = list(password)
random.shuffle(pass_list)
result = ''.join(pass_list)
print(f"Your password is: {result}")

