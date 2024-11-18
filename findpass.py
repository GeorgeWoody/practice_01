def find_pass():
    key_word = 'clave123'
    for i in range(3):
        user_key_word = input("Input Key Word (Only 3 Tries): ")
        if key_word == user_key_word:
            print("Keyword 'clave123' Found")
            return
        else:
            attempts_left = 2 - i
            if attempts_left > 0:
                print(attempts_left," Attempts Left")
            else:
                print("Have No Attempts Left")

find_pass()


"""
Escribe un programa que le pida al usuario ingresar una contraseña y le permita tres intentos 
para adivinar la contraseña correcta (predefinida en el programa). Usa un bucle while con 
condicionales para verificar si la contraseña es correcta y limitar el número de intentos.

    Ejemplo: Si la contraseña es clave123, el programa debería permitir tres intentos y mostrar 
    un mensaje diferente si el usuario acierta o se queda sin intentos.
"""

### HINTS
""" No es posible iterar sobre un int. Los iterables son objetos que pueden recorrerse elemento por elemento,
    como listas, cadenas y rangos. Un (int) no tiene esa capacidad. Para iterar "X veces", usas range(X):                                 
        for i in range(3):
            # código
    range(3) genera una secuencia de números (0, 1, 2), que son tres iteraciones. Así controlas las veces que 
    corre el bucle en un iterable."""


""" FIRST ATTEMPT
def find_pass():
    key_word = 'clave123'

    for i in range(3):
        user_key_word = input("Input Key Word (Only 3 Tries): ")
        if key_word == user_key_word:
            print("Keyword 'clave123' Found")
            return
        else:
            print("Try Again, 3 Tries Left")

        if i in range(3) == 2:
            break
"""

"""SECOND ATTEMPT
def find_pass():
    key_word = 'clave123'
    for i in range(3):
        user_key_word = input("Input Key Word (Only 3 Tries): ")
        if key_word == user_key_word:
            print("Keyword 'clave123' Found")
            return
        elif 3-i-1 == 2:
            print("Try Again, ", 3-i-1,  "Tries Left")

        elif 3-i-1 == 1:
            print("Try Again, ", 3 - i - 1, "Tries Left")

        else:
            print("No tienes mas intentos")

find_pass()
"""