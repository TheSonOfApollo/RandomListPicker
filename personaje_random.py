# Picker de personaje de Valorant 

import random

contador = 0 
seguir = True


personajes = ["ASTRA",
 "BREACH", 
 "BRIMSTONE", 
 "CHAMBER", 
 "CYPHER", 
 "FADE",
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


def escoger():
    global contador
    while contador < numpersonajes:
        contador = contador + 1
        print(random.choice(personajes))

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



