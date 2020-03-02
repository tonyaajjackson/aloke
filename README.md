# aloke
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

aloke is a tool for generating random words similar to existing words.

## How it works
When given a list of words, aloke analyzes the frequency and pattern of letters within each word to make a probability matrix. The probability matrix is then connected to a finite-state machine that moves about the probability matrix to generate new words.

### Probability Matrix
The probability matrix is a 27x27 array of cumulative probabilities. Each row represents the current letter. Each column value in a row represents the cumulative probability of that letter being the next letter in the word. The "`" character represents the beginning or end of a word.

A sample probability matrix with equal probabilities for each letter would look like:

|   | ` | a    | b    | c    | d    | e    | f    | g    | ... |
|---|---|------|------|------|------|------|------|------|-----|
| ` | 1/27 | 2/27 | 3/27 | 4/27 | 5/27 | 6/27 | 7/27 | 8/27 |... |
| a | 1/27 | 2/27 | 3/27 | 4/27 | 5/27 | 6/27 | 7/27 | 8/27 |... |
| b | 1/27 | 2/27 | 3/27 | 4/27 | 5/27 | 6/27 | 7/27 | 8/27 |... |
| c | 1/27 | 2/27 | 3/27 | 4/27 | 5/27 | 6/27 | 7/27 | 8/27 |... |
| d | 1/27 | 2/27 | 3/27 | 4/27 | 5/27 | 6/27 | 7/27 | 8/27 |... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

The probability zone for each letter is bounded by the probability value of the
previous letter and the probability value of the current letter. Using the previous
sample row, "a" occupies [1/27, 2/27). As there is no previous letter before "`", it occupies the range [0, 1/27).

### Finite State Machine
The finite state machine begins with the current letter as "`", starting on row 0 in the probability matrix.

A random value between 0 and 1 is generated, then compared along the row in the probability matrix until the first probability value larger than random value is found. For example, using the above sample matrix and a random value of 4.5/27, the first value larger than 4.5/27 is 5/27, which corresponds to the letter "d".

The found letter ("d") is then appended to the new word buffer and becomes the current letter, moving to the corresponding row (row 4). A new random value is generated and then compared along the row to find the next letter.

This process repeats until the found letter is "`", signifying the end of the word. The word buffer is appended to the list of words and a new word is started.

# Getting Started
See "main.py" for a basic example of using aloke.

## Install Dependencies
* [Python 3](https://www.python.org/downloads/)
* [Numpy](https://numpy.org/)


## Import Dependencies
```python
import json
import numpy
from prob_calc import prob_calc
from word_gen import word_gen
```

## Set up list of words
Create a variable with your desired list of words as a list of strings. Ensure that the words do not contain spaces. As an example, main.py uses the firstNames.json list from [Corpora](https://github.com/dariusk/corpora):

```python
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
```

## Generate the probability matrix
Pass the word list to prob_calc and store the probability matrix as a variable

```python
prob = prob_calc(words)
```

### Generate new words
Pass the probability matrix and number of words to word_gen

```python
num_words = 10
new_words = word_gen(prob, num_words)
```

### Print new words to console
```python
print("\n".join(new_words))
```