print("Welcome to my computer quiz !")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :)")

score = 0

answer = input("What does CPU stand for? ")

if answer.lower()== "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect!")

answer = input("What does GPU stand for? ")

if answer.lower() == "graphic processing unit":
    print("correct")
    score += 1
else:
    print("incorrect!")
    
print("You got " + str(score) + " question correct")

print("You got " + str((score/2) * 100) + "%")

    

