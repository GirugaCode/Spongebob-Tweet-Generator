import random


def histogram_dict(file):
    text_file = open(file, 'r') # Open text file

    content = text_file.read() # Read text file
    list_of_words = content.split(' ') # Splits the spaces in the text file
    text_file.close() # Close text file for optimization

    histogram = {}

    for word in list_of_words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram

if __name__ == '__main__':
    dictionary = histogram_dict('fish.txt')
    print(dictionary)
