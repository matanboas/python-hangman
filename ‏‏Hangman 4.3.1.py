letter = input("Guess a letter: ").lower()
check_is_it_alpha = letter.isalpha()
how_mauch_characters = len(letter)

if how_mauch_characters != 1 and check_is_it_alpha == False:
    print("E3")
elif how_mauch_characters > 1:
    print("E1")
elif check_is_it_alpha == False:
    print("E2")
else:
    print(letter)