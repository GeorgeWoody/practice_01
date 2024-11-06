def classify():
    num_list = list(map(float, input("Input Positives or Negatives Numeric Values: ").split(',')))

    positives = [] #Se declaran las listas vacías, donde se almacenaran los valores requeridos
    negatives = []
    zeros = []
    for i in num_list: #Se recorren los n°s ingresados; con la condición se discrimina si es positivo o negativo
        if i > 0:
            positives.append(i) #Con el método .append se agrega el valor ya discrimonado positivo o negativo, dentro de la lista correspondiente
        elif i < 0:
            negatives.append(i)
        else:
            zeros.append(i)

    print("Positives: ",positives,"Total: ",len(positives)) #Con la función len() se contabiliza la cantidad de valores (índices) dentro de la lista,
    print("Negatives: ", negatives,"Total: ", len(negatives))
    print("Zero/es: ",len(zeros))
    
    
classify()

"""
-Método .split(',') divide la cadena de entrada en partes separadas por comas. P.Ej. si el usuario ingresó
 "4,5,9,7", la cadena se convierte en una lista de strings: ["4", "5", "9", "7"].

-Función map(int, ...) toma dos argumentos: una función (int) y un iterable (una lista).
 map(int, ["4", "5", "9", "7"]) aplica la función int a cada elemento de la lista, convirtiendo cada 
 string en un número entero.
 El resultado de map() es un iterador que contiene los números enteros: [4, 5, 9, 7].

-Función list(...) convierte el resultado de map() (que es un iterador) en una lista de enteros.
  Resultado final: [4, 5, 9, 7].

-Resumen
    *input() obtiene la entrada del usuario como una cadena.
    *split(',') divide esa cadena en una lista de substrings, separando por comas.
    *map(int, ...) convierte esos substrings en enteros.
    *list(...) convierte el resultado de map() en una lista de enteros.

Ej: Si el usuario ingresa 4,5,9,7, la línea entera hará que:
    *input() obtenga "4,5,9,7",
    *.split(',') la convierta en ["4", "5", "9", "7"],
    *map(int, ...) la transforme en [4, 5, 9, 7],
    *y list(...) retorne [4, 5, 9, 7].
"""