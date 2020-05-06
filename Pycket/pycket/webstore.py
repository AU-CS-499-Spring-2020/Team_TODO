from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flask_login import login_required, current_user

from werkzeug.exceptions import abort 

from pycket import app, db
from pycket.models import Product
from pycket.forms import CreateProductForm, EditProductForm

bp = Blueprint('webstore', __name__, template_folder='templates/webstore/')

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

            return redirect(url_for('Webstore.index'))
    return render_template('store_newproduct.html', form=form)

@bp.route('/store/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    if current_user.is_authenticated:
        product = Product.query.filter_by(id=id).first()
        form = EditProductForm(obj=product)
        if form.validate_on_submit():
            form.populate_obj(product)
            db.session.commit()
            return redirect(url_for('webstore.index'))

        return render_template('webstore/store_update_product.html', form=form, product=product)