import random

list = ['1','2','3','4','5','6','7','8','9']
play = True

def display():
    
    print(f" {list[0]} | {list[1]} | {list[2]}  ")
    print('---+---+---')
    print(f" {list[3]} | {list[4]} | {list[5]}  ")
    print('---+---+---')
    print(f" {list[6]} | {list[7]} | {list[8]} ")

def printing(n, ply):
        if ply == 'O':
            if list[n-1] != 'O' or 'X':
                list[n-1] = 'O'
            else:
                pass    
        else:
            if list[n-1] != 'O' or 'X':
                list[n-1] = 'X'
            else:
                pass


def winner():
    if list[0] == list[1] == list[2]:
        print(f"player {list[0]} wins")
    elif list[3] == list[4] == list[5]:
        print(f"player {list[3]} wins")
    elif list[6] == list[7] == list[8]:
        print(f"player {list[6]} wins")
    elif list[0] == list[3] == list[6]:
        print(f"player {list[0]} wins")
    elif list[1] == list[4] == list[7]:
        print(f"player {list[1]} wins")
    elif list[2] == list[5] == list[8]:
        print(f"player {list[2]} wins")
    elif list[0] == list[4] == list[8]:
        print(f"player {list[0]} wins")
    elif list[2] == list[4] == list[6]:
        print(f"player {list[2]} wins")
    else:
        pass

    
def random_choice():
    a = 0
    n = len(list)
    for i in range(0, n-1):
        if list[i] == 'X' or 'O':
            

    

    



comp = ''
Player1 = input("Select either 'X' or 'O': ")
if Player1 == 'X':
    comp = 'O'
else:
    comp = 'X'  
display()
count = 0
n = len(list)-1

while count != n:
    choice = int(input("Select a number: "))
    while list[choice - 1] != Player1:
        choice = int(input("Select a number: "))
        printing(choice, Player1)
    display()
    print('computer is choosing')
    comp_choice = random_choice()
    while list[comp_choice-1] != comp:
        comp_choice = random_choice()
        printing(comp_choice, comp)
    display()
    winner()
    count += 1
