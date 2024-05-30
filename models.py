from extensions import db, login_manager
from app import app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(200), nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)
    
    def set_password(self, new_password):
        self.password = generate_password_hash(new_password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

class Kart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_filename = db.Column(db.String(100), nullable=True)
    title = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(100), nullable=True)
    desc2 = db.Column(db.String(200), nullable=True)
    price = db.Column(db.String(20), nullable=True)
    button1_text = db.Column(db.String(50), nullable=True)
    button2_text = db.Column(db.String(50), nullable=True)
    category = db.Column(db.String(20), nullable=True)

    @property
    def price_value(self):
        try:
            return float(self.price)
        except ValueError:
            return self.price

    @price_value.setter
    def price_value(self, value):
        self.price = str(value)
        
class Imkan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=True)
    image = db.Column(db.String(100), nullable=True)  
    kart_id = db.Column(db.Integer, db.ForeignKey('kart.id'), nullable=True)
    

class Tarif(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    column1 = db.Column(db.String(200), nullable=True) 
    column2 = db.Column(db.String(500), nullable=True)  
    kart_id = db.Column(db.Integer, db.ForeignKey('kart.id'), nullable=True)
    
    @property
    def price_value(self):
        try:
            return float(self.column2)
        except ValueError:
            return self.column2

    @price_value.setter
    def price_value(self, value):
        self.column2 = str(value)

    @price_value.setter
    def price_value(self, value):
        self.column2 = str(value)


class Sans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sup = db.Column(db.String(10), nullable=True) 
    explanation = db.Column(db.String(500), nullable=True)  
    kart_id = db.Column(db.Integer, db.ForeignKey('kart.id'), nullable=False)

