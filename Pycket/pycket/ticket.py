from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flask_login import login_required, current_user

from werkzeug.exceptions import abort 

from pycket import app, db
from pycket.models import Ticket
from pycket.forms import CreateTicketForm, EditTicketForm

bp = Blueprint('ticket', __name__, template_folder='templates/ticket/')

@bp.route('/ticket/index')
@login_required
def index():
    tickets = Ticket.query.all()

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

@bp.route('/ticket/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    if current_user.is_authenticated:
        ticket = Ticket.query.filter_by(id=id).first()
        form = EditTicketForm(obj=ticket)
        if form.validate_on_submit():
            form.populate_obj(ticket)
            db.session.commit()
            return redirect(url_for('ticket.index'))

        return render_template('ticket/ticket_edit.html', form=form, ticket=ticket)
