import json
import numpy
from prob_calc import prob_calc
from word_gen import word_gen

# Load words from file
file_path = "firstNames.json"

with open(file_path) as read_file:
    # Corpora file uses format:
    # {{description: description}, {words: [list of words]} so the list of words
    # needs to be extracted for use
    words_raw = json.load(read_file)
    for item in words_raw:
        if type(words_raw[item]) == list:
            words = words_raw[item] 

prob = prob_calc(words)

num_words = 10
new_words = word_gen(prob, num_words)

print("\n".join(new_words))