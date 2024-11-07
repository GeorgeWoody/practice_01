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
    x = 0
    for n in pairs:

        new_num = n
        sum_pair = n + x


    print(pairs)
    print(impairs)
    print(sum_pair)


pair_impair()