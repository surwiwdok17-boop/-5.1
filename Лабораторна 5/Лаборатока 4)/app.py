from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, Product, Order, Feedback, Client
from routes import blueprints
from routes.admin import init_admin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

for bp in blueprints:
    app.register_blueprint(bp)

init_admin(app)

# Картинки для головної сторінки
images = [
    "https://cloudy.kyiv.ua/image/cache/catalog/products/Rdini/Zhizha-NOVA-Red-Bull-Blue-Raspberry-Salt-30ml-65mg-870x1131.jpg",
    "https://uestore.in.ua/image/cache/catalog/doublerasp-600x600-900x900.jpg",
    "https://v7par.com.ua/image/cache/catalog/1212/disposablle/elfbarrr/geekbar/2022-09-08%2012.35.34-650x650.jpg",
    "https://vapehub.shop/image/cache/catalog/import_files/51/51785680820711edfc8700505687efca_b93a26048f6811edcd9600505687efca-600x600.jpg",
    "https://uestore.in.ua/image/cache/catalog/pineapplelemonade-600x600-900x900.jpg",
    "https://vapehub.shop/image/cache/catalog/liquid/nova%2030/peach-mang-600x600.jpg",
    "https://v7par.org.ua/image/cache/catalog/1212/disposablle/elfbarrr/geekbar/2-650x650.jpg",
]
index = 0

@app.route('/')
def home():
    global index
    image_url = images[index]
    index = (index + 1) % len(images)
    return render_template('home.html', image_url=image_url)

@app.route('/about')
def about():
    return render_template('about.html')

def seed_products():
    with app.app_context():
        if Product.query.count() == 0:
            items = [
                {"name": "Double Raspberry", "price": 129.0, "image_url": images[1]},
                {"name": "Peach Mango", "price": 139.0, "image_url": images[5]},
                {"name": "GoldBar Grape", "price": 149.0, "image_url": images[2]},
                {"name": "Red Bull Blue Raspberry", "price": 159.0, "image_url": images[0]},
                {"name": "Pineapple Lemonade", "price": 119.0, "image_url": images[4]},
                {"name": "Geekbar Assorted", "price": 99.0, "image_url": images[6]},
            ]
            for it in items:
                db.session.add(Product(name=it["name"], price=it["price"], image_url=it["image_url"]))
            db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_products()
    app.run(debug=True)
