def choose_word(file_path, index):
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