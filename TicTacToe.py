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
    if list[n-1] == 'X' or 'O':
        print("Cell already occupied")
    else:
        list[n-1] = ply

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
    while list[n-1] == 'X' or 'O':
        n = random.randrange(0,8)
    return n

comp = ''
Player1 = input("Select either 'X' or 'O': ")
if Player1 == 'X':
    comp = 'O'
else:
    comp = 'X'  
display()

choice = input("Select a number: ")
printing(choice, Player1)
comp_choice = random_choice()
printing(comp_choice, comp)
display()
winner()
