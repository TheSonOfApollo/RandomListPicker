# Trenzador 


R = "R"
G = "G"
B = "B"

colores = [R,G,B]

sec1 = [2,0,1]

contador = 0

def trenzar():
    global colores
    colores = [colores[i] for i in sec1]
    print(*colores)
 

print(*colores)
while contador < 20:
    contador = contador + 1
    trenzar()

