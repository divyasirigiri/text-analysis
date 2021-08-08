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
    ip2 = request.form.get('ip2')
    text = TextBlob(ip_word)
    
    
    freq = FreqDist(nltk.word_tokenize(ip_word))
    new = {}
    if ip2=="Keyword Density":
        word_count = len(text.words)
        for i in text.words:
            if i not in new:
                new[i] = freq[i]
        for i in new:
            new[i] = str(round((new[i]/word_count)*100,2))+"%"
        res = new
    elif ip2=="Word Count":
        word_count = len(text.words)
        res=word_count

    elif ip2=="Sentence Count":
        sen_count = len(text.sentences)
        res = sen_count
    elif ip2=="Character Count":
        res = len(ip_word)

    return render_template('base.html',translated_text=f'\n the "{(ip2)}" in the given text is :  {res}')

if __name__=='__main__':
    app1.run(debug=True)
