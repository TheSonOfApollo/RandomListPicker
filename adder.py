# Picker de personaje de Valorant 

import random

contador = 0 
seguir = True
seguir2 = True
terminate = False
listnumber = 0 

mainlist = []

def escoger():
    global contador
    while contador < numpersonajes:
        contador = contador + 1
        print(random.choice(mainlist))


while terminate == False:
    print("\nWelcome to the ramdom list picker!")
    print("These are your options: ")
    print("\n1: Choose from an existing list")
    print("2: Make a new list")
    print("3: Exit")
    menuopt = int(input("Option: "))
    if menuopt == 1: 
        numpersonajes = int(input("\nWrite the number of items you wish to randomly select: "))
        decision = input("Do you wish to skip any of the items in the list? Y / N: ").upper()
        if decision == "Y":
            while seguir == True:
                print(*mainlist)
                borrar = input("\nWrite the item you wish to remove: ").upper()
                mainlist.remove(borrar)
                print(*mainlist)
                decision2 = input("Do you wish to remove another item? Y / N: ").upper()
                if decision2 == "Y":
                    continue
                elif decision2 == "N":
                    seguir = False
                else:
                    print("Invalid answer, try again!")
        elif decision == "N":
            pass
        else: 
            print("Invalid answer, try again!")
        print("\n")
        escoger()
        print("\n")
    elif menuopt == 2: 
        while seguir2 == True: 
            mainlist.append(input("Item to add to new list: ").upper())
            print(*mainlist)
            decision3 = input("Do you wish to add another item to the list? Y / N: ").upper()
            if decision3 == "Y":
                continue
            elif decision3 == "N":
                seguir2 = False
            else: 
                print("Invalid choice, try again!")
    elif menuopt == 3: 
        print("Terminating programm ...")
        terminate = True
    else: 
        print("Invalid command, try again!")

        
            
    



















