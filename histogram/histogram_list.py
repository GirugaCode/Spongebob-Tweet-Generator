import random
import re


def histogram_list(file): # Takes an argument file so I can input the text file name when attempting run it.
    text_file = open(file, 'r') # Opens the text file and reads it

    content = text_file.read().lower() # Will read the text file in a lower case context
    words = re.split(' ', content) # Splits all the words in the text file containing ' ' so it will only show the words
    text_file.close() # Closes the text file for optimization


    list_of_words = [] # Empty list for words
    count = [] # Empty list to keep count

    # For every word in the text file
    for word in words:
        # If the word in the empty array(list_of_words)
        if word in list_of_words:
            # Keeps count for words of the same index
            count[list_of_words.index(word)] += 1
        else:
            # Else, append word in the list
            list_of_words.append(word)
            count.append(1)

    # An empty list to contain the histogram results
    histogram = []
    # Keeps track of the index
    i = 0

    # For word in list_of_words list
    for word in list_of_words:
        # Append both the words and how many times it shows up in the text file to the histogram list
        histogram.append([list_of_words[i], count[i]])
        i += 1

    return histogram

if __name__ == '__main__':
    histogramlist = histogram_list('sample-histogram.txt')
    print(histogramlist)
