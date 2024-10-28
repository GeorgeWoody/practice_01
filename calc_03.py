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
    
def calculator():

    while True:

        num01 = float(input("Ingrese un número: "))

        try:
            operator = input("Ingrese la operación a realizar, o presione 'q' para salir: ")
        except ValueError:
            print("Operador no valido") 

        if operator.lower() == 'q':
            print("Has salido...")
            break
        
        num02 = float(input("Ingrese un número: "))

        if operator in operators:
            res = operators[operator](num01, num02)

            print("El resultado es: ", res)
        else:
            print("El operador no es valido, intente de nuevo")

calculator()
    
    
    
    
    
    #if operator == '+' or operator == '-' or operator == '*' or operator == '/':    
    #    num = int(input("Ingrese Numero"))
        
        