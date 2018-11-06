import random



# This function creates a histogram of a text file and returns it as a dictionary
def open_file():
    with open('sample-histogram.txt', 'r') as myfile:
        words = myfile.read().replace('\n', '').lower().split()
    return words

def histogram(file):
    histogram_dictionary = {}
    for word in file:
        if word in histogram_dictionary:
            histogram_dictionary[word] += 1
        else:
            histogram_dictionary[word] = 1
    return histogram_dictionary

def random_word(histogram_dictionary):
    # Keeps track of the count with an accumulator
    word_count = 0

    # Grabs the sum of the dictionary values
    sum_dict = sum(histogram_dictionary.values())
    # Gets a random number from the sum of values
    rand_sum = random.randint(0, sum_dict - 1)
    # For loop that goes through the (key, value) of the histogram_dictionary

    for key, value in histogram_dictionary.items():
        # Increment the word_count with the value of histogram_dictionary

        word_count += value
        # If the word_count is less than the returned rand_sum return the key
        if word_count > rand_sum:
            return key
        else:
            continue

# def random_test(file):
#     dict = {}
#     for _ in range(0,100):
#         word_selected = random_word(histogram_dictionary)
#         if word_selected in dict:
#             dict[word_selected] += 1
#         else:
#             dict[word_selected] = 1
#     return dict

def main():
    words = open_file()
    histogram_dict = histogram(words)
    # print(histogram_dict)
    return random_word(histogram_dict)

if __name__ == "__main__":
    main()
    # print(random_test(histogram))
