'''
Scripts description numbre race
dev: halier rojas
date 13/08/2024
'''

from random import randint
import os

status_game = True


def main_menu():
    global status_opts
    status_opts = True 
        
    print(":::main menu :::")
    print ("[1]. Star Game")
    print ("[2]. Help")
    print ("[3]. Exit")
    
    while status_opts:
        opt = int(input("Press any option:"))
        if opt < 1 or opt > 3:
            print("error. press any option between 1 and 3")
        else:
            status_opts = False  
    return opt  

while status_game:
    os.system('clear')
    op= main_menu()
    if op == 1:
        os.system('clear')
        print("welcome to number race")   
        key= input("Press any key to go to the main menu ..")
    elif op == 2:
        print("Help under construction")
        key= input("press any key to go to the main menu...")
    else:
        print("see you")
        key = input("press any key to exit...")
        break
            
    
'''
dice1 = randint(1,6)
dice2 = randint(1,6)

print(f"Dice 1:{dice1}")
print(f"Dice 2:{dice2}")
'''