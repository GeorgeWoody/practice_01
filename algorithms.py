def search_max_number():
    list_num = [4,5,9,7]
    num_max = list_num[0]
    for i in list_num:
        if i > num_max:
            num_max = i

    print("el numero mayor es: ", num_max)
    
    
def search_max_number_parameter(list_param):  ###[6,9,4,10]
    num_max_p = list_param[0]
    for i in list_param:  #9
        if i > num_max_p:
            num_max_p = i
    return num_max_p

def structures_control():
    pass     
