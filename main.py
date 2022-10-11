import random
from re import M
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
print(title)
word = get_word()
for i in range(len(word)-1):
    print("_" + str(i)+ " ", end="")
print('')
print(word)
input = input("Enter a leter: ")
if(input.upper() in (word.upper())):
    yes = "Correct"
    print(yes)
#def function1():
#