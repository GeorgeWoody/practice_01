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
    print("Tienes 3 Opciones: Piedra, Papel o Tijera")

    while True:
        user_choice = input("Ingrese Su Opción:\n ").lower()

        if user_choice == 'q':
            print("Saliste del Juego")
            break
        if user_choice not in options:
            print("Selección Incorrecta")
            continue

        cpu_choice = random.choice(options)

        if user_choice == cpu_choice:
            print("Has Empatado")
            ties = ties + 1
        elif cpu_choice == rules[user_choice]:
            print("Has Ganado")
            cpu_wins = cpu_wins + 1
        else:
            print("Has Ganado")
            user_wins = user_wins + 1


cachipun()