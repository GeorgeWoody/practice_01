def sum_func():
    while True: ### Mientras los Valores Ingresados Sean 'int' ###
        try: ### Intentar Validar las Variables Ingresadas como 'int' ###
            num01 = int(input("Ingrese el primer número: "))
            num02 = int(input("Ingrese el segundo número: "))
        except ValueError: ### Si NO son Enteros, imprimir... ###
            print("Has Ingresado Un Valor que NO es 'ENTERO'\nVuelve A Ingresar Un Número")
            continue ### Permite al while True (ciclo infinito)volver al Inicio y pedir que se vuelvan a ingresar los datos correctos ###
        
        res = num01 + num02
        print("El resultado es: ", res)
        
        try:
            opc_menu = (input("***Presione 0 para volver al menu anterior***\n***Presione Cualquier tecla para realizar la misma operacion: ***"))
        except ValueError:
            print("Vuelves a Realizar 'SUMA'")
            continue
        if opc_menu == '0':
            break    
             

def rest_func():
    while True:
        try:
            num01 = int(input("Ingrese el primer número: "))
            num02 = int(input("Ingrese el segundo número: "))
        except ValueError:
            print("Has Ingresado Un Valor que NO es 'ENTERO'\nVuelve A Ingresar Un Número")
            continue
        res = num01 - num02
        print("El resultado es: ", res)
        try:
            opc_menu = (input("***Presione '0' Para Volver Al Menú Anterior***\n***Presione Cualquier Tecla Para Realizar La Misma Operación: " + "***"))
        except ValueError:
            print("Vuelves A Realizar 'RESTA'")
            continue        
        if opc_menu == '0':
            break
        
def mult_func():
    while True:
        try:
            num01 = int(input("Ingrese el primer número: "))
            num02 = int(input("Ingrese el segundo número: "))
        except ValueError:
            print("Has Ingresado Un Valor que NO es 'ENTERO'\nVuelve A Ingresar Un Número")        
        res = num01 * num02
        print("El resultado es: ", res)
        try:
            opc_menu = (input("***Presione '0' Para Volver Al Menú Anterior***\n***Presione Cualquier Tecla Para Realizar La Misma Operación: " + "***"))
        except ValueError:
            print("Vuelves A Realizar MULTIPLICACIÓN")
            continue
        if opc_menu == '0':
            break
            
def div_func():
    while True:
        try:
            num01 = int(input("Ingrese el primer número: "))
            num02 = int(input("Ingrese el segundo número: "))
        except ValueError:
            print("Has Ingresado Un Valor que NO es 'ENTERO'\nVuelve A Ingresar Un Número")        
            continue
        res = num01 / num02
        print("El resultado es: ", res)
        
        try:
            opc_menu = (input("***Presione '0' Para Volver Al Menú Anterior***\n***Presione Cualquier Tecla Para Realizar La Misma Operación: " + "***"))
        except ValueError:
            print("Vuelves A Realizar DIVISIÓN")
            continue
        if opc_menu == '0':
            break