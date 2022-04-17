# Picker de personaje de Valorant 

import random
from subprocess import list2cmdline

contador = 0 
seguir = True
seguir2 = True
terminate = False
listnumber = 0 

personajes = ["ASTRA",
 "BREACH", 
 "BRIMSTONE", 
 "CHAMBER", 
 "CYPHER", 
 "JETT", 
 "KAYO", 
 "KILLJOY", 
 "NEON", 
 "OMEN", 
 "PHOENIX", 
 "RAZE", 
 "REYNA",
 "SAGE", 
 "SKYE", 
 "SOVA", 
 "VIPER", 
 "YORU"]

newlist = []


def escoger():
    global contador
    while contador < numpersonajes:
        contador = contador + 1
        print(random.choice(personajes))



while terminate == False:
    print("\nWelcome to the ramdom list picker!")
    print("These are your options: ")
    print("\n1: Choose from an existing list")
    print("2: Make a new list")
    print("3: Exit")
    menuopt = int(input("Option: "))
    if menuopt == 1: 
        numpersonajes = int(input("\nEscriba la cantidad de personajes que desea escoger: "))
        decision = input("Desea omitir a algun personaje Y / N: ").upper()
        if decision == "Y":
            while seguir == True:
                print(*personajes)
                borrar = input("\nEscriba el nombre del personje que desea omitir: ").upper()
                personajes.remove(borrar)
                print(*personajes)
                decision2 = input("Desea borrar otro personaje de la lista Y / N: ").upper()
                if decision2 == "Y":
                    continue
                elif decision2 == "N":
                    seguir = False
                else:
                    print("Decision invalida, intente de nuevo!")
        elif decision == "N":
            pass
        else: 
            print("Decision invalida, intente de nuevo!")
        print("\n")
        escoger()
        print("\n")
    elif menuopt == 2: 
        while seguir2 == True: 
            newlist.append(input("Item to add to new list: ").upper())
            print(*newlist)
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

        
            
    



















