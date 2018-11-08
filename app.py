from flask import Flask
from stochastic_sampling import open_file, histogram, random_word, main

app = Flask(__name__)

@app.route('/')

def generate_sentence():
    return (main())
