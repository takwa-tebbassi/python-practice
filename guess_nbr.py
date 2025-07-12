from random import*
from math import*

def guess_number():

    nbr = randint(1,100)
    guessed = int(input("guess the nbr: it's between 1 - 100 : "))

    while(nbr != guessed):
        if(nbr > guessed):
            print("Too low ! ")
            guessed = int(input("try again.. "))
    
        elif(nbr < guessed):
            print("Too high ! ")
            guessed = int(input("try again.. "))

    if(nbr == guessed):
        print("Right guess! Good job. ")

    

# main program

guess_number()