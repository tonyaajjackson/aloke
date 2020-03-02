#! usr/bin/ python3

import numpy
import random

def word_gen(prob, num_names):
    new_words = []
    for x in range(num_names):
        end_of_word = False
        prev_letter = 0
        word = ""

        # Add loop counter to catch if loop gets stuck
        loops = 0
        while not end_of_word:
            rand_prob = random.random()

            # Find a letter corresponding to this probability
            found_letter = False
            current_letter = 0
            while not found_letter:
                if rand_prob <= prob[prev_letter, current_letter]:
                    found_letter = True
                    prev_letter = current_letter
                else:
                    current_letter +=1

            if current_letter == 0:
                end_of_word = True
            else:
                word += chr(current_letter+96)

            loops +=1
            if loops > 100:
                print("Looped too many times - exiting")
                end_of_word = True

        new_words.append(word)
    return new_words