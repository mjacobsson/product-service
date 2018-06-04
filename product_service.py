#!/usr/bin/env python3
from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {
        'id': 1,
        'name': u'Jeans', 
    },
    {
        'id': 2,
        'name': u'Shirt', 
    }
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    product = [p for p in products if p['id'] == int(id)]
    return jsonify(product[0])

if __name__ == '__main__':
    print('Product service listening on port 8007!')
    app.run(port=8007)