from flask import Flask,render_template, request, redirect
from flask import request
import nth_order_markov
import sys
import twitter

app = Flask(__name__)

app.nth_order_markov = nth_order_markov.main()

@app.route('/')
def sentence_creator():
    my_sentence = app.nth_order_markov.generate_sentence()
    return render_template("main.html", sentence = my_sentence)

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')
