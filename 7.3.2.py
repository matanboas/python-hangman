def check_win(secret_word, old_letters_guessed):
    secret_word = secret_word.lower()
    i = 0
    printable_word = ""
    Win = True
     
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            pass
        else:
            Win = False
    
    return Win