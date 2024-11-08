def sums(iterable):
    total = 0
    for i in iterable:
        total = total + i
    return total

def pair_impair():
    try:
        pair_impair_list = list(map(float, input("Input Numbers To Classify\nSeparated By Comma: \n").split(",")))
        pairs:list[float] = []
        impairs:list[float] = []
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

        total_impair = 0
        for n in impairs:
            new_num_impair = n
            total_impair = total_impair + new_num_impair

    except ValueError:
        print("Error, Input A Numeric Value, Try Again")

    print("*** Pairs: ", pairs, " \n")
    print("*** Impairs: ", impairs, " \n")
    print("*** Summed Pairs: ", total_pair, " \n")
    print("*** Summed Impairs: ", total_impair, " \n")

pair_impair()