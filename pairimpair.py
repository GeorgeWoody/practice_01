def sum_funct(iterable):
    total = 0
    for i in iterable:
        total = total + i
    return total


def pair_impair():
    pair_impair_list = list(map(int, input("Input Numbers To Classify\nSeparated By Comma: ").split(",")))
    pairs = []
    impairs = []

    print("Numbers Added: ", pair_impair_list)

    for i in pair_impair_list:
        if i % 2 == 0:
            pairs.append(i)
        else:
            impairs.append(i)

    total_pair = sum_funct(pairs) #Importante: El resultado de la funcion y su argumento ya procesado, se debe guardar en una variable para poder ser mostrado
    # total_pair = 0
    # for x in pairs:
    #    new_num_pair = x
    #    total_pair = total_pair + new_num_pair

    total_impair = 0
    for n in impairs:
        new_num_impair = n
        total_impair = total_impair + new_num_impair

    print("Pairs: ", pairs)
    print("Impairs: ", impairs)
    print("Summed Pairs: ", total_pair )
    print("Summed Impairs: ", total_impair)



pair_impair()