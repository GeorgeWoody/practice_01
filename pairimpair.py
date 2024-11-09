def sums(iterable):
    total = 0
    for i in iterable:
        total = total + i
    return total

def pair_impair():
    pairs:list[float] = []
    impairs:list[float] = []
    total_pair = 0
    total_impair = 0
    while True:
        try:
            pair_impair_list = list(map(float, input("Input Numbers To Classify\nSeparated By Comma: \n").split(",")))

            print("#"*30)
            print("Numbers Added: ", pair_impair_list)
            print("#" * 30)
            print(" \n")
            for i in pair_impair_list:
                if i % 2 == 0:
                    pairs.append(i)
                else:
                    impairs.append(i)

            total_pair = sums(pairs)#Importante: El resultado de la función y su argumento ya procesado, se debe guardar en una variable para poder ser mostrado
            total_impair = sums(impairs)

        except ValueError:
            print("Error, Input A Numeric Value, Try Again")
            continue

        print("*** Pairs: ", pairs, " \n")
        print("*** Impairs: ", impairs, " \n")
        print("*** Summed Pairs: ", total_pair, " \n")
        print("*** Summed Impairs: ", total_impair, " \n")

pair_impair()