def my_function():
    print("Hello")
    print("I used a space for the indentation")


my_function()


#At this url: http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    while wall_on_right():
        move()
    else:
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        else:
            turn_left()


while not at_goal():
   while front_is_clear() and right_is_clear():
    turn_right()
    move()
   while wall_in_front():
    if wall_on_right():
        turn_left()
    else:
        turn_right()
   move()
