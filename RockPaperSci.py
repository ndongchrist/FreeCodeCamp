import random

def Computer_choice():
    list = ['r','p','s']
    a = random.randrange(0,2)
    return list[a]

def compare(ply, Cpt):
    if ply == Cpt:
        return "Draw, No winner"
    elif ply == 'p' and Cpt == 'r':
        return "Player 1 wins"
    elif ply == 'p' and Cpt == 's':
        return "Computer wins"
    elif ply == 'r' and Cpt == 'p':
        return "Computer wins"
    elif ply == 'r' and Cpt == 's':
        return "Player 1 wins"  
    elif ply == 's' and Cpt == 'r':
        return "computer wins"  
    elif ply == 's' and Cpt == 'p':
        return "Player 1 wins"

count = 0
while count != 3:
    count += 1
    p = input("Enter an Option: r:rock, p:paper, s:scissor -->")
    print(f"you: {p}")
    comp = Computer_choice()
    print(f'computer: {comp}')
    a = compare(p, comp)
    print(a)
    
