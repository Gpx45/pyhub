 #!/usr/bin/python3
from vsearch import vsearch
from flask import Flask, render_template, request, escape, session, copy_current_request_context
from  DB import Database, ConnectionError, CredentialsError, SQLError
from datetime import datetime
from checker import check_logged_in
from time import sleep
from threading import Thread

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

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are logged in'

@app.route('/logout')
def do_logout() -> str:
    session.pop['logged_in']
    return 'You are now logged out'

# The log_request function is where the values are sent and then placed on the log table inside the logdb database.

# Entrance to the website.
@app.route('/')
@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html', the_title='Welcome to search4letters Online')

# In search4 is where the results are sent the server and the vsearch distributed package runs to compute a value.
@app.route('/search4', methods=['POST'])
def do_search() -> 'html':

    @copy_current_request_context # Holds onto the variables values afterthe thread starts so that it remains even after the function ends.
    def log_request(req: 'flask request', res: str)-> None:
        # raise Exception("Something awful happened.")  # A custom created exception. Its only an example.
        #sleep(15) # --> This is emulate a delay on the site.
            with Database(app.config['dbconfig']) as cursor:
                _sql = """insert into log
                (phrase, letters, ip, browser_string, results)
                values (%s, %s, %s, %s, %s)"""
                cursor.execute(_sql, (req.form['phrase'],
                                      req.form['letters'],
                                      req.remote_addr,
                                      req.user_agent.browser,
                                      res, ))

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "Here are your results: "
    results = str(vsearch(phrase, letters))


    try:
        t = Thread(target=log_request, args=(request,results)) # Created a Thread object so that the call would allow the website to continue without being held up.
        t.start() # --> Here is where the values are sent the database object that then stores in MySQL

    except ConnectionError as err:
        print("Database could not be reached. Error: ", str(err))
    except CredentialsError as err:
        print("UserID/Password is incorrect: ", str(err))
    except SQLError as err:
        print("Is your query correct? Error: ", str(err))
    except Exception as err:
        print("Just an unknown Error: ", str(err))

    return render_template('result.html',
                           the_phrase = phrase,
                           the_letters = letters,
                           the_title = title,
                           the_results = results,)


# This webpage retrieves the same information but querying the Database instead of making a file.
@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    try:
        with Database(app.config['dbconfig']) as cursor:
            _sql = """select phrase, letters, ip, browser_string, results, time_date
            from log"""
            cursor.execute(_sql)
            contents = cursor.fetchall()
        titles = ('Phrase','Letters', 'Remote Address', 'User Agent', 'Results', 'Time')

    except ConnectionError as err:
        print("Is the database on? Error: ", str(err))
    except CredentialsError as err:
        print("UserID/Password is incorrect: ", str(err))
    except SQLError as err:
        print("Is your query correct? Error: ", str(err))
    except Exception as err:
        print("Just an unknown Error: ", str(err))


    return render_template('viewlog.html', the_title = "View Log",
                           the_row_titles = titles,
                           the_data = contents,)


app.secret_key = 'YouWillNeverGuessMySecretKey'
# If this file is ran as is it'll run in debug mode, if called from another object and or function it'll run without dubug mode on.
if __name__ == '__main__':
    app.run(debug=True)
