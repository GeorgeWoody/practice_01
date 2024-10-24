from operators import sum_func, rest_func, mult_func, div_func
from calc import complex_calc
from algorithms import search_max_number, search_max_number_parameter
def main_menu():
    while True:    
        print("***Selecciona la operacion que deseas***")
        print("*.* Presiona 1 Para SUMAR")
        print("*.* Presiona 2 Para RESTAR")
        print("*.* Presiona 3 Para MULTIPLICAR")
        print("*.* Presiona 4 Para DIVIDIR")
        print("*.* Presiona 5 Para FUNCIÓN CALCULADORA COMPLEJA")
        print("*.* Presiona 6 Para BUSCA EL NUMERO MAYOR (algoritmo simple)")
        print("*.* Presiona 7 Para BUSCA EL NUMERO MAYOR (con parametros)")
        #print("*.* Presiona # Para BUSCA EL NUMERO MAYOR")
        print("--------------------------------------------------------")
        print("*** Presiona 0 Para SALIR ***")

        try:
            opc = int(input("Seleciona Tu Opción: "))
        except ValueError:
            print("Opcion No Válida, Ingresa Un Número Entero")
            
        if opc == 0:
            print("Saliendo......")
            break
        
        if opc == 1:
            print("Has seleccionado SUMA")
            sum_func()

        elif opc == 2:
            print("Has seleccionado RESTA")
            rest_func()

        elif opc == 3:
            print("Has seleccionado MULTIPLICACIÓN")
            mult_func()
        
        elif opc == 4:
            print("Has seleccionado DIVISIÓN")
            div_func()
            
        elif opc == 5:
            print("FUNCIÓN CALCULADORA COMPLEJA")
            complex_calc()
            
        elif opc == 6:
            #print("ALGORÍTMOS")
            search_max_number()
            
        elif opc == 7:
            #print("ALGORÍTMOS")
            list_param = [6,9,4,10]
            res = search_max_number_parameter(list_param)
            print("El NUMERO MAYOR ES: ", res)
        
        else:
            print("No Has Seleccionado Un Número, Vuelve A Seleccionar")


if __name__ == "__main__":
    main_menu()