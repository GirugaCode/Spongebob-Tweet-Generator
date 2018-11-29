
import time
import random

# from listogram import Listogram
from markov import Markov
from file_parser import File_Parser


class Sentence(object):

    def __init__(self, histogram):
        self.change_histogram(histogram)

    def change_histogram(self, histogram):
        '''Sets a new histogram'''
        self.histogram = histogram
        if isinstance(histogram, list):
            self.is_listogram = True
        else:
            self.is_listogram = False

    def get_sentence(self, length, benchmark=False):
        '''Generates a sentence of a given length. If benchmarking
        is set to true, returns a list containing sentence and
        generation time. Otherwise, only returns a sentence.'''
        if benchmark:
            start_time = time.time()

        sentence = self._generate_sentence(length)

        # If benchmarking, returns list with sentence string and
        # generation time. Otherwise, returns sentence string.
        if benchmark:
            # sentence = ' '.join(sentence)
            generation_time = time.time() - start_time
            return [generation_time, ' '.join(sentence)]
        else:
            return ' '.join(sentence)

    def _generate_sentence(self, length):
        sentence = []
        previous_word = ''
        while len(sentence) < length:
            random_word = (self._get_random_word_list() if self.is_listogram
                           else self._get_random_word_dict(previous_word))
            sentence.append(random_word)
            previous_word = random_word
        return sentence

    def _get_random_word_list(self):
        accumalator = 0
        random_number = random.randint(1, self.histogram.types)
        for word in self.histogram:
            accumalator = accumalator + word[1]
            if accumalator >= random_number:
                return word[0]

    def _get_random_word_dict(self, previous_word):
        if previous_word != '':
            accumalator = 0
            random_number = random.randint(1, self.histogram[previous_word].types)
            for key, val in self.histogram[previous_word].items():
                accumalator += val
                if accumalator >= random_number:
                    return key
        else:
            for key, _ in self.histogram.items():
                return key


if __name__ == "__main__":
    file = File_Parser('corpus_text/The-Iliad-Of-Homer.txt')
    markov = Markov(file.parsed_file)
    sentence = Sentence(markov)
    print(sentence.get_sentence(10, True))
