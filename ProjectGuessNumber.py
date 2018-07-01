# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 14:50:50 2018

@author: UDIT
"""

import random
import time
min1=1
max1=100
print("Take a guess b/w {} and {}".format(min1,max1))
guessNumber=int(input("Guessed number = "))
randNumber=random.randint(min1,max1)


choice=""
count=0
while(guessNumber!=randNumber ):
    print("Wrong Guess\n")
    if(guessNumber<randNumber):
        print("Number is greater\n")
    else:
        print("Number is smaller\n")
    count+=1
    print("Want to continue?\n")
    choice = input("Enter Y or N = ")
    if(choice.capitalize()=='N' ):
        print("Correct Number = {}\n".format(randNumber))
        print("Attempts made = {}\nThanks for playing\nQuitting now\n".format(count))
        break
    guessNumber = int(input("Guessed Number = "))
if(guessNumber==randNumber):
    print("Congrats you guessed it right in {} attempt\n".format(count+1))

print("Want to see the correct method\nPress 1 for Yes 0 for No")
ch = int(input("Either 1 or 0:Choice  = "))

if(ch):
    def magic(min1,max1):
        global guessNumber
        guessNumber=min1+max1
        if guessNumber%2!=0:
            guessNumber-=1
        guessNumber//=2
        
    #print("Take a guess between {}-{}\n".format(min1,max1))
    count=0
    magic(min1,max1)
    
    print("Guessed number = {}".format(guessNumber))
    while(guessNumber!=randNumber):
        
        print("Wrong Guess")
        if(guessNumber<randNumber):
            min1=guessNumber
            print("secret number is greater ...")
        else:
            max1=guessNumber
            print("secret number is lesser ...")
        time.sleep(2)
        magic(min1,max1)        
        count+=1
        print("\nGuessed number = {}".format(guessNumber))
    msg="correct number {} guessed right in {} attempt".format(randNumber,count+1)
    if count>1:
        msg=msg+'s'
    print(msg)

