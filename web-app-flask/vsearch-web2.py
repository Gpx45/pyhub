#!/usr/bin/python3
from flask import Flask, render_template, request, escape
from vsearch import vsearch
import pymysql

app = Flask(__name__)
# These are special values kept by the interpreter.
# Values with __ are called dunders while _ is called a wonder double and one
# underscores.


# We can have more than one URL be associated with a function, this is so you
# don't have to import if you don't need to.

# def log_request(req: 'flask_request', res: str)-> None:
#    with open('vsearch.log', 'a') as log:
#        print(req.form, req.remote_addr, req.user_agent, res, sep='|', file=log)


def log_request(req: 'flask request', res: str)-> None:
    dbconfig = {'host': 'localhost', 'user': 'vsearch', 'password': 'password',
                'db': 'vsearchlogdb'}
    db = pymysql.connect(**dbconfig)
    _sql = """insert into log
    (phrase, letters, ip, browser_string, results)
    values (%s, %s, %s, %s, %s)"""
    with db.cursor() as cursor:
        cursor.execute(_sql, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, ))
    db.commit()
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent.browser, res, sep='|',
              file=log)


@app.route('/')
@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html', the_title='Welcome to search4letters Online')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "Here are your results: "
    results = str(vsearch(phrase, letters))
    log_request(request, results)
    return render_template('result.html',
                           the_phrase = phrase,
                           the_letters = letters,
                           the_title = title,
                           the_results = results,)


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title = "View Log",
                           the_row_titles = titles,
                           the_data = contents,)


if __name__ == '__main__':
    app.run(debug=True)
