from flask import Flask
from text_file_frequency import open_file, histogram, random_word, main

app = Flask(__name__)

@app.route('/')

def generate_sentence():
    return (main())
