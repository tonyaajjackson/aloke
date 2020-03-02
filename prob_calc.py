import numpy

def prob_calc(words):
    prob  = numpy.zeros((27,27))

    # Count up instances of each letter in dataset
    for word in words:
        prev_letter = 0     # Starting a new word, so the previous letter is an end of line
        word = word.lower() + "`"       #Adding ` to detect end of word
        for letter in word:
            assert letter != " ", "Space found in word. Ensure list of words does not contain spaces"
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

    return prob
