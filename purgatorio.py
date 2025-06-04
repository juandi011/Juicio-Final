from cielo import cielo

def purgatorio():
    print("BIENVENIDO AL PURGATORIO")
    print("Aquí purgarás tus pecados antes de alcanzar el Cielo")
    print("Por cada pecado, deberás realizar una penitencia")
    print("Recuerda que el arrepentimiento es clave para tu redención")
    
    # Simulación de penitencias
    penitencias = ["Rezar 10 Ave Marías", "Hacer una obra de caridad", "Ayunar un día", "Confesar tus pecados"]
    
    for penitencia in penitencias:
        print(f"Penitencia: {penitencia}")
        input("Presiona Enter cuando hayas completado la penitencia...")
    
    print("Has completado todas las penitencias. Tu alma está más limpia.")
    print("Ahora puedes ascender al Cielo.")
    cielo()  # Llamada a la función cielo para finalizar el proceso