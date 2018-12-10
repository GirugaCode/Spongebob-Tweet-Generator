import random


def histogram_dict():

    histogram = {}

    for word in list_of_words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram
