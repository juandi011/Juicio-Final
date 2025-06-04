import time
from cielo import cielo
from infierno import infierno
from purgatorio import purgatorio

#JUICIO FINAL pre-Alpha

PECADO = 0.6 #0 = CIELO, 1 = INFIERNO, entre 0 y 1 = PURGATORIO
i = 1
respuesta = ""

print("Bienvenido a tu Juicio Final")
print()
print("Espere mientras analizamos su nivel de pecado")

while i<5:
    print(".")
    time.sleep(2)
    i=i+1

if PECADO == 0: #CIELO
    cielo()

if PECADO > 0: #JUICIO
    print("HAS LLEGADO CON MANCHA A TU JUICIO FINAL")
    respuesta = input("¿Te arrepientes de tus pecados? (si/no): ")
    if respuesta.lower() == "si":
        #Aunque uno se arrepienta, puede seguir teniendo pecado
        if PECADO - 0.5 < 0: #Si el pecado que queda es menor de 0.5, se perdona
            print("DIOS ES MISERICORDIOSO")
            print("TUS PECADOS HAN SIDO PERDONADOS")
            cielo()
        else: #Aún queda pecado
            purgatorio()

    else:
        infierno()               
