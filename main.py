from logging import debug
from flask import Flask, render_template, request
import nltk
from nltk import FreqDist
from textblob import TextBlob
from textblob import Word

app1 = Flask(__name__)


@app1.route('/')
def hello():
    return render_template('base.html')

@app1.route('/define',methods = ['POST'])
def define():
    ip_word = request.form.get('ip-word')
    text = TextBlob(ip_word)
    word_count = len(text.words)
    sen_count = len(text.sentences)
    freq = FreqDist(nltk.word_tokenize(ip_word))
    new = {}
    for i in text.words:
        if i not in new:
            new[i] = freq[i]
    for i in new:
        new[i] = str(round((new[i]/word_count)*100,2))+"%"

    return render_template('base.html',translated_text=f'\n the word count of "{(ip_word)}"  is :  {word_count} \n the sentence count is : {sen_count} \n the key word density is : {new}')

if __name__=='__main__':
    app1.run(debug=True)
