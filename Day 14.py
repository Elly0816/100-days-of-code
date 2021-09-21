

def compare():
    global score
    global play_again
    if answer == 'a':
        if a.get('follower_count') >= b.get('follower_count'):
            score += 1
            return f"You're right, current score is {score}"
        else:
            play_again = False
            return f"Sorry that's wrong, Final score: {score}"
    elif answer == 'b':
        if b.get('follower_count') >= a.get('follower_count'):
            score += 1
            return f"You're right, current score is {score}"
        else:
            play_again = False
            return f"Sorry that's wrong. Final score: {score}"




import random
from Day14data import data
from Day14data import logo
from Day14data import vs
print(logo)
a = data[random.randrange(len(data))]
b = data[random.randrange(len(data))]
print(f"Compare A: {a.get('name')} a {a.get('description')} from {a.get('country')} with {a.get('follower_count')} followers.")
print(vs)
print(f"Against B: {b.get('name')} a {b.get('description')} from {b.get('country')} with {b.get('follower_count')} followers.")

#Ask the user to guess which of the dictionaries have a higher follower count
answer = input("Who has more followers? 'A' or 'B'? : ").lower()


play_again = True
score = 0
print(compare())

while play_again:
    a = b
    b = data[random.randrange(len(data))]
    print(f"\nCompare A: {a.get('name')} a {a.get('description')} from {a.get('country')} with {a.get('follower_count')} followers.")
    print(vs)
    print(f"Against B: {b.get('name')} a {b.get('description')} from {b.get('country')} with {b.get('follower_count')} followers.")

    # Ask the user to guess which of the dictionaries have a higher follower count
    answer = input("Who has more followers? 'A' or 'B'? : ").lower()
    print(compare())




