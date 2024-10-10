name = input("Type your name: ")
print("Welcome", name, "To this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go right or left. Which way would you like to go? ")

if answer == "right":
    answer == input("You come to a river, you can walk around it or swim acrosss? Type wlk to walk around it and swim to swim across: ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        ('Not a valid option. You lose.')  

if answer == "left":
    print("You came to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")  

    if answer ==  "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer == input("You cross the bridge and meet a stranger. Do you talk to them(Yes/No)? ")

    if naswer == "Yes":
        print("You talk to the stranger and they give you a gold. You WIN!")

    elif answer == "No":
        print("You egnore the stranger and they offended and you lose.")

    else:
        ('Not a valid option. You lose.')

    
else:
    ('Not a valid option. You lose.')

else:
    ('Not a valid option. You lose.')    