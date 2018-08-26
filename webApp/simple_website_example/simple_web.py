from flask import Flask, session

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello from My Webpage'


@app.route('/page1')
def page1() -> str:
    return 'Hello from Page 1'


@app.route('/page2')
def page2() -> str:
    return 'Hello from Page 2'


@app.route('/page3')
def page3() -> str:
    return 'Hello from Page 3'


app.secret_key = 'TheSecretKey' # -> This is for sessions to initialize
# Login page that has a set session key 'logged_in' to True to state the account is logged in.
@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout() -> str:
    if session['logged_in'] == True:
        session.pop('logged_in')
    return 'You are now logged out'


@app.route('/checkstatus')
def checkstatus() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in.'
    return 'You are now logged out'


if __name__ == '__main__':
    app.run(debug=True)
