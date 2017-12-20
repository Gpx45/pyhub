from flask import Flask
from vsearch import vsearch

app = Flask(__name__) # These are special values kept by the interpreter values with __ are called dunders while _ is called a wonder double and one underscores.

@app.route('/') # This is called a function decorator which always start with an @ a decorator ajusts the behavior of a function without you having to rewrite it.
def hello() -> str:
    return "Hello World"

@app.route('/search4')
def do_search() ->str:
    return vsearch("life the universe","eiru")

app.run()
