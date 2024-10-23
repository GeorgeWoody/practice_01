
def mat_func():
    while True:
        print("Has entrado en Suma")
        try:
            num01 = int(input("Ingrese el primer número: "))
            num02 = int(input("Ingrese el segundo número: "))
        except ValueError:
            print("Has ingresado un valor que no es entero")
            continue
        
        res = num01 + num02
        print("El resultado es: ", res)
        
        opc_menu = int(input("Presione 0 si desea volver al menu anterior"))
        if opc_menu == 0:
            break    
             

def rest_func():
    while True:
        print("Has entrado en Resta")
        try:
            num01 = int(input("Ingrese el primer número: "))
            num02 = int(input("Ingrese el segundo número: "))
        except ValueError:
            print("Has ingresado que no es 'ENTERO")
            continue
        
        res = num01 - num02
        print("El resultado es: ", res)
    
        opc_menu = int(input("Presione 0 si desea volver al menu anterior"))
        if opc_menu == 0:
            break
        
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