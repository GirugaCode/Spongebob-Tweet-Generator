import random
import sys


def random_arrangement():
    # Creates a list for the command line inputs starting from the 1 index
    inputs_list = sys.argv[1:]
    # An empty list to append the command lines as strings
    result_list = []
    # shuffles the list
    random.shuffle(inputs_list)

    for command_line in inputs_list:
        # Adds the indexs from the input_list to the empty result_list
        result_list.append(command_line)
        # Converts the list into strings
        str1 = ' '.join(result_list)
    return str1


if __name__ == '__main__':
    arrange = random_arrangement()
    print(arrange)
