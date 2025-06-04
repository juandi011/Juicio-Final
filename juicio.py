import time
from cielo import cielo
from infierno import infierno
#JUICIO FINAL V0
#03/06/2025

PECADO = 0 #0 = CIELO, 1 = INFIERNO, entre 0 y 1 = PURGATORIO
i = 0
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
    input("¿Te arrepientes de tus pecados? (si/no): ")
    if respuesta.lower() == "si":
        print("DIOS ES MISERICORDIOSO")
        print("TUS PECADOS HAN SIDO PERDONADOS")
        cielo()
    else:
        print("No se mostrará el nivel de pecado")
    infierno()               