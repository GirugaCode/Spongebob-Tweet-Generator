from flask import Flask
from flask import request
import nth_order_markov
import sys


app = Flask(__name__)

app.nth_order_markov = nth_order_markov.main()

@app.route('/')

def sentence_creator():
    my_sentence = app.nth_order_markov.generate_sentence()
    return my_sentence
