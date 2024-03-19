import random
import os

# Función para lanzar dos dados
def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

# Función para validar la entrada del número de jugadores
def solicitar_numero_jugadores():
    while True:
        try:
            num_jugadores = int(input("Ingrese la cantidad de jugadores (entre 2 y 4): "))
            if 2 <= num_jugadores <= 4:
                return num_jugadores
            else:
                print("Por favor ingrese un número válido de jugadores.")
        except ValueError:
            print("Por favor ingrese un número válido.")

# Función para solicitar el nivel de tablero
def solicitar_nivel_tablero():
    while True:
        try:
            os.system('clear')  # Limpiar pantalla del sistema
            print("Seleccione el nivel de tablero a jugar:")
            print("1. Nivel básico (Tablero de 20 posiciones)")
            print("2. Nivel intermedio (Tablero de 30 posiciones)")
            print("3. Nivel avanzado (Tablero de 50 posiciones)")
            print("4. Nivel experto (Tablero de 100 posiciones)")
            nivel = int(input("Ingrese el número correspondiente al nivel: "))
            if 1 <= nivel <= 4:
                return nivel
            else:
                print("Por favor ingrese un nivel válido.")
        except ValueError:
            print("Por favor ingrese un número válido.")

# Función principal para simular el juego
def carrera_numerica():
    num_jugadores = solicitar_numero_jugadores()
    nivel_tablero = solicitar_nivel_tablero()
    meta = {1: 20, 2: 30, 3: 50, 4: 100}
    posiciones_jugadores = [0] * num_jugadores
    os.system('clear')
    pares_consecutivos_jugadores = [0] * num_jugadores

    while True:
        for i in range(num_jugadores):
            print(f"\nTurno del jugador {i + 1}:")
            input("Presiona Enter para lanzar los dados...")
            dado1, dado2 = lanzar_dados()
            print(f"Has sacado {dado1} y {dado2}.")
            avance = dado1 + dado2
            posiciones_jugadores[i] += avance
            print(f"Avanzas {avance} posiciones.")

            # Verificar si se sacó un par
            if dado1 == dado2:
                pares_consecutivos_jugadores[i] += 1
                print("¡Felicidades! Has sacado un par.")
            else:
                pares_consecutivos_jugadores[i] = 0
            
            # Verificar si el jugador ha acumulado 3 pares consecutivos en 3 turnos
            if pares_consecutivos_jugadores[i] == 3:
                print(f"¡Felicidades! El jugador {i + 1} ha ganado con tres pares consecutivos en tres turnos.")
                return

            print(f"Ahora estás en la posición {posiciones_jugadores[i]}.")

            if posiciones_jugadores[i] >= meta[nivel_tablero]:
                print(f"¡Felicidades! El jugador {i + 1} ha llegado a la meta.")
                return

# Llamada a la función principal
carrera_numerica()
