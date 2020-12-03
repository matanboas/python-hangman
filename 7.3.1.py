def show_hidden_word(secret_word, old_letters_guessed):
    secret_word = secret_word.lower()

    i = 0
    printable_word = ""
     
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            printable_word += secret_word[i] + " "
        else:
            printable_word += "_ "
    printable_word = printable_word[0:-1]
    return printable_word