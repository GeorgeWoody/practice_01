import os

os.system('cls' if os.name =='nt' else 'clear')

print("*"*100)
print("-"*100)
print("*"*20+"HAS INGRESADO A MI CALCULADORA SENCILLA"+"*"*20)
print("*"*20+"EN ESTA CALCULADORA DEBES INGRESAR '2' NÚMEROS\n"+"*"*20+"Y SELECCIONAR LA OPERACIÓN QUE QUIERES REALIZAR"+"*"*20)
print("*"*100)
print("*"*100)


while True:
    num01 = int(input(" "*5+"Ingresa el Primer Número: "))
    num02 = int(input(" "*5+"Ingrese el Segundo Número: "))

    print("Presione + para Sumar")
    print("Presione - para Restar")
    print("Presione * para Multiplicar")
    print("Presione / para Dividir")
    oper = input("#"*5+" "*5+"¿Que Operacion Desea Realizar?"+" "*5+"#"*5)
    
    res = 0
    if oper == '+':
        res = num01 + num02
        
    elif oper == '-':
        res = num01 - num02

    elif oper == '*':
            res = num01 * num02
            
    else:
        res = num01 / num02
        
    print("El resultado es: ", res)