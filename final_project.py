"""
hangman by matan boas
"""

# functions
def show_hidden_word(secret_word, old_letters_guessed):
    secret_word = secret_word.lower()

    i = 0
    printable_word = ""
     
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            printable_word += secret_word[i] + " "
        else:
            printable_word += "_ "
        i += 1
    printable_word = printable_word[0:-1]
    return printable_word

def check_if_lost_round(secret_word, letter_guessed):
    secret_word = secret_word.lower()
    i = 0
    secret_word_letters_list = []
     
    for i in range(len(secret_word)):
        secret_word_letters_list.append(secret_word[i])
        i += 1
    
    if letter_guessed in secret_word_letters_list:
        return False
    else:
        return True

def check_valid_input(letter_guessed):
    letter_guessed = letter_guessed.lower()

    if len(letter_guessed) != 1 or letter_guessed.isalpha() == False or letter_guessed in old_letters_guessed:
        return False
    else:
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()

    if not check_valid_input(letter_guessed):
        return False

    else:
        old_letters_guessed.append(letter_guessed)
        old_letters_guessed = old_letters_guessed.sort()
        return True

def bad_input(letter_guessed, old_letters_guessed):
    if try_update_letter_guessed(letter_guessed, old_letters_guessed) and check_valid_input(letter_guessed):
        return False
    else:
        return True

def choose_word(file_path, index):
    index = int(index)
    words = open(file_path, 'r')
    words_string = words.read()
    word_list = words_string.split(" ")
    word_list_with_filtering = []
    
    while index > len(word_list):
        index -= len(word_list)

    for word in word_list:
        if word not in word_list_with_filtering:
            word_list_with_filtering.append(word)

    word_and_words_number = (len(word_list_with_filtering), word_list[index - 1])
    return word_and_words_number


def print_hangman(num_of_tries):
    picture_1 = """
    x-------x
    """
    picture_2 = """
    x-------x
    |
    |
    |
    |
    |
    """
    picture_3 = """
    x-------x
    |       |
    |       0
    |
    |
    |
    """
    picture_4 = """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """
    picture_5 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """
    picture_6 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    """
    picture_7 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
    hangman_photos = {0:picture_1, 1:picture_2, 2:picture_3, 3:picture_4, 4:picture_5, 5:picture_6, 6:picture_7}

    print(hangman_photos[num_of_tries])

def start_screen(MAX_TRIES):
    print(r"""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
    """)
    print(MAX_TRIES)

def check_win(printable_word, secret_word):
    letter_list = printable_word.split(" ")
    guessed_word = ""
    for letter in letter_list:
        guessed_word += letter
    if guessed_word == secret_word:
        return True
    else:
        return False

# variable
MAX_TRIES = 6
start_screen(MAX_TRIES)
file_path, index = input(r"Enter file path: "), input(r"Enter index: ")
secret_word = choose_word(file_path, index)[1]
num_of_tries = 0
old_letters_guessed = []

print("\nLet’s start!\n")
print_hangman(num_of_tries)
print(show_hidden_word(secret_word, old_letters_guessed))

# main game loop
run_game = True
while run_game:
    letter_guessed = input("Guess a letter: ")
    letter_guessed = letter_guessed.lower()

    if not try_update_letter_guessed(letter_guessed, old_letters_guessed):

        i = -1
        print("X")
        old_letters_with_arrows = ""

        for old_letter in old_letters_guessed:
            old_letters_with_arrows += old_letter + " -> "
        old_letters_with_arrows = old_letters_with_arrows[0:-3]

        if old_letters_with_arrows != "":
            print(old_letters_with_arrows)

    else:
        printable_word = show_hidden_word(secret_word, old_letters_guessed)

        if check_if_lost_round(secret_word, letter_guessed):
            print(":(")
            num_of_tries += 1
            print_hangman(num_of_tries)

        print(printable_word)

        if check_win(printable_word, secret_word):
            print("WIN")
            run_game = False

        if num_of_tries == 6:
            print("LOSE")
            run_game = False