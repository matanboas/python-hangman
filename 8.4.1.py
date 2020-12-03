def print_hangman(num_of_tries):
    picture_1 = "    x-------x"
    picture_2 = """    x-------x
    |
    |
    |
    |
    |"""
    picture_3 = """    x-------x
    |       |
    |       0
    |
    |
    |"""
    picture_4 = """    x-------x
    |       |
    |       0
    |       |
    |
    |"""
    picture_5 = """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |"""
    picture_6 = """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """
    picture_7 = """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""
    hangman_photos = {1:picture_1, 2:picture_2, 3:picture_3, 4:picture_4, 5:picture_5, 6:picture_6, 7:picture_7}

    print(hangman_photos[num_of_tries])