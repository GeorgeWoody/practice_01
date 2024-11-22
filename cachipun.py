import random


def cachipun():
    options = ['piedra', 'papel', 'tijera']
    rules = {
        'piedra': 'tijera',
        'tijera': 'papel',
        'papel': 'piedra',
    }
    user_wins = 0
    cpu_wins = 0
    ties = 0
    rounds = 0

    print("Bienvenido al Ca Chi Pun")

    while True:
        print("Tienes 3 Opciones: Piedra, Papel o Tijera")

        user_choice = input("Ingrese Su Opción:\n ").lower()

        if user_choice == 'q':
            print("Saliste del Juego")
            break
        if user_choice not in options:
            print("Selección Incorrecta")
            continue

        cpu_choice = random.choice(options)

        if user_choice == cpu_choice:
            print(f"Tu: {user_choice}\nCPU:{cpu_choice}.\nHas Empatado\n")
            ties = ties + 1
        elif cpu_choice == rules[user_choice]:
            print(f" Tu: {user_choice}\nCPU: {cpu_choice}.\nHas Ganado\n")
            user_wins = user_wins + 1
        else:
            print(f"Tu: {user_choice}, CPU: {cpu_choice}.\nHas Perdido\n")
            cpu_wins = cpu_wins + 1

        rounds = rounds + 1

        print(f"\nPartidas Ganadas por el Usuario: {user_wins}")
        print(f"Partidas Ganadas por la CPU: , {cpu_wins}")
        print(f"Empates: {ties}")
        print(f"Rondas: {rounds}")

        if user_wins > cpu_wins:
            print("Ganaste El Juego")
        elif user_wins == cpu_wins:
            print("Has Empatado el Juego, Intentalo en otra Oportunidad")
        else:
            print("Lo Siento, Perdiste el Juego :( ")



cachipun()
