from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

from pycket.auth import login_required
from pycket.db import get_db

bp = Blueprint('ticket', __name__, template_folder='templates')

@bp.route('/ticket/index')
@login_required
def index():
    db = get_db()
    tickets = db.execute(
        'SELECT p.id, title, body, created, creator_id, username'
        ' FROM ticket p JOIN user u ON p.creator_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('ticket/product.html', posts=tickets)

@bp.route('/ticket/create', methods=('GET', 'POST'))
@login_required
def create():
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
                'INSERT INTO ticket (title, body, author_id)'
                ' Values (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('ticket.index'))
    
    return render_template('ticket/create_ticket.html')

def get_ticket(id, check_author=True):
    ticket = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM ticket p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if ticket is None:
        abort(404, "Ticket id {0} doesn't exist.".format(id))

    if check_author and ticket['author_id'] != g.user['id']:
        abort(403)

    return ticket

@bp.route('/ticket//<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    ticket = get_ticket(id)

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

    return render_template('ticket/edit_ticket.html', post=ticket)

@bp.route('/ticket/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_ticket(id)
    db = get_db()
    db.execute('DELETE FROM ticket WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('ticket.index'))