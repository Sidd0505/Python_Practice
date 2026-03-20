#Game 
import sys, random

Loss = 0
Win = 0
Tie = 0
while True:
    print(f"Wins : {Win},Losses : {Loss}, Ties : {Tie} in the game :)")
    while True:
        print("Enter (r)ock, (p)aper, (s)cissor :")
        playermove = input()
        if(playermove == "r"):
            print("Rock Vs. ")
            break
        if(playermove == "p"):
            print("Paper Vs. ")
            break
        if(playermove == "s"):
            print("scissor Vs. ")
            break
        if(playermove == "q"):
            sys.exit()
        
    num = random.randint(1,3)
    if(num == 1):
        computermove = "r"
        print("Rock")
    if(num ==2):
        computermove = "p"
        print("Paper")
    if(num == 3):
        computermove = "s"
        print("Scissor")
    

    if(playermove == "r" and computermove == "r"):
        Tie = Tie + 1
    elif(playermove == "r" and computermove == "p"):
        Loss = Loss + 1
    elif(playermove == "r" and computermove == "s"):
        Win = Win  + 1
    elif(playermove == "p" and computermove == "r"):
        Win = Win + 1
    elif(playermove == "p" and computermove == "p"):
        Tie = Tie + 1
    elif(playermove == "p" and computermove == "s"):
        Loss = Loss + 1
    elif(playermove == "s" and computermove == "r"):
        Loss = Loss + 1
    elif(playermove == "s" and computermove == "p"):
        Win = Win + 1
    elif(playermove == "s" and computermove == "s"):
        Tie = Tie + 1
        



