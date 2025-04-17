from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS  # Для обработки CORS-запросов от Mini App

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)


PRODUCTS = [
    {"id": 1, "title": "Товар 1", "price": 100, "description": "Описание товара 1"},
    {"id": 2, "title": "Товар 2", "price": 200, "description": "Описание товара 2"},
    {"id": 3, "title": "Товар 3", "price": 150, "description": "Описание товара 3"},
]

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Эндпоинт для получения списка всех товаров
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(PRODUCTS)

# Эндпоинт для получения информации о конкретном товаре по ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Товар не найден"}), 404

# Эндпоинт для добавления товара в корзину (пример обработки POST-запроса)
@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    if not data or 'product_id' not in data:
        return jsonify({"error": "Некорректные данные запроса"}), 400

    product_id = data['product_id']

    print(f"Товар с ID {product_id} добавлен в корзину (сервер)")
    return jsonify({"message": f"Товар с ID {product_id} успешно добавлен в корзину"})

# Эндпоинт для оформления заказа (пример обработки POST-запроса)
@app.route('/api/orders/create', methods=['POST'])
def create_order():
    data = request.get_json()
    if not data or 'items' not in data or 'user_id' not in data:
        return jsonify({"error": "Некорректные данные заказа"}), 400

    items = data['items']  # Список ID товаров и их количество
    user_id = data['user_id']

    print(f"Создан заказ для пользователя {user_id} с товарами: {items} (сервер)")
    return jsonify({"message": f"Заказ для пользователя {user_id} успешно создан"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
