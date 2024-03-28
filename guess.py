#import random
import random

#use random.randint()  
num = random.randint(1, 10)
guess = None
   
#use while loop 
while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)
    
    if guess == num:
        print("congratulations! you guessed it right!")
        break
    else:
        print("sorry, try again!")
