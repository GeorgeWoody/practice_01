import random

def hangman():

    print("Bienvenido al AHORCADO")
    print("     i----I")
    print("     i    I")
    print("     O    I")
    print("    /I\   I")
    print("   / I \  I")
    print("    / \   I")
    print("   /   \  I")
    print("----------I")

    WORDS = [
        "perro", "gato", "casa", "arbol", "coche", "lapiz", "papel", "libro", "mesa", "silla",
        "flor", "sol", "luna", "estrella", "cielo", "mar", "rio", "pez", "ave", "nube",
        "niño", "niña", "tierra", "fuego", "viento", "agua", "puerta", "ventana", "reloj", "camino",
        "rojo", "verde", "azul", "negro", "blanco", "amarillo", "morado", "naranja", "gris", "rosa",
        "manzana", "pera", "uva", "pluma", "pan", "queso", "carro", "tren", "camion", "bici"
    ]

    selected_word = random.choice(WORDS)
    print(selected_word)
    hidden_word = ['_' for _ in selected_word]
    print(" ".join(hidden_word))






hangman()