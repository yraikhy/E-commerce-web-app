from flask import Blueprint

main = Blueprint('main', __name__)
shopping_basket = Blueprint('shopping_basket', __name__)

main.register_blueprint(shopping_basket)

from . import routes