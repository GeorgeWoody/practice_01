import random

def hangman():

    print("Bienvenido al AHORCADO")
    print("     i----I")
    print("     i    I")
    print("     O    I")
    print("    /I\   I")
    print("   / I \  I")
    print("    / \   I")
    print("   /   \  I")
    print("----------I")

    WORDS = [
        "perro", "gato", "casa", "arbol", "coche", "lapiz", "papel", "libro", "mesa", "silla",
        "flor", "sol", "luna", "estrella", "cielo", "mar", "rio", "pez", "ave", "nube",
        "niño", "niña", "tierra", "fuego", "viento", "agua", "puerta", "ventana", "reloj", "camino",
        "rojo", "verde", "azul", "negro", "blanco", "amarillo", "morado", "naranja", "gris", "rosa",
        "manzana", "pera", "uva", "pluma", "pan", "queso", "carro", "tren", "camion", "bici"
    ]

    selected_word = random.choice(WORDS)
    print(selected_word)
    hidden_word = ['_' for _ in selected_word]
    print(" ".join(hidden_word))


#hangman()


def test_sets():
    guessed_letter = set()
    while True:
        user_input = input("Input Letter: ")
        if user_input != 1 and user_input.isalpha():


        if user_input in guessed_letter:
            print("Letter Exist")
        else:
            guessed_letter.add(user_input)
            print("Letter Dont Exist")



test_sets()



""" ChatGPT Conversación
CHAT: Preguntas Clave
      ¿Hay algo que no quede claro de este proceso? ¿Te gustaría una explicación más detallada de algún punto específico? 😊

Me: Me queda claro, lo que si es que ese tipo de usabilidad de ciertas herramientas no son claras en mi todavía, 
    ademas de saber cuando y como utilizarlas en momentos específicos

CHAT: Es completamente normal que al principio cueste identificar qué herramientas usar y cómo aplicarlas en el contexto adecuado. Es parte del proceso de aprendizaje en programación. Voy a darte algunos consejos prácticos para mejorar en este aspecto:
    
    1. Familiarízate con las herramientas básicas
    
    Antes de intentar combinaciones complejas, dedica tiempo a practicar herramientas comunes de Python y entender cómo funcionan por separado. Por ejemplo:
    
        Listas y sus operaciones básicas (append, remove, slicing, etc.).
        Métodos de cadenas como .join(), .split(), .replace(), etc.
        Comprehensions para listas y diccionarios.
        Estructuras de control (for, if, etc.).
    
    Con ejercicios simples, puedes explorar cómo funcionan estas herramientas.
    2. Reconoce patrones comunes
    
    En muchos problemas, los programadores enfrentan retos similares una y otra vez. Al resolver ejercicios o analizar ejemplos, presta atención a patrones como:
    
        Generar una lista o cadena basada en otra estructura (como en el caso de hidden_word).
        Filtrar elementos (por ejemplo, seleccionar solo números pares de una lista).
        Transformar datos de un formato a otro (por ejemplo, listas a cadenas y viceversa).
    
    Cuanto más practiques, más naturales serán estas asociaciones.
    3. Piensa en pasos lógicos
    
    Antes de codificar, desglosa el problema:
    
        ¿Qué necesito? En el caso del ahorcado, necesitas representar las letras ocultas.
        ¿Cómo lo represento? Aquí decides usar una lista de guiones bajos.
        ¿Cómo lo muestro? Aquí es donde aparece el uso de .join().
    
    Hacer este análisis paso a paso reduce la sensación de estar improvisando y facilita seleccionar las herramientas adecuadas.
    4. Prueba y error
    
    Experimenta y observa cómo se comporta el código:
    
        ¿Qué pasa si imprimes la lista directamente?
        ¿Qué sucede si cambias el separador de .join()?
        ¿Qué ocurre si usas otro tipo de comprensión de lista?
    
    Este enfoque te ayuda a interiorizar no solo qué hace una herramienta, sino también por qué y cómo se adapta al contexto.
    5. Resuelve problemas similares
    
    Para mejorar, practica problemas pequeños que requieran el uso de herramientas específicas:
    
        Generar patrones visuales (como _ _ _ _ _).
        Transformar datos (como convertir "12345" en [1, 2, 3, 4, 5]).
        Manipular listas y cadenas en formas útiles.
    
    Puedes intentar desafíos pequeños, como escribir un programa que:
    
        Cambie todas las vocales de una palabra por guiones bajos.
        Combine dos listas de números alternando sus elementos.
    
    6. Sé paciente
    
    Identificar herramientas y usarlas en el momento correcto es una habilidad que se desarrolla con tiempo y práctica. Lo importante es que sigas trabajando en resolver problemas, aunque sientas que aún no es "natural". Con cada ejercicio, estarás un paso más cerca de dominarlo.
    
    

"""








