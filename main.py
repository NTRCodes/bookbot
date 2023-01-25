windows_path = "C:\\Users\\nr44c\\workspace\\github.com\\ntrcodes\\bookbot\\books\\frankenstein.txt"
wsl_path = "books/frankenstein.txt"

import string

def word_count(word_list):
    return len(word_list)

def letter_count(word_list):
    punctuations = [*string.punctuation]
    letter_map = {}
    for word in word_list:
        # filter all punction from each word
        letters = [letter for letter in [*word.lower()] if letter.isalpha()]
        for letter in letters:
            if letter in letter_map:
                letter_map[letter] += 1
            else:
                letter_map[letter] = 1
    return letter_map
            

with open(wsl_path) as f:
   file_contents = f.read() # get text as a string
   n_words = word_count(file_contents.split())
   n_letters = letter_count(file_contents.split())
   print(f"*** Begin Report of: {wsl_path} ***\n")
   print(f"There are {n_words} words in the document\n")
   for letter in n_letters:
    print(f"The '{letter}' character was found {n_letters[letter]} times")