#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility

from Source.dictogram import Dictogram


class Markov(dict):
    """Markov is a dictionary of dictograms."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Markov, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None: # Loops through the whole list and takes account of the previous word
            previous_word = ''
            for word in word_list:
                self.add_count(word, previous_word)
                previous_word = word

    def add_count(self, word, previous_word, count=1):
        """Increase frequency count of given word by given count amount."""
        if previous_word is not '': # IF the previous word is not empty add self.type += 1
            try:
                dicto = self[previous_word]
            except KeyError:
                dicto = Dictogram()
                self.types += 1
            self[previous_word] = dicto
            dicto.add_count(word)
            self.tokens = self.tokens + count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        if word in self:
            return self[word]
        else:
            return 0


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Markov(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
