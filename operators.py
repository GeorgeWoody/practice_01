from main import main_menu

def mat_func():
    print("Has entrado en Suma")
    num01 = int(input("Ingrese el primer número: "))
    num02 = int(input("Ingrese el segundo número: "))
    res = num01 + num02
    print("El resultado es: ", res)
    print("Presione 0 si desea volver al menu anterior")
    opc_op = int(input("Ingrese su opción: "))
    if opc_op == 0:
        main_menu
    else:
        print("NADA")
        
def rest_func():
    print("Has entrado en Resta")
    num01 = int(input("Ingrese el primer número: "))
    num02 = int(input("Ingrese el segundo número: "))
    res = num01 - num02
    print("El resultado es: ", res)
    
def mult_func():
    print("Has entrado en Multiplicacion")
    num01 = int(input("Ingrese el primer número: "))
    num02 = int(input("Ingrese el segundo número: "))
    res = num01 * num02
    print("El resultado es: ", res)
    
def div_func():
    print("Has entrado en Division")
    num01 = int(input("Ingrese el primer número: "))
    num02 = int(input("Ingrese el segundo número: "))
    res = num01 / num02
    print("El resultado es: ", res)