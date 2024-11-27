def test_sets():
    guessed_letter = set()  ### Important: la variable usada por set() debe estar fuera del bucle while True, si
    while True:             ### se encuentra dentro, la variable se vaciara y no agregará los user_imput a guessed_
        user_letter = input("Input Letter: ")

        if user_letter in guessed_letter:
            print("Letter Exist")
        else:
            guessed_letter.add(user_letter)
            print("Letter Dont Exist")
            continue
        
test_sets()