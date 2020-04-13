from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flask_login import login_required, current_user

from werkzeug.exceptions import abort 

from pycket import app, db
from pycket.models import Product
from pycket.forms import CreateTicketForm

bp = Blueprint('Webstore', __name__, template_folder='templates/webstore/')

@bp.route('/store/index')
@login_required
def index():
    return render_template('store_home.html')