from flask import Blueprint, render_template, session, redirect, url_for, request
import psycopg2, psycopg2.extras
from blueprints.database.models import db

exec_bp = Blueprint("executives", __name__, template_folder="../templates")

# routes to dashboard (Executive)
@exec_bp.route('/executive')
def executive():
    cursor = db.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if 'logged_in' in session:
        cursor.execute(
            'SELECT * FROM users WHERE id = %s'
            , [session['id']]
        )
        account = cursor.fetchone()       
        
        return render_template('users/executives/exec_dashboard.html', username=session['username'], fullname=account['fullname'])

    return redirect(url_for('auth.login'))

# routes to profile (Executive)
@exec_bp.route('/executive_profile')
def executive_profile():
    cursor = db.conn.cursor(
        cursor_factory=psycopg2.extras.DictCursor
    )

    # Check if user is logged in
    if 'logged_in' in session:
        cursor.execute(
            'SELECT * FROM users WHERE id = %s'
            , [session['id']]
        )
        account = cursor.fetchone()

        # Show the profile page with account info
        return render_template('users/executives/exec_profile.html', account = account)
    
    # if user is not logged in, redirect to login page
    return redirect(url_for('login'))