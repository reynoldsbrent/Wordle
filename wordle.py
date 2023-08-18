import random

def word_list(list_of_words):
    with open('5_letter_words.txt', 'r') as file:
        for line in file:
           line = line.strip()
           list_of_words.append(line)
    return list_of_words

def random_word(list_of_words):
    pass

def is_real_word(guess, list_of_words):
    pass

def check_guess(word_entered, actual_word):
    pass

def next_guess(list_of_words):
    pass

def main():
    list_of_words = []
    print(word_list(list_of_words))

main()