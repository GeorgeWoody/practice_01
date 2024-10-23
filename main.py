from operators import mat_func, rest_func, mult_func, div_func

print("Selecciona la operacion que deseas")
print("Presiona 1 para Sumar")
print("Presiona 2 para Restar")
print("Presiona 3 para Dividir")
print("Presiona 4 para Multiplicar")
print("Presiona cualquier tecla para salir")

opc = int(input("Seleciona tu opcion: "))

if opc == 1:
    print("Has seleccionado Suma")
    mat_func()

elif opc == 2:
    print("Has seleccionado Resta")
    rest_func()

elif opc == 3:
    print("Has seleccionado Multiplicacion")
    mult_func()
elif opc == 4:
    print("Has seleccionado Division")
    div_func()
    
else:
    print("Has Salido")

