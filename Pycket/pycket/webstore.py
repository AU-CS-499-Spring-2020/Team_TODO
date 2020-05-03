from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flask_login import login_required, current_user

from werkzeug.exceptions import abort 

from pycket import app, db
from pycket.models import Product
from pycket.forms import CreateProductForm

bp = Blueprint('Webstore', __name__, template_folder='templates/webstore/')

@bp.route('/store/index')
@login_required
def index():
    items = ['Item 1', 'Item 1', 'Item 1', 'Item 1', 'Item 1', 'Item 1', 'Item 1']
    return render_template('store_home.html', title="Products", items=items)

@bp.route('/store/create', methods=('GET', 'POST'))
@login_required
def create():
    if current_user.is_authenticated:
        form = CreateProductForm()
        if form.validate_on_submit():
            product = Product(
                item_name=form.item_name.data,
                price=form.price.data,
                category=form.category.data,
                description=form.description.data
            )
        
            db.session.add(product)
            db.session.commit()

            return redirect(url_for('product.index'))
    return render_template('store_newproduct.html', form=form)