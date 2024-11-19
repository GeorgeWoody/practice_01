import random

def guess_number():
    random_number = random.randint(1,100)

    while True: ### Dejamos que el usuario ingrese cualquier tipo de caracter...
        user_input = input("Guess The Secret Number, Between 1 And 100 (press 'q' to quit): ")  ### esto con el fin de poder valor 'q'
                                                                                                ### como valor de salida del programa

        if user_input == 'q': ### Si es 'q', el programa termina
            print("Exiting...")
            return            ### con 'return'. Sino

        user_int = int(user_input) ### Se valida lo ingresado por el usuario con un entero

        if user_int < random_number:    ### Y comenzamos la validación de las condiciones hasta encontrar el numero correcto...
            print("Your Number Is: ",user_int,"Secret Number is Higher, Try Again")
        elif user_int > random_number:
            print("Your Number Is: ",user_int,"Secret Number Is Lower, Try Again")
        else:
            print("You Have Match, Number is ",random_number) 
            break   ### Sino coinciden ninguna de las condiciones anteriores, es porque se encontro el numero 'random'
                    ### y el programa termina la funcion con 'break'
guess_number()