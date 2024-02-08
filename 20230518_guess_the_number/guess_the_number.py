

import random   


num = random.randint(1, 10) # returns a random number between 1 and 10 
guess = None  

while guess != num:
    guess = input("guess a number between 1 and 10: ") 
    guess = int(guess)
    
    if guess == num:
        print("congratulations! you won!")
        break # if the guess is correct, then "break" is used to exit the loop and skip the remaining iterations
    
    else:
        print("nope, sorry. Try again") 
        




