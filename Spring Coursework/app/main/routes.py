from flask import render_template, redirect, url_for, session, request
from ..models import Item
from . import main, shopping_basket
from .forms import *


@main.route('/', methods=['GET', 'POST'])
def index():
    if 'basket' not in session:
        session['basket'] = []

    items = Item.query.all()
    form = SubmitForm()

    if request.method == 'POST':
        item_id = request.form['item_id']
        item = Item.query.get(item_id)
        add_to_basket(item)

    return render_template('index.html', items=items, form=form)

@main.route('/items/<int:id>')
def item_detail(id):
    item = Item.query.get_or_404(id)
    form = SubmitForm()

    if request.method == 'POST':
        item_id = request.form['item_id']
        item = Item.query.get(item_id)
        add_to_basket(item)

    return render_template('item_detail.html', item=item, form=form)

@shopping_basket.route('/basket', methods=['GET', 'POST'])
def view_basket():
    basket = session.get('basket')
    total = sum(i['price']*i['quantity'] for i in basket)
    payForm = SubmitForm()

    if request.method == 'POST':
        return redirect(url_for('main.payment', total_price=total))

    return render_template('basket.html', basket=basket, total=total, form=payForm)

@shopping_basket.route('/basket/add/<int:item_id>', methods=['GET', 'POST'])
def add_to_basket(item_id):
    item = Item.query.get_or_404(item_id)
    basket = session.get('basket', [])
    item_exists = False

    for item_dict in basket:
            if item_dict['id'] == item_id:
                item_dict['quantity'] += 1
                item_exists = True
                break

    if item_exists == False:
        basket.append({'id': item_id, 'name': item.name, 'price': item.price, 'quantity': 1})

    session['basket'] = basket
    return redirect(url_for('main.index'))

@shopping_basket.route('/basket/remove/<int:item_id>')
def remove_from_basket(item_id):
    basket = session.get('basket', [])
    for item_dict in basket:
        if item_id == item_dict['id']:
            item_dict['quantity'] -= 1
            if item_dict['quantity'] == 0:
                del basket[basket.index(item_dict)]

    session['basket'] = basket
    return redirect(url_for('main.shopping_basket.view_basket'))

@shopping_basket.route('/basket/clear')
def clear_basket():
    session.pop('basket', None)
    return redirect(url_for('main.shopping_basket.view_basket'))

@main.route('/pay/<int:total_price>', methods=['GET', 'POST'])
def payment(total_price):
    form = payForm()

    if form.validate_on_submit():
        session.pop('basket', None)
        return redirect(url_for('main.payment_complete'))

    return render_template('pay.html', total=total_price, form=form)

@main.route('/order_complete')
def payment_complete():
    return render_template('payment_complete.html')