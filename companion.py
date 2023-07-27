
import webbrowser
import random

Terminate = False
needanotherreason = True
needanothermovie  = True 

reasonstolive = [
    "https://www.youtube.com/watch?v=ull52nptr3U", 
    "https://www.youtube.com/watch?v=PppkNH3bKV4",
    "https://www.youtube.com/watch?v=ur48jVNNlKk",
    "https://www.youtube.com/watch?v=tYzMYcUty6s" 
]

conformovies = [ 
    "WALL-E", 
    "Charlie and the chocolate factory", 
    "Spy", 
]

def reasonpicker(): 
    global needanotherreason
    while needanotherreason == True:
        reason = random.choice(reasonstolive)
        webbrowser.open_new(reason)
        anotherreason = input("Would you like to see another reason? Y/N \n").upper()
        if anotherreason == "Y":
            continue
        
        elif anotherreason == "N":
            needanotherreason = False
            
        else: 
            print("Invalid answer, try again!")
            break
        
def moviepicker(): 
    global needanothermovie
    while needanothermovie == True: 
        movie = random.choice(conformovies)
        print("You should watch: " + movie)
        anothermovie = input("Do you want to watch that movie? Y/N \n").upper()
        if anothermovie == "Y":
            needanothermovie = False
            
        elif anothermovie == "N":
            continue
        
        else: 
            print("Invalid answer, try again!")
            break
            
        


print("\n \nWelcome to the COMPANION ONE a creation made possible by Gord-O.S.")
print("COMPANION ONE can be your frined when you feel lonely.")
print("If at any time you want to interrupt the programm just type in: zzz ")

while Terminate == False: 
    openingquestion = input("Would you like a friend: Y/N \n").upper()

    if openingquestion == "ZZZ":
        print("Terminating . . .  \n \n")
        Terminate = True 
   
    elif openingquestion == "Y":
        print("Awesome!")
        q1 = input("Would you like to watch a movie? Y/N \n").upper()
        if q1 == "Y": 
            moviepicker()
            
        elif q1 == "N": 
            q2 = input("That's ok, would you like to eat something then? Y/N \n").upper()
            
        else:
             print("Invalid answer, try again!")
            
        

    elif openingquestion == "N":
        print("I'll be here anyway if you need anything. \n I know something that could make you feel better")
        q3 = input("Would you like to try? Y/N \n").upper()
        if q3 == "Y":
            reasonpicker()
            
        elif q3 == "N":
            print("Its ok,  we can try another thing")
            
        else: 
            print("Invalid answer, try again!")
        
    else:
        print("Invalid answer, try again!")
            
            