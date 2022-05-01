def counter(n): #counts the number of spaces for arranging the spaces between
    if len(n) == 1:
        return ('   '+ n)
    elif len(n) == 2:
        return ('  '+ n)
    elif len(n) == 3:
        return(' ' + n)
    elif len(n) == 4:
        return (n)
    else:
        n = None
        return 'Invalid'    
       

def placer(element, answer = None):#for arranging the operations in vertical order
    #I create a new list by spliting the element
    new_e = element.split(" ")

    print(f" {counter(new_e[0])}")
    print(f"{new_e[1]}{counter(new_e[2])}")
    print('-'*7)


def arithmetic_arranger(operation, answer = None):#Creating a list() for storing operations
    
    for i in range(len(operation)):
        item = operation[i]
        placer(item)
        new_e = item.split(" ")
        if new_e[1] == '*' or new_e[1] == '/':
            print("Error: Opertor must be '+' or '-'.")
            break
        if answer == True:
            new_e1 = int(new_e[0])
        new_e2 = int(new_e[2])
        if new_e[1] == '+':
            print(f' {new_e1 + new_e2}')
        elif new_e[1] == '-':
            print(f' {new_e1 - new_e2}') 
        elif len(new_e[0]) == 5 and new_e[2] == 5:
            return("Error: Numbers cannot be more than four digits.")
            break

            

arithmetic_arranger(['9356 + 7455', '60000 + 7','9356 + 7455', '6000 - 7','9356 + 7455'], True)
