from flask import render_template, flash, redirect, url_for, request, Blueprint
from pycket import app, db
from pycket.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from pycket.models import User
from werkzeug.urls import url_parse

bp = Blueprint('auth', __name__, template_folder='templates/auth/')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
<<<<<<< HEAD
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            error = 'Incorrect Email'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect Password'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('ticket.index'))
        
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
=======
    if current_user.is_authenticated:
        return redirect(url_for('ticket.index'))
    form = LoginForm()
    if form.validate_on_submit():
       user = User.query.filter_by(email=form.email.data).first()
       if user is None or not user.check_password(form.password.data):
           flash('Invalid username or password')
           return redirect(url_for('login'))
       login_user(user, remember=form.remember_me.data)
       next_page = request.args.get('next')
       if not next_page or url_parse(next_page).netloc != '':
           next_page = url_for('ticket.index')
       return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
>>>>>>> 047946502c924afb77228860b23f4ac2bbc64d63
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
