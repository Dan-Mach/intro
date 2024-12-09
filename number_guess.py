import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number that is greater than zero.")
        quit()

else:
    print("Please type a digit.")
    quit()


random_number = random.randrange(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number.")
        continue
    
    if user_guess == random_number:
        print("you got it! ")
        break
    elif user_guess > random_number:
            print("Greater than number! ")
    else:
        print("Lower than the  number! ")
        
print("You got it in ", guesses, "guessses")

    


    



