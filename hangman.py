# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 14:04:29 2018

@author: UDIT
"""

print("Welcome to the game of Hangman")

def player1_input():
    #randName = ''.join(random.choices(string.ascii_lowercase,k=random.randint(4,10))).title()
    #global word
    global noOfGuessess
    #word = input("Enter the word = ").lower()
    noOfGuessess = int(input("Set maximum no of attempts = "))
    
def player2_input(word,noOfGuessess):
    countCorrect = len(word)
    print("Length of word = ",countCorrect)
    print("_ "*countCorrect)
    guessCharacters = []
    while(countCorrect>0):
        guessCharacters.append("_ ")
        countCorrect-=1
    listOfCharacters = list(word)
    global win
    while(countCorrect!=len(word)):
        ch = input("Enter a character = ").lower()
        if ch in listOfCharacters:
            index = listOfCharacters.index(ch) 
            guessCharacters[index]=ch
            listOfCharacters[index]='$'
            print("Correct guess")
            countCorrect+=1
        else:
            noOfGuessess -= 1
            print("Wrong guess")
        print(guessCharacters)
        print("No of characters remaining to be guessed = ",len(listOfCharacters) - countCorrect,"\nGuess remaining = ",noOfGuessess)
        if(noOfGuessess == -1):
                print("\nYou lost the game")
                #print("Correct word = ",word)
                print("Correct word = ",word.capitalize())
                win = False
                break
            
def listOfLists():
    global categoryList
    
    carList = dataset.iloc[:,0:1].values
    carList = carList.astype(str).reshape(carList.size,1)

    brandList = dataset.iloc[:,1:2].values
    brandList = brandList.astype(str).reshape(brandList.size,1)

    countryList = dataset.iloc[:,2:3].values
    countryList = countryList.astype(str).reshape(countryList.size,1)

    charactersList = dataset.iloc[:,3:4].values
    charactersList = charactersList.astype(str).reshape(charactersList.size,1)

    sportsList = dataset.iloc[:,4:5].values
    sportsList = sportsList.astype(str).reshape(sportsList.size,1)

    actorsList = dataset.iloc[:,5:6].values
    actorsList = actorsList.astype(str).reshape(actorsList.size,1)

    actressList = dataset.iloc[:,6:7].values
    actressList = actressList.astype(str).reshape(actressList.size,1)
    
    categoryList = {'Car':carList,'Clothings':brandList,'Sports':sportsList,'Actors':actorsList,'Actress':actressList,'Characters':charactersList,
                    'Countries':countryList}

    for c in categoryList:
        print(c)

# Starting of Program
import random
import pandas as pd

dataset = pd.read_csv("10.csv")

categoryList = {}
listOfLists()#function calling

choice = True
while(choice):
    ch = input("Enter your desired category = ").capitalize()
    if ch not in categoryList:
        print("Please select the category carefully")
        ch = input("Enter your desired category = ").capitalize()
    else:
        choice = False
        
n = random.randint(0,41)
desiredList = categoryList[ch]
#word = desiredList[n]
word = str(desiredList[n]).lower()
#if(ch=='Countries' or ch == 'Car' or ch == 'Clothings' or ch == 'Characters' or ch == 'Sports'
#   or ch == 'Actors'):

word=word[2:len(word)-2]
noOfGuessess = random.randint(3,7)
print("No of guess awarded = ",noOfGuessess)
win = True

player2_input(word,noOfGuessess)  
if(win):
    print("\nCongratulations!!!\nYou won the game :)") 