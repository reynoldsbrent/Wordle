import random

def word_list():
    list_of_words = []
    with open('5_letter_words.txt', 'r') as file:
        for line in file:
           line = line.strip()
           list_of_words.append(line)
    return list_of_words

def random_word(list_of_words):
    word = list_of_words[random.randint(0, len(list_of_words) - 1)]
    return word

def is_real_word(guess, list_of_words):
    if guess in list_of_words:
        return True
    else:
        return False

def check_guess(word_entered, actual_word):
    final_string = ''
    number_of_letters_in_guess = []
    number_of_letters_in_actual = []
    for i in range(len(word_entered)):
        number_of_letters_in_guess.append(word_entered.count(word_entered[i]))
    
    for i in range(len(actual_word)):
        number_of_letters_in_actual.append(actual_word.count(actual_word[i]))

    for j in range(len(word_entered)):
        if word_entered[j] == actual_word[j]:
            final_string += "X"
        elif (word_entered[j] in actual_word):
            if word_entered[j] in word_entered[:j]:
                final_string += "_"
            else:
                final_string += "O"
        else:
            final_string += "_"

    if final_string == "XXXXX":
        return "XXXXX"
    
    return final_string

def next_guess(list_of_words):
    guess = input("Please enter a guess: ").lower()
    status = False
    while status == False:
        if is_real_word(guess, list_of_words):
            status = True
            return guess
        else:
            print("That is not a real word!")
            guess = input("Please enter a guess: ").lower()

def main():
    list_of_words = word_list()
    random_actual_word = random_word(list_of_words)
    count = 0
    while count < 6:
        guess = next_guess(list_of_words)
        print(check_guess(guess, random_actual_word))
        if check_guess(guess, random_actual_word) == "XXXXX":
            print("You won!")
            break
        else:
            count += 1
        if count == 6:
            print(f"You lost! \nThe word was {random_actual_word}")
main()