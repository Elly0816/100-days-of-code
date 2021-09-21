# programming_dictionary = {
#   "Bug" : "An error in a program that prevents the program from running as expected.",
#  "Function" : "A piece of code that you can easily call over and over again." ,
#  "Loop": "The action of doing something over and over again.",
# }


#Retrieving items from a dictionary
#print(programming_dictionary["Bug"])

#Adding new items to a dictionary
# programming_dictionary["List"] = "A datatype that contains many values."

#print(programming_dictionary["List"])

#Create an empty dictionary
#empty_dictionary = {}
#print(empty_dictionary)

#Wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#Edit an item in a dictionary
#programming_dictionary["Bug"] = "A moth in a computer"
#print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#  print(programming_dictionary[key])

# student_scores = {
#  "Harry": 81,
#  "Ron": 78,
#  "Hermoine": 99,
#  "Draco": 74,
#  "Neville": 62,
# }
#
# student_grades = {}
#
# for key in student_scores:
#  if 91<= student_scores[key] <= 100:
#   grade = 'Outstanding'
#  elif 81<= student_scores[key] <= 90:
#   grade = 'Exceeds Expectations'
#  elif 71<= student_scores[key] <= 80:
#   grade = 'Acceptable'
#  else:
#   grade = 'Fail'
#  student_grades[key] = grade
# print(student_grades)


#Nesting a list in a dictionary
capitals = {
 "France": ["Paris", "Lille", "Dijon"],
 "Germany": ["Berlin", "Hamburg", "Stuttgart"],

}

#Nesting a dictionary in a dictionary
travel_log = {
 "France": {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits": 12},
 "Germany": {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 15},
 "England": {"cities_visited" : ["Manchester", "Southampton", "London"], "total_visits": 18},
}

# print(travel_log["England"]['total_visits'])

#Nesting Dictionary in list
# travel_log = [
#  {"Country": "France",
#   "cities_visited" : ["Paris", "Lille", "Dijon"],
#   "total_visits": 12
#   },
#  {"Country": "Germany",
#   "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
#   "total_visits": 15
#   },
#  {"Country": "England",
#   "cities_visited" : ["Manchester", "Southampton", "London"],
#   "total_visits": 18
#   },
# ]


# travel_log = [
#  {
#   "country":"France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
#  },
#  {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
#  },
# ]
#
# def add_new_country(country, visits, cities):
#  travel_log.append({"country":country, "visits": visits, "cities": cities})
#  print(travel_log)
#
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
other_bidder = True
print(f"{logo} \nWelcome to the secret auction program ")
auction = {}
while other_bidder:
 name = input("What is your name?: ")
 bid = int(input("What's your bid?: $"))
 auction[name] = bid
 other = input("Are there any other bidders? Type 'yes' or 'no'. ")
 if other.lower() == 'no':
  other_bidder = False
 elif other.lower() == 'yes':
  clear()
max_value_keys = [key for key in auction.keys() if auction[key] == max(auction.values())]
print(f"The highest bidder was {''.join(map(str,max_value_keys)).capitalize()} with a bid of "
      f" ${max(auction.values())} .")