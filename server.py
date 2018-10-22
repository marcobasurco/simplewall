from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL as connect
from flask_bcrypt import Bcrypt
import math
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Za-z ]+')


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "superSecretNSAkey"


@app.route("/")
def index():
    print(session)
    return render_template('index.html')


@app.route("/register", methods=['POST'])
def register():

    # validattion check for first Name
    if len(request.form['first_name']) == 0:
        flash('First Name is required', 'first_name')
    elif len(request.form['first_name']) < 2:
        flash('First Name must have minimum 2 characters', 'first_name')

    # validattion check for last Name
    if len(request.form['last_name']) == 0:
        flash('Last Name is required', 'last_name')
    elif len(request.form['last_name']) < 2:
        flash('Last Name must have minimum 2 characters', 'last_name')

   # I am checking email address if is already taken
    mysql = connect('quotes_wall')
    query = "SELECT * FROM users WHERE email = %(email)s"
    data = {'email':   request.form['email']}
    email_check = mysql.query_db(query, data)

    print ('>>>>>>>>>>>>>>>>>>>>>>>>>   GETTING EMAIL FOR VALIDATION>>>>>>>>>>>>>>>>>>>>', email_check)

    if len(request.form['email']) == 0:
        flash('Email address is required', 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email', 'email')
    elif len(email_check) > 0:
        flash('Email already taken', 'email')

    # # validation for password
    if len(request.form['password']) == 0:
        flash('Password is required', 'password')
    elif len(request.form['password']) < 8:
        flash('Password must be at least 8 characters', 'password')
    elif not re.search('[0-9]', request.form['password']):
        flash('Password must have at leat one number', 'password')
    elif not re.search('[A-Z]', request.form['password']):
        flash('Password must have at least one Capital letter', 'password')
    elif request.form['password'] != request.form['confirm_password']:
        flash('Password must match', 'confirm_password')

    if '_flashes' in session.keys():
        session['first_name'], session['last_name'], session['email'] = request.form['first_name'], request.form['last_name'], request.form['email']
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    mysql = connect('quotes_wall')
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
    data = {
        'first_name':   request.form['first_name'],
        'last_name':   request.form['last_name'],
        'email':   request.form['email'],
        'password':   pw_hash
    }
    new_member_id = mysql.query_db(query, data)
    session['new_member_id'] = new_member_id

    print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', session['new_member_id'])

    debugHelp("REGISTER METHOD")
    return redirect('/')


@app.route("/login", methods=['POST'])
def login():
    session.clear()

    mysql = connect('quotes_wall')
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {
        'email':   request.form['email'],
    }
    results = mysql.query_db(query, data)

    if len(request.form['email']) == 0:
        flash('Email address is required', 'email_login')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email', 'email_login')
    if len(request.form['password']) == 0:
        flash('Password is required to login', 'password_required')

    if results:

        if bcrypt.check_password_hash(results[0]['password'], request.form['password']):
            session['id'] = results[0]['id']
            session['first_name'] = results[0]['first_name']
            session['last_name'] = results[0]['last_name']
            return redirect('/quotes')
        else:
            flash('You could not be logged in', 'failed_login')
            return redirect("/")
    else:
        flash('You could not be logged in', 'failed_login')

        return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

    

@app.route("/quotes")
def quotes():
    if 'id' not in session:
        session.clear()
        return redirect('/')


 
    return render_template('quotes.html')


@app.route("/user_quotes")
def user_quotes():
    if 'id' not in session:
        session.clear()
        return redirect('/')
    print("session[id]: ", session['id'])

    return render_template('user_quotes.html')


@app.route("/edit")
def edit():
    if 'id' not in session:
        session.clear()
        return redirect('/')
    print("session[id]: ", session['id'])




    return render_template('edit.html')





@app.route("/send/<id>", methods=['POST'])
def send(id):
  
    return redirect('/quotes')






@app.route('/delete')
def delete(id):

    return redirect('/quotes')






def debugHelp(message=""):
    print("\n\n-----------------------------------------",
          message, "-----------------------------------------")
    print("REQUEST.FORM:", request.form)
    print("SESSION:", session)


if __name__ == "__main__":
    app.run(debug=True)
