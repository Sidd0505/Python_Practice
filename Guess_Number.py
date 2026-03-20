#Guess the Number
import random

myguess = random.randint(1,20)
guess =  0

for i in range(1,5):
    print("Guess the Number :")
    guess = int(input())
    if(guess < myguess):
        print("Guess Higher")
    elif(guess > myguess):
        print("Guess Lower")
    else:
        break

if(guess == myguess):
    print(f"You have guessed number {guess} correctly in {i}th iteration")
else:
    print("Better Luck next time !!")