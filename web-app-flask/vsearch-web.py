from flask import Flask, render_template
from vsearch import vsearch

app = Flask(__name__) # These are special values kept by the interpreter. Values with __ are called dunders while _ is called a wonder double and one underscores.

@app.route('/') # This is called a function decorator which always start with an @ a decorator ajusts the behavior of a function without you having to rewrite it.
def hello() -> str:
    return "Hello World"

@app.route('/search4')
def do_search() ->str:
    return str(vsearch("life the universe","eiru"))

@app.route('/entry')
def entry_page() ->str:
    return render_template('entry.html',the_title='Welcome to search4letters Online')

app.run()
