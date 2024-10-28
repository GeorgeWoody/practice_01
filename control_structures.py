def control_flow():
    while True:
        x = int(input("Ingrese un numero cualquiera entre 1 y 100 (no puedes ingresar 0): "))
        print("El numero ingresasdo es: ",x)    
        
        if x == 0 or x > 100:
            print("No puedes ingresar", x, "FIN DEL PROGRAMA")
            break
        
        elif x < 50:
            x2 = x * 2
            print("Tu numero es ", x, "multiplicado por 2 es ", x2)
        
        else:
            x3 = x * 3
            print("Tu numero es ", x, "multiplicado por 3 es ", x3)

def pair_number():
    p = int(input("Ingrese un numero para verificar si es par: "))
    p_res = p % 2
    if p_res == 0:
        print("El numero ",p, "es par")
    else:
        print("El numero ingresado no es par")

