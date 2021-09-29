import random

#This is a dictinary to save the states of the hangman
HANGMAN_PHOTOS = {1: "\tx-------x",
                  2: "\tx-------x\n\t|\n\t|\n\t|\n\t|\n\t|",
                  3: "\tx-------x\n\t|       |\n\t|       0\n\t|\n\t|\n\t|",
                  4: "\tx-------x\n\t|       |\n\t|       0\n\t|       |\n\t|\n\t|",
                  5: "\tx-------x\n\t|       |\n\t|       0\n\t|      /|\\\n\t|\n\t|",
                  6: "\tx-------x\n\t|       |\n\t|       0\n\t|      /|\\\n\t|      /\n\t|",
                  7: "\tx-------x\n\t|       |\n\t|       0\n\t|      /|\\\n\t|      / \\\n\t|"}

#Function that print the state
#The function get the dictionary key (state) as parameter
def print_hangman_guess(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])

#Function that print the start logo of the game
def print_game_wolcome():
    HANGMAN_ASCII_ART = """Welcome to the game Hangman
        _    _
       | |  | |
       | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
       |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\   
       | |  | | (_| | | | | (_| | | | | | | (_| | | | |
       |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |
                           |___/
Let's start!    
    """
    print(HANGMAN_ASCII_ART)
    print("you have %d geuss." % MAX_TRIES)
    print_hangman_guess(1)

#Bool function have 2 argumnets,check if the player cracked the secret word or not.
#The "old_letters_guessed" is a list of the right guessed lettes and "_" to the missing letters.
#If the char "_" is not partof the list, the player win.
def check_win(secret_word, old_letters_guessed):
    if "_" in show_hidden_word(secret_word, old_letters_guessed)[1]:
        return False
    else:
        return True

#Function to replace right letter guessed from "_" to the letter.
def show_hidden_word(secret_word, old_letters_guessed):
    init_line = list(secret_word)
    good_guess = False
    for var in range(0, len(secret_word)):
        if secret_word[var] in old_letters_guessed:
            init_line[var] = secret_word[var]
            good_guess = True
        else:
            init_line[var] = "_"
    print_str =""
    for var in init_line:
        print_str = print_str + var + " "
    print("valid latters: %s\n"% print_str)
    return [good_guess, print_str]

#function to check input validation.
def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) > 1 and not letter_guessed[:].isalpha():
        print("E3 - string longer than 1 char and contains non ABC letter")
        return False
    elif len(letter_guessed)<1:
        print("E0 - can't insert empty letter")
        return False
    elif not letter_guessed[0].isalpha():
        print("E2 - letter must be from ABC")
        return False
    elif len(letter_guessed)>1:
        print("E1 - letter can contains only one char")
        return False
    elif letter_guessed in old_letters_guessed:
        print("E4 - you already guessed this letter")
        return False
    else:
        return True

#Function to update the letter guessed bank
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        print("old letters guessed bank:",old_letters_guessed)
        if letter_guessed in secret_word:
            print("great guess! :)")
            return True
        else:
            print("letter not in secret word :(")
            return False
    else:
        print("X")
        print ("Old letter bank: ", (sorted(old_letters_guessed)))
        return False

#function that choosing word from file:
#if the indux argument is "0", the word choosed randomalic, else the number of word.
#if the number is bigger than number of word, the the function start to run again in loop
def choose_word(file_path, index):
    file_data = deserialization(file_path)

    list_of_complete_string = []
    list_of_complete_string = file_data[0]

    split_string_to_sparete_element = []
    array_of_string_words= ""
    for var in list_of_complete_string:
        split_string_to_sparete_element.append(var.split(" "))

    for file_data in list_of_complete_string:
        array_of_string_words = (file_data.split(" "))

    while index >= len (array_of_string_words):
        index-=len(array_of_string_words)

    ret_tup = len(set(array_of_string_words)), array_of_string_words[index-1]
    if index == False:
        print("word choosed random..")
        index = random.randint(1, len(array_of_string_words))

    return (array_of_string_words[index-1])

#deserialization from file to list.
def deserialization(file_path):
    read_file = open(file_path, "r")
    data = read_file.read()
    data1 = data.split("\n")
    data2 = []
    for item in data1:
        data2.append(item.split(";"))
    return data2

if __name__ == '__main__':
    MAX_TRIES = 6
    old_letters_guessed = []
    file1 = r"C:\Users\Avishai Hagever\Desktop\file1.txt" #change here path location
    num_of_tries = 0
    good_guess = False

    print_game_wolcome()
    secret_word = choose_word(file1, 0)
    print("_ " * len(secret_word))

    while (num_of_tries < MAX_TRIES):
        letter_guessed = input("Guess a letter: ")
        letter_guessed = letter_guessed.lower()

        while not check_valid_input(letter_guessed, old_letters_guessed):
            letter_guessed = input("Woring input insreted, Guess a new letter: ")
            letter_guessed = letter_guessed.lower()

        if not try_update_letter_guessed(letter_guessed, old_letters_guessed):
            num_of_tries += 1
            print(HANGMAN_PHOTOS[num_of_tries + 1])
            print("%d tries left" % (MAX_TRIES - num_of_tries))

        if check_win(secret_word, old_letters_guessed):
            print("WIN!!")
            break

        if num_of_tries == MAX_TRIES:
            print("GAME OVER, Try again.")
            break
