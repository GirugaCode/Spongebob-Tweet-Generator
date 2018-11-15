import random

def histogram_tuple(file):
    text_file = open(file, 'r')

    content = text_file.read().lower()
    words_file = content.split(' ')
    text_file.close()

    list_of_words = []
    count = []

    for i in words_file:
        if i in list_of_words:
            count[list_of_words.index(i)] += 1
        else:
            list_of_words.append(i)
            count.append(1)

    histogram = []
    i = 0

    for word in list_of_words:
        histogram.append((list_of_words[i], count[i])) #Changed the brackets to parenthesis to be classified as a tuple
        i += 1

    return histogram


if __name__ == '__main__':
    histogramtuple = histogram_tuple('corpus_text/fish.txt')
    print(histogramtuple)
