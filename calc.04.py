import os
os.system('cls' if os.name =='nt' else 'clear')


def sum(x,y):
    return x + y
        
def rest(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    if y == 0:
        print("No es posible dividir por 0")
    else:
        return x / y

operators = {
    '+' : sum,
    '-' : rest,
    '*' : mult,
    '/' : div
}


def calculator_02():
    while True:    
        try:
            var_num = float(input("Ingrese un numero: "))
        except ValueError:
            print("Error, Se espera un numero")
            continue   
        
        var_operator = input("Ingrese un operador, '+', '-', '*', '/', presione 'q' para salir: ")      
        if var_operator.lower() == 'q':
            print("Saliendo del programa")
            break
        
        if var_operator in operators:
            saved_operator = operators[var_operator]
            result = saved_operator(var_num, var_num)
            print("Resultado: ", result)
        else:
            print("El operador no es valido")
        
        continue    
        
        var_num = float(input("Ingrese un numero: "))

        
    
        



calculator_02()