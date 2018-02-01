#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response
from flask import request
 
products = [
    {
        'id': 1000,
        'title': 'Stabilo kalem seti',
        'description': '16li renk paketi', 
        'price': 50,
        'category':'Kirtasiye',
        'inStock':True
    },
    {
        'id': 1002,
        'title': 'Python Programming',
        'description': 'Python programlama ile ilgili giris seviye kitap', 
        'price': 60,
        'category':'Kitap',
        'inStcok':False
    },
    {
        'id': 1003,
        'title': 'Mini iPod',
        'description': '80 Gb Kapasiteli MP3 Calar', 
        'price': 200,
        'category':'Elektronik',
        'inStock':True
    }
]
 
app = Flask(__name__)
 
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({'products': products})
 
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        return jsonify({'product': 'Not found'}),404
    return jsonify({'product': product})
 
@app.route('/api/products', methods=['POST'])
def create_product():
    newProduct = {
        'id': products[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json['description'],
        'price':request.json.get('price', 1),
        'category':request.json['category'],
        'inStock': request.json.get('inStock', False)
    }
    products.append(newProduct)
    return jsonify({'product': newProduct}), 201
 
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        return jsonify({'product': 'Not found'}), 404
    products.remove(product[0])
    return jsonify({'result': True})

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        return jsonify({'product': 'Not found'}), 404
    product = product[0]
    product["title"] = request.json['title']
    product["description"] = request.json['description']
    product["price"] = request.json['price']
    product["category"] = request.json['category']
    product["inStock"] = request.json['inStock']
    return jsonify({'product': product})
 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'HTTP 404 Error': 'The content you looks for does not exist. Please check your request.'}), 404)
 
if __name__ == '__main__':
    app.run(debug=True)#!flask/bin/python