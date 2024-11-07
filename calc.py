import os
os.system('cls' if os.name =='nt' else 'clear')

def sums(x, y):
    return x + y

def rest(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y == 0:
        print("Error. Cannot Divide Zero")
    else:
        return x / y

operators = {
    '+': sums,
    '-': rest,
    '*': mult,
    '/': div,
}

def calculator():

    while True:
        try:
            print("#"*30)
            var_num = float(input("Input Numeric Value: "))
            print("#"*30)

        except ValueError:
            print("#"*30)
            print("Not Numeric Value. Try Again")
            continue

        while True:
            var_operator = input("Input Numeric Operator, Or Press 'q' to exit: ")

            if var_operator == 'q':
                print("Exiting...")
                return

            if var_operator in operators:
                selected_operator = operators[var_operator]
            else:
                print("Not An Operator. Input Again")
                continue

            try:
                next_var_num = float(input("Input Next Value: "))
            except ValueError:
                print("Not A Numeric Value, Try Again")
                continue

            result = selected_operator(var_num, next_var_num)

            if result is not None:
                print("Output: ", result)
                var_num = result

#calculator()

