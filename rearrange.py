import random
import sys

def random_arrangement():
    # A list of the given terminal command line inputs
    inputs_list = sys.argv[1:]
    # An empty list
    result_list = []
    while len(inputs_list) != 0:
        # Returns a random index number from the inputs_list
        rand_index = random.randint(0, len(inputs_list) -1)
        # Pops the index values from inputs_list and adds it into the empty result_list
        result_list.append(inputs_list.pop(rand_index))
    # Changes the list to strings
    return (' '.join(result_list))
    # pass


if __name__ == '__main__':
    arrange = random_arrangement()
    print(arrange)
