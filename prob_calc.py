#! usr/bin/ python3

import json
import numpy

file_path = "../corpora/data/humans/firstNames.json"

# Load words from file
with open(file_path) as read_file:
    # Corpora file uses format:
    # {{description: description}, {words: [list of words]} so the list of words
    # needs to be extracted for use
    words_raw = json.load(read_file)
    words = words_raw["firstNames"]

# Set up array to hold cumulative probabiliies for each letter
# 27x27 array where each row and column represents a letter, "`" is a beginning
# or end of word
#   ` a b c d e f g h...
# ` 0 0 0 0 0 0 0 0 0...
# a 0 0 0 0 0 0 0 0 0...
# b 0 0 0 0 0 0 0 0 0...
# c 0 0 0 0 0 0 0 0 0...
# d 0 0 0 0 0 0 0 0 0...
# Row is the previous letter in the word. Column is the cumulative probability
# that the next letter is the letter of the column.
# A sample row entry with equal probabilities for all letters would be:
# [1/27 2/27 3/27 4/27...]
# The probability zone for each letter is bounded by the probability of the
# previous letter and the probability of the current letter. Using the previous
# sample row, "`" occupies the range [0, 1/26) and "a" occupies [1/26, 2/26)

prob  = numpy.zeros((27,27))

# Count up instances of each letter in dataset
for word in words:
    prev_letter = 0     # Starting a new word, so the previous letter is a space
    word = word.lower() + "`"       #Adding ` to detect end of word
    for letter in word:
        current_letter = ord(letter) - 96   # Conver string to array index
        prob[prev_letter, current_letter] += 1
        prev_letter = current_letter

# Normalize counts to get probabilities
sums = numpy.apply_along_axis(numpy.sum,1,prob).reshape(1,-1)
prob = prob/sums.T

# Make probabilities cumulative
for row in range(0,27):
    for col in range(1,27):
        prob[row, col] += prob[row, col-1]

# Store probs to table
numpy.save("prob", prob)
