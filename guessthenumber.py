
'''
guessthenumber.PY: Beskrivning av fil/program 

jag anser att mitt projekt är nära A nivå. 

__author__  = "Sam Rindö"
__version__ = "1.0.0"
__email__   = "sam.rindo@elev.ga.dbgy.se"
'''
import random
import subprocess
from bcolors import bcolors



while True:

    subprocess.run("cls", shell=True)

    print(f"{bcolors.CYAN} {bcolors.UNDERLINE}welcome to guess the number game!{bcolors.DEFAULT}")

    random_number = random.randint(1, 100)
    tries = 7

    print(f"guess a number between 1 and 100 (0=quit)")

    while tries > 0:

        try:
             guess = int(input(f"your guess: "))
        except ValueError:
            print(f"{bcolors.RED}only whole numbers are allowed, try again{bcolors.DEFAULT}")
            continue
        
        if guess == 0: 
            print(f"round cancelled, number was {random_number}")
            break
        
        if guess < random_number:
            tries -= 1
            if tries > 0:
                print(f"{bcolors.BLUE}too low, you have {tries} tries left{bcolors.DEFAULT}")

        elif guess > random_number:
            tries -= 1
            if tries > 0:
                print(f"{bcolors.YELLOW}too high, you have {tries} tries left{bcolors.DEFAULT}")

        else:
            print(f"{bcolors.GREEN}you guessed the number {random_number} correctly!  you had {tries}/7 tries left!{bcolors.DEFAULT}")
            break

    else:
        print(f"{bcolors.RED}you have no tries left, the number was {random_number}{bcolors.DEFAULT}")
        
    while True:
        again = input(f"play again? (Y/N): ")
        
        if again.upper() == "Y": 
            break
        
        elif again.upper() == "N":
            print(f"Thanks for playing!")
            exit()
        
        else: 
            print(f"type Y or N") 