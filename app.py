from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pagination import paginate_orders, paginate_products
from queries import (
    analyze_employee_performance,
    identify_top_selling_products,
    determine_customer_lifetime_value,
    evaluate_production_efficiency
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///factory.db'
db = SQLAlchemy(app)

@app.route('/orders', methods=['GET'])
def get_orders():
    return paginate_orders()

@app.route('/products', methods=['GET'])
def get_products():
    return paginate_products()


@app.route('/analyze_employee_performance', methods=['GET'])
def analyze_employee():
    return analyze_employee_performance()

@app.route('/top_selling_products', methods=['GET'])
def top_selling_products():
    return identify_top_selling_products()

@app.route('/customer_lifetime_value', methods=['GET'])
def customer_lifetime_value():
    return determine_customer_lifetime_value()

@app.route('/production_efficiency', methods=['GET'])
def production_efficiency():
    return evaluate_production_efficiency()

if __name__ == '__main__':
    app.run(debug=True)
