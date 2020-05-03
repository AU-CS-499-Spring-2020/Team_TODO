from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flask_login import login_required, current_user

from werkzeug.exceptions import abort 

from pycket import app, db
from pycket.models import Ticket
from pycket.forms import CreateTicketForm

bp = Blueprint('ticket', __name__, template_folder='templates/ticket/')

@bp.route('/ticket/index')
@login_required
def index():
    tickets = [
        {
            "id": "1", 
            "firstname": "Dan", 
            "lastname": "Danson",
            "phone_number": "123456789",
            "location": "Someplace, Somestate",
            "Subject": "This is ticket 1",
            "description": "Please resolve this soon.. :(",
        }, 
        {
            "id": "2", 
            "firstname": "Jan", 
            "lastname": "Janson",
            "phone_number": "223456789",
            "location": "Someplace, Somestate",
            "Subject": "This is ticket 2",
            "description": "Please resolve this soon.. :(",
        }
    ]

    return render_template('ticket_home.html', tickets=tickets)

@bp.route('/ticket/create', methods=('GET', 'POST'))
@login_required
def create():
    if current_user.is_authenticated:
        form = CreateTicketForm()
        if form.validate_on_submit():
            ticket = Ticket(
                firstname=form.firstname.data,
                lastname=form.lastname.data,
                phone_number=form.phone_number.data,
                email=form.email.data,
                location=form.location.data,
                subject=form.subject.data,
                description=form.description.data,
                user_id=1
            )

            db.session.add(ticket)
            db.session.commit()
            return redirect(url_for('ticket.index'))
        return render_template('ticket_create.html', title='Create Ticket', form=form)

# @login_required
# def get_ticket(id, check_author=True):
#     ticket = get_db().execute(
#         'SELECT p.id, title, body, created, author_id, username'
#         ' FROM ticket p JOIN user u ON p.author_id = u.id'
#         ' WHERE p.id = ?',
#         (id,)
#     ).fetchone()

#     if ticket is None:
#         abort(404, "Ticket id {0} doesn't exist.".format(id))

#     if check_author and ticket['author_id'] != g.user['id']:
#         abort(403)

#     return ticket

@bp.route('/ticket//<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    ticket = Ticket.query.filter_by(id=id).first()

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE ticket SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('ticket.index'))

    return render_template('ticket/ticket_edit.html', ticket=ticket)

@bp.route('/ticket/<int:id>/archive', methods=('POST',))
@login_required
def archive(id):
    get_ticket(id)
    db = get_db()
    db.execute('DELETE FROM ticket WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('index'))