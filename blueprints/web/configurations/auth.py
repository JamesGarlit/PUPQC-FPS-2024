from flask import Blueprint, render_template, request, session, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2, psycopg2.extras, re
from blueprints.database.models import db  # Import db and user from models

auth_bp = Blueprint("auth", __name__, template_folder="../templates")

# routes for login page
@auth_bp.route("/", methods=['GET','POST'])
def login():

    cursor = db.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Check if user and pass post request exist
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # # print(username)
        # # print(password)

        # Check if account exist
        cursor.execute(
            'select * from users where username = %s', (username,)
        )
        
        # Find one record and return result
        account = cursor.fetchone()

        if account:
            password_rs = account['password']
            # print(password_rs)

            # if account exist, redirect to dashboard
            if check_password_hash(password_rs, password):
                # create a session data, global data can be accessed on other routes
                session['logged_in'] = True
                session['id'] = account['id']
                session['username'] = account['username']

                # redirect to dashboard
                return redirect(url_for('executives.executive'))
                
        else:
            # No account in db
            flash('Incorrect username and password')

    return render_template('login.html')

# routes for register page
@auth_bp.route("/register", methods=['GET','POST'])
def register():
    cursor = db.conn.cursor(
        cursor_factory=psycopg2.extras.DictCursor
    )

    # check if the username, pass, and email POST request exist (user submitted form)
    if request.method == 'POST':
        # variables
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # print(fullname)
        # print(username)
        # print(password)
        # print(email)
        
        hashed_password = generate_password_hash(password)
        
        # check if account exists using mysql
        db.cursor.execute(
            'SELECT * FROM users WHERE username = %s'
            , (username,)
        )
        account = db.cursor.fetchone()
        # print(account)

        # if account exist show error and validation checks
        if account:
            flash('Account already exist')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address')
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash('Username must contain only characters and numbers')
        elif not username or not password or not email:
            flash('Please fill out the form')
        else:
            # account doesn't exists and the form data is valid, now insert new account into users table
            cursor.execute(
                """
                INSERT INTO users (fullname, username, password, email)
                VALUES (%s, %s, %s, %s)
                """
                , (fullname, username, hashed_password, email)
            )
            db.conn.commit()
            flash('You have successfully registered!')
    elif request.method == 'POST':
        # form is empty
        flash('Please fill out the form!')
    # show registration form with message
    return render_template('register.html')

# routes to logout
@auth_bp.route('/logout')
def logout():
    #remove the session data
    session.pop('logged_in', None)
    session.pop('id', None)
    session.pop('username', None)

    # Kick to login Page
    return redirect(url_for('auth.login'))

