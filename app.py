from flask import Flask
from flask import request
from libary.markov import Markov
from libary.file_parser import File_Parser
from libary.random_sentence import Sentence

app = Flask(__name__)

@app.route('/')

def generate_sentence():
    file = File_Parser("corpus_text/The-Iliad-Of-Homer.txt")
    markov = Markov(file.parsed_file)
    sentence = Sentence(markov)

    count = request.args.get('num', default=10, type=int)
    benchmark = request.args.get('bench', default=False, type=bool)
    sentence = sentence.get_sentence(count, bool(benchmark))
    if benchmark:
        return "generation time: {}\n\n{}".format(sentence[0], sentence[1])
    return sentence
