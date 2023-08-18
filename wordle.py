import random

list_of_words = []
def word_list():
    with open('5_letter_words.txt', 'r') as file:
        for line in file:
           line = line.strip()
           list_of_words.append(line)
    return list_of_words
