#!/usr/bin/python3
from vsearch import vsearch
from flask import Flask, render_template, request, escape
from  DB import Database
from datetime import datetime

app = Flask(__name__)

# These are special values kept by the interpreter.
# Values with __ are called dunders while _ is called a wonder double and one
# underscores.


# We can have more than one URL be associated with a function, this is so you
# don't have to import if you don't need to.

# def log_request(req: 'flask_request', res: str)-> None:
#    with open('vsearch.log', 'a') as log:
#        print(req.form, req.remote_addr, req.user_agent, res, sep='|', file=log)

app.config['dbconfig'] = {'host': 'localhost',
                          'user': 'root',
                          'password': '',
                          'db': 'logdb'}

# The log_request function is where the values are sent and then placed on the log table inside the logdb database.
def log_request(req: 'flask request', res: str)-> None:
    with Database(app.config['dbconfig']) as cursor:
        _sql = """insert into log
        (phrase, letters, ip, browser_string, results)
        values (%s, %s, %s, %s, %s)"""
        cursor.execute(_sql, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, ))
    # The context manager is to simply write all of the values onto a log file logdb.log
    with open('logdb.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent.browser, res, sep='|',
              file=log)

# Entrance to the website.
@app.route('/')
@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html', the_title='Welcome to search4letters Online')

# In search4 is where the results are sent the server and the vsearch distributed package runs to compute a value.
@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "Here are your results: "
    results = str(vsearch(phrase, letters))
    log_request(request, results) # --> Here is where the values are sent the database object that then stores in MySQL
    return render_template('result.html',
                           the_phrase = phrase,
                           the_letters = letters,
                           the_title = title,
                           the_results = results,)

# This webpage retrieves the same information but querying the Database instead of making a file.
@app.route('/viewlog')
def view_the_log() -> 'html':
    with Database(app.config['dbconfig']) as cursor:
        _sql = """select phrase, letters, ip, browser_string, results, time_date
        from log"""
        cursor.execute(_sql)
        contents = cursor.fetchall()
    titles = ('Phrase','Letters', 'Remote Address', 'User Agent', 'Results', 'Time')
    return render_template('viewlog.html', the_title = "View Log",
                           the_row_titles = titles,
                           the_data = contents,)

# If this file is ran as is it'll run in debug mode, if called from another object and or function it'll run without dubug mode on.
if __name__ == '__main__':
    app.run(debug=True)
