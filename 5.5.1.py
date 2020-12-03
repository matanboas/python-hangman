def is_valid_input(letter_guessed):
    letter_guessed = letter_guessed.lower()

    if len(letter_guessed) != 1 or letter_guessed.isalpha() == False:
        return False
    else:
        return True