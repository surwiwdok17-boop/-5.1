from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, Product, Order, Feedback, Client

def init_admin(app):
    admin = Admin(app)
    admin.add_view(ModelView(Feedback, db.session))
    admin.add_view(ModelView(Product, db.session))
    admin.add_view(ModelView(Order, db.session))
    admin.add_view(ModelView(Client, db.session))
