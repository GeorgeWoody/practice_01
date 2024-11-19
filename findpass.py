def find_pass():
    key_word = 'clave123'
    for i in range(3): # (1)
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
""" (1) No es posible iterar sobre un int. Los iterables son objetos que pueden recorrerse elemento por elemento,
    como listas, cadenas y rangos. Un (int) no tiene esa capacidad. Para iterar "X veces", usas range(X):                                 
        for i in range(3):
            # código
    range(3) genera una secuencia de números (0, 1, 2), que son tres iteraciones. Así controlas las veces que 
    corre el bucle en un iterable."""

### EXPLICACIÓN
""" A raíz de que la lógica practicamente me la dio CHATGPT, procedo a da la explicación de lo que entiendo del código.
    El motivo es para no olvidar cual es la lógica en que trababa este código.
    
    key_word = 'clave123' ### Inmediatamente despuúes de declarar la función, declaramos en una variable la palabra clave secreta.
    
    for i in range(3):  ### Para validar que el programa solo te de 3 intentos solamente, declaramos un 'for' en rango de 3 (range(3))
                        ### Al declarar un range(3) dentro del bucle, i dara 3 vueltas comenzando desde 0 hasta el 2.
        user_key_word = input("Input Key Word (Only 3 Tries): ")
        if key_word == user_key_word:   ### Se declara inmediatamente que si lo ingresado por el usuario es correcto, se valide
            print("Keyword 'clave123' Found") ### y el programa envíe un mensaje y termine con 'return'
            return
        else:   ### Sino coincide lo ingresado por el usuario...
            attempts_left = 2 - i   ### Se crea una variable de intentos restantes. Como al usuario se le avisa que solo tiene 3 intentos,
                                    ### el 1er intento ya se descuenta. Como el 'for' va en la primera vuelta e 'i' equivale a 0,
                                    ### lo guardado en intentos restantes es el resultado de 2 - 0, lo que es igual a 2.
                
                
                if attempts_left > 0: ### En el condicional se valida si intentos restantes es mayor 0, que lo es, porque 'i' vale 2... 
                print(attempts_left," Attempts Left") ### Se imprime el valor 2
            
                                    ### Ahora en la segunda vuelta, 'i' valdra 1, como intentos restantes vale 2, en la 2da vuelta valdra la
                                    ### 2 - i, y sabiendo que en la 2da vuelta i vale 1, se resta, e intentos restantes valdra 1
                                    
                                    ### En la tercera vuelta i valdra 2, como intentos restantes vale 2 en la resta dara 0,
                                    ### por lo cual la condición de intentos restantes > a 0 no será True, y pasará al else,
                                    ### e imrpimirá "No tienes intentos restantes y el bucle for termina.
            else:
                print("Have No Attempts Left") """