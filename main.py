import random
from re import M
from tracemalloc import start
title = "  _    _                                           __   ___  \n | |  | |                                         /_ | / _ \ \n | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __    | || | | |\n |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \   | || | | |\n | |  | | (_| | | | | (_| | | | | | | (_| | | | |  | || |_| |\n |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  |_(_)___/ \n                      __/ |                                  \n                     |___/                                   \n" #the hangman title
def get_word(): #load world list
     with open('words/DE_all.txt') as f:
         lines = f.readlines()
     word=(str(random.choice(lines)))
     return word
def gen_hangman(mistakes): #generate the hangman image for any given mistakes
    if(mistakes==0):
        return "           \n           \n           \n           \n           \n           \n           \n           \n"
    elif(mistakes==1):
        return "           \n           \n           \n           \n           \n┌────────┐ \n│        └┐\n└─────────┘\n"
    elif(mistakes==2):
        return " |         \n │         \n │         \n │         \n │         \n┌┴───────┐ \n│        └┐\n└─────────┘\n"
    elif(mistakes==3):
        return " ┌───┐     \n │         \n │         \n │         \n │         \n┌┴───────┐ \n│        └┐\n└─────────┘\n"
    elif(mistakes==4):
        return " ┌───┐     \n │   O     \n │         \n │         \n │         \n┌┴───────┐ \n│        └┐\n└─────────┘\n"
    elif(mistakes==5):
        return " ┌───┐     \n │   O     \n │  /│\    \n │         \n │         \n┌┴───────┐ \n│        └┐\n└─────────┘\n"
    elif(mistakes==6):
        return " ┌───┐     \n │   O     \n │  /│\    \n │  / \    \n │         \n┌┴───────┐ \n│        └┐\n└─────────┘\n"
    else:
        return 0

input = ""
word = get_word()
mistakes = 0
guessed_letters = ""
def print_game():
    #prints title, hangman statue and filld letters
    print(title)
    print(gen_hangman(mistakes))
    for i in range(len(word)-1):
        if(word[i] in guessed_letters):
            print(word[i]+" ", end="")
        else:
            print("_ ", end="")
    print('')
    print(word)
    input = input("Enter a leter: ")
print_game()

if(input.upper() in word.upper()):
     #if letter correct
    guessed_letters+=input



elif(mistakes==6):
    print(gen_hangman(mistakes))
    print("Game Over!")
    print("The word was: " + word)
    #end game
else:
    #wrong letter entered(no death)
    mistakes+=1



