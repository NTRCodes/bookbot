windows_path = "C:\\Users\\nr44c\\workspace\\github.com\\ntrcodes\\bookbot\\books\\frankenstein.txt"
wsl_path = "books/frankenstein.txt"

import string

def get_letter_count(letter_count: tuple):
    return letter_count[1]

def word_count(word_list):
    return len(word_list)

def letter_count(word_list):
    punctuations = [*string.punctuation]
    letter_counts = {}
    for word in word_list:
        # filter all punctuation from each word
        letters_of_word = [letter for letter in [*word.lower()] if letter.isalpha()]
        for letter in letters_of_word:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

    letters = [(letter, letter_counts[letter]) for letter in letter_counts]
    letters.sort(key=get_letter_count, reverse=True)

    return letters
            

with open(wsl_path) as f:
   file_contents = f.read() # get text as a string
   words = word_count(file_contents.split())
   letters = letter_count(file_contents.split())
   print(f"*** Begin Report of: {wsl_path} ***\n")
   print(f"There are {words} words in the document\n")
   for letter, count in letters:
    print(f"The '{letter}' character was found {count} times")