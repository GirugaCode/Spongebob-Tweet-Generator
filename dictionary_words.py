import sys
import random


def random_words():

    # Created a variable to open the "/usr/share/dict/words" and read it and splits all the new lines.
    words = open("/usr/share/dict/words", "r").read().split('\n')

    # Created a variable to hold the first terminal command-line input
    command_input = sys.argv[1]

    # Created an empty list
    randomWords = []

    # Use a for loop to loop through the variable with the terminal command-line input
    # Append words in the empty list, randomize through the variable that is going through the text file
    # Return it as a string
    for _ in range(int(command_input)):
        randomWords.append(words[random.randint(0, len(words))] + " ")
    return (''.join(randomWords))


# Print
print(random_words())
