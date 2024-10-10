print("Welcome to my computer quiz!")

Playing = input("do you want to Play? ")

# text = "Tim IS GReat!"
# print(text.lower())
# .lower

if Playing.lower() != "yes":
     quit()

print("Okay! let's play: )")  
score = 0  

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing Unit":
    print('Correct!')
    score += 1
    # score = score + 1
else:
    print("Incorrect!")    


answer = input("What does GPU stands for? ")
if answer.lower() == "Grahpics Processing Unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")    


answer = input("What does RAM stands for? ")
if answer == "random access memmory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")     


answer = input("What does PSU stands for? ")
if answer.lower() == "Power Supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")    

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")


# "tim" + "1" = "tim1"


         

