from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    c_password = request.form['c_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    c_password_error = ''
    email_error = ''

    if username == '' or (' ' in username) or len(username) < 3 or len(username) > 20:
        username_error = "That's not a valid username"
    if password == '' or (' ' in password) or len(password) < 3 or len(password) > 20:
        password_error = "That's not a valid password"
    if c_password == '':
        c_password_error = "That's not a valid password"
    if c_password != password:
        c_password_error = "Passwords don't match"
    if email != '' and (email.count("@") != 1 or email.count(".") != 1 or (' ' in email) or len(email) < 3 or len(email) > 20):
        email_error = "That's not a valid email"


    if not username_error and not password_error and not c_password_error and not email_error:
        return redirect('/welcome?username=' + username)
    else:
        return render_template('index.html',
            username = username,
            email = email,
            username_error = username_error,
            password_error = password_error,
            c_password_error = c_password_error,
            email_error = email_error)


@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


@app.route("/")
def index():
    return render_template('index.html')


app.run()
