def vocals_consonants():
    
    word_list = list(map(str, input("Input Word To Analyze: ").lower())) #Con el metodo .lowe() transformamos cualquier letra en minuscula.
    
    vocals_dict = ['a','e','i','o','u']
    consonants_dict = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    vocals_extracted = [] #Lista Vacia donde se almacenan vocales
    consonants_extracted = [] #Lista Vacia donde se almacenan consonantes
    
    for i in word_list:
        if i == ' ':
            continue            
        if i in vocals_dict:
            vocals_extracted.append(i)
        elif i in consonants_dict:
            consonants_extracted.append(i)
   
    print("Vocals In Word: ",vocals_extracted, "Total: ", len(vocals_extracted))
    print("Consonants In Word: ",consonants_extracted, "Total: ", len(consonants_extracted))    
    
    
    
    
    
vocals_consonants()