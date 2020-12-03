def check_valid_input(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()

    if len(letter_guessed) != 1 or letter_guessed.isalpha() == False or letter_guessed in old_letters_guessed:
        return False
    else:
        return True