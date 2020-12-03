def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()

    if len(letter_guessed) != 1 or letter_guessed.isalpha() == False or letter_guessed in old_letters_guessed:
        i = 0
        print("X")
        
        while i < len(old_letters_guessed) - 1:
            print(old_letters_guessed[i]  , end =" ")
            print(" -> " , end =" ")
            i += 1
        print(old_letters_guessed[-1])

    else:
        old_letters_guessed.append(letter_guessed)
        return True