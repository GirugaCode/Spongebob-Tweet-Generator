from __future__ import division, print_function

from libary.Source.dictogram import Dictogram
from libary.stochastic_sampling import random_word
import random

class Nth_Order_Markov(dict):
    def __init__(self, word_list=None, order=6):
        super(Nth_Order_Markov, self).__init__() # initalize empty dictionary to self
        self.empty = True
        # order is how many words we are going to be grabbing to be in our list
        self.order = order

        if word_list is not None:
            self.create_markov(word_list)


    def create_markov(self, word_list):
        length_of_list = len(word_list)

        for i in range(0, length_of_list - self.order):
            i + self.order < length_of_list
            # key
            current_type = tuple(word for word in word_list[i:i + self.order])
            # maximum length were indexing / never indexing out of list
            # value
            next_type = word_list[i + self.order]
            self.add_token(current_type, next_type)



    def add_token(self, current_type, next_type):
        # checking if init dictionary is Empty
        if self.empty:
            self.empty = False
            self[current_type] = Dictogram([next_type])
        # if dictionary is not empty, checking for current_type (tuple)
        else:
            #if current_type is found, we increment frequency of next_type with .add_count
            if current_type in self:
                self[current_type].add_count(next_type)
            # if current_type is not found we create a new key-value pair
            # of {(current_type): {next_type: count}} structure.
            # current_type = tuple of nth order
            # next_type = next unique word
            else:
                self[current_type] = Dictogram([next_type])



    def generate_sentence(self, sentencelength=16):
        # Keeps the indexs in bounds
        sentencelength = sentencelength - self.order

        # TODO: Empty List
        print(" ---EMPTY LIST--- ")
        random_sentence = []
        print(random_sentence)

        # TODO: Create a list of keys
        # [(a,b), (b,c), (c,d)]
        print(" ---LIST OF KEYS--- ")
        key = list(self.keys())
        print(key)

        # TODO: Pick a random index in your list to begin your markov walk
        # key[random_number]
        print(" ---RANDOM INDEX--- ")
        random_index = random.randint(0, len(key))
        print(random_index)

        # TODO: Generate a random key (a starting point for your markov)
        print(" ---RANDOM KEY--- ")
        random_key = key[random_index]
        print(random_key)

        # TODO: Store Key as a List instead of a Tuple
        list_of_tuples = list(random_key)
        print("--- my Tuple, but in a form of a list---")
        print(list_of_tuples)

        # TODO: Find associated with the key. Store into a variable
        print(" ---FIND VALUE--- ")
        find_value = self[random_key]
        print(find_value)

        # TODO: Get the next weighted random word from, by calling the function with your dictogram is the parameter
        print(" ---NEXT WORD--- ")
        next_word = random_word(find_value)
        print(next_word)

        # TODO: iterate through the length of the sentence
        random_sentence = list(random_key)
        for i in range(0, sentencelength):

            while next_word is None:
                key = key[random.randint(0, len(key))]
                next_word = random_word(self[key])
            # TODO: get rid fo the first thing in my tuple as a list
            print(" --- SLICE HEAD --- ")
            list_of_tuples = list_of_tuples[1:]
            print(" ---AFTER REMOVING HEAD---")
            print(list_of_tuples)
            # TODO: add the nextword to the list (add word to a list)
            list_of_tuples.append(next_word)
            print(" ---AFTER NEW WORDS ADDED--- ")
            print(list_of_tuples)
            random_key = tuple(list_of_tuples)
            print(" ---TURNS LIST INTO TUPLE--- ")
            print(random_key)

            find_value = self[random_key]
            print(" ---NEW POTENTIAL WORDS--- ")
            print(find_value)

            next_word = random_word(find_value)
            print(" --- NEW NEXT WORD--- ")
            print(next_word)

            random_sentence.append(next_word)
            print("ADDING THIS WORD TO THE SENTENCE: ")
            print(next_word)

        my_sentence = " ".join(random_sentence)
        return my_sentence

def main():
    corpus_text = open('libary/corpus_text/finalcorpus.txt', 'r')

    list = []
    for line in corpus_text:
        list.append(line)

    markov = Nth_Order_Markov(list[0].split())
    return markov

main()
