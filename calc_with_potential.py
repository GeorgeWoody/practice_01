def sums(x,y):
    return x+y
def rest(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    if y==0:
        print("Error, Cannot Divide By 0")
        return None
    else:
        return x/y
    
def pot

operators = {
    '+':sums,
    '-':rest,
    '*':mult,
    '/':div
}

def calc():

    while True:
        try:
            var_num = int(input("Input Number: "))
        except ValueError:
            print("Error, Not A Numeric Value, Try Again")
            continue

        while True: ### Solo necesito el 'while True' y no try except, ya que no necesito validar un tipo especifico de
            var_operators = input("Input An Operator, Or Press 'q' To Exit: ") ### carácter

            if var_operators == 'q':
                print('Exiting...')
                return

            if var_operators in operators:
                selected_operator = operators[var_operators]    ### En este punto ya estoy validando el operador seleccionado,
                                                                ### con 'if' por lo cual NO necesito validarlo con 'try:' entonces
            else:  ### 'SINO'... si el operador no existe dentro del diccionario, imprimo....
                print("Error, Input A Numeric Operator")
                continue
            
            try:
                next_var_num = int(input("Input Next Numeric Value: "))
            except ValueError:
                print("Error, Not A Numeric Value, Try Again")
                continue

            res = selected_operator(var_num,next_var_num)

            if res is not  None:
                print("Result: ", res)
                var_num = res


calc()