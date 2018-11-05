import random

histogram_dictionary = {}

def histogram(file):
    for word in file:
        if word in histogram_dictionary:
            histogram_dictionary[word] += 1
        else:
            histogram_dictionary[word] = 1

    return histogram_dictionary

def random_word(file):
    word_count = 0
    sum_dict = sum(histogram_dictionary.values())
    rand_sum = random.randint(0, sum_dict - 1)

    for key, value in histogram_dictionary.items():
        word_count += value
        if word_count > rand_sum:
            return key
        else:
            continue

def random_test(file):
    dict = {}

    for _ in range(0,1000):
        word_selected = random_word(histogram_dictionary)
        if word_selected in dict:
            dict[word_selected] += 1
        else:
            dict[word_selected] = 1
    return dict

if __name__ == "__main__":
    with open('sample-histogram.txt', 'r') as file:
        words = file.read().replace('\n', '').lower().split()
    histogram = histogram(words)
    print(histogram)
    print(random_word(histogram))
    print(random_test(histogram))
