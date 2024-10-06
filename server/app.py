from flask import Flask, render_template, jsonify
from flask_migrate import Migrate
from model import db, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app,db)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/products')
def display_products():
    products = Product.query.all()
    return render_template('products.html', products=products)
@app.route('/json_products')
def product_json():
    products = Product.query.all()
    product_list = [product.to_dict() for product in products]
    return jsonify(product_list), 200


if __name__ == '__main__':
    app.run(port=5555,debug=True)

