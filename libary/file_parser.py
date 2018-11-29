import re


class File_Parser(object):

    def __init__(self, path=None):
        """If path is given, store parsed data."""
        if path is not None:
            self.parsed_file = self.read_file(path)

    def read_file(self, path):
        """returns a list of all words in the given source."""

        lines = [line.rstrip('\n').strip(' ')
                 for line in open(path)]

        word_list = []
        for line in lines:
            for word in line.split():
                if word != ' ':
                    special_chars = re.findall("[^A-Za-z0-9']+", word)
                    word = re.sub("[^A-Za-z0-9']+", "", word)
                    word_list.append(word.lower())
                    if len(special_chars) > 0:
                        for char in special_chars:
                            word_list.append(char)
        return word_list


if __name__ == "__main__":
    file_parser = File_Parser('corpus_text/The-Iliad-Of-Homer.txt')
    print(file_parser.parsed_file)
