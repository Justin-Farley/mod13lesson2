from app import db
from sqlalchemy import func
from models import Order, Product, Employee, Customer, Production

def analyze_employee_performance():
    results = db.session.query(
        Employee.name,
        func.sum(Order.quantity).label('total_quantity')
    ).join(Order, Order.product_id == Employee.id).group_by(Employee.id).all()
    return jsonify([{'employee': result[0], 'total_quantity': result[1]} for result in results])

def identify_top_selling_products():
    results = db.session.query(
        Product.name,
        func.sum(Order.quantity).label('total_quantity')
    ).join(Order, Order.product_id == Product.id).group_by(Product.id).order_by(func.sum(Order.quantity).desc()).all()
    return jsonify([{'product': result[0], 'total_quantity': result[1]} for result in results])

def determine_customer_lifetime_value():
    results = db.session.query(
        Customer.name,
        func.sum(Order.total_value).label('total_order_value')
    ).join(Order, Order.customer_id == Customer.id).group_by(Customer.id).having(func.sum(Order.total_value) >= 1000).all()
    return jsonify([{'customer': result[0], 'total_order_value': result[1]} for result in results])

def evaluate_production_efficiency():
    subquery = db.session.query(
        Production.product_id,
        func.sum(Production.quantity).label('total_quantity')
    ).filter(Production.date == '2024-08-19').group_by(Production.product_id).subquery()
    
    results = db.session.query(
        Product.name,
        subquery.c.total_quantity
    ).join(subquery, Product.id == subquery.c.product_id).all()
    
    return jsonify([{'product': result[0], 'total_quantity': result[1]} for result in results])
