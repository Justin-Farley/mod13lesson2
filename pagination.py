from flask import request, jsonify
from app import db
from models import Order, Product

def paginate_orders():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    orders_query = Order.query.paginate(page, per_page, False)
    orders = [order.to_dict() for order in orders_query.items]  
    return jsonify({
        'orders': orders,
        'total': orders_query.total,
        'page': orders_query.page,
        'per_page': orders_query.per_page
    })

def paginate_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    products_query = Product.query.paginate(page, per_page, False)
    products = [product.to_dict() for product in products_query.items]  
    return jsonify({
        'products': products,
        'total': products_query.total,
        'page': products_query.page,
        'per_page': products_query.per_page
    })
