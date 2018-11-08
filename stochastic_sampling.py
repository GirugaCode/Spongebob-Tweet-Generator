import random

# This function creates a histogram of a text file and returns it as a dictionary
def open_file():
    with open('fish.txt', 'r') as myfile:
        words = myfile.read().replace('\n', '').lower().split()
    return words

def histogram():
    # Empty dictionary to store our histogram of the text file
    histogram_dictionary = {}
    # Opens the text file
    file = open_file()
    # Loops through the text file and adds the frequency of words inside the empty dictionary
    for word in file:
        if word in histogram_dictionary:
            histogram_dictionary[word] += 1
        else:
            histogram_dictionary[word] = 1
    # Returns the dictionary
    return histogram_dictionary

def random_word():
    # Inputs the histogram
    histogram_dictionary = histogram()

    # Keeps track of the count with an accumulator
    word_count = 0

    # Grabs the sum of the dictionary values
    total_values = sum(histogram_dictionary.values())
    # Gets a random number from the sum of values
    rand_index = random.randint(0, total_values - 1)
    # For loop that goes through the (key, value) of the histogram_dictionary

    for key, value in histogram_dictionary.items():
        # Increment the word_count with the value of histogram_dictionary

        word_count += value
        # If the word_count is less than the returned rand_sum return the key
        if word_count > rand_index:
            return key
        else:
            continue

def random_test():
    dict = {}
    # Inputs the histogram
    histogram_dictionary = histogram()
    for _ in range(0,100):
        word_selected = random_word()
        if word_selected in dict:
            dict[word_selected] += 1
        else:
            dict[word_selected] = 1
    return dict

def main():

    histogram_dict = histogram()
    print(histogram_dict)
    print(random_word())
    print(random_test())

    return(random_word())

if __name__ == "__main__":
    main()
