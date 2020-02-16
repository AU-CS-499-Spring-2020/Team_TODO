import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from pycket.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        password = request.form["password"]
        email = request.form["email"]
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        username = firstname.lower() + lastname.lower()
        db = get_db()
        error = None
        
        if not password:
            error = "Password is required."
        elif not email:
            error = "An email is required."
        elif not firstname:
            error = "A first name is required."
        elif not lastname:
            error = "A last name is required."
        elif (
            db.execute("SELECT id FROM user WHERE username = ?", (username,)).fetchone()
            is not None
        ):
            error = "User {0} is already registered.".format(username)

        if error is None:
            db.execute(
                "INSERT INTO user (username, password, email, firstname, lastname) VALUES (?, ?, ?, ?, ?)",
                (username, generate_password_hash(password), email, firstname, lastname),
            )
            db.commit()
            return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/signup.html")

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            error = 'Incorrect email'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)
    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    return wrapped_view