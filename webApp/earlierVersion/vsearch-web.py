from flask import Flask, render_template,request,redirect
from vsearch import vsearch

app = Flask(__name__) # These are special values kept by the interpreter. Values with __ are called dunders while _ is called a wonder double and one underscores.

@app.route('/') # This is called a function decorator which always start with an @ a decorator ajusts the behavior of a function without you having to rewrite it.
def hello() -> 302:
    return redirect('/entry')


@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html',the_title='Welcome to search4letters Online')


@app.route('/search4', methods = ['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "Here are your results: "
    results = str(vsearch(phrase,letters))
    return render_template('result.html',
        the_phrase = phrase,
        the_letters = letters,
        the_title = title,
        the_results = results,)



if __name__ == '__main__':
    app.run(debug=True)
