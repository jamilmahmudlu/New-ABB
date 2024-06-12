from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db, login_manager


class Online(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(500), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Integer, nullable = True)
    month = db.Column(db.Integer, nullable = True)
    percent = db.Column(db.Integer, nullable = True)
    button_1 = db.Column(db.String(50), nullable = True)
    button_2 = db.Column(db.String(50), nullable = False)  

class Etrafli1(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = True)
    title_mini = db.Column(db.String(100), nullable = True)
    title_mini_2 = db.Column(db.String(100), nullable = True)
    title_mini_3 = db.Column(db.String(100), nullable = True)
    title_mini_4 = db.Column(db.String(100), nullable = True)
    title_mini_5 = db.Column(db.String(100), nullable = True)
    description = db.Column(db.String(50), nullable = True)
    description_2 = db.Column(db.String(50), nullable = True)
    description_3 = db.Column(db.String(50), nullable = True)
    button = db.Column(db.String(50), nullable = True)

class Kampaniya(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(500), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(50), nullable = False)
    description_2  = db.Column(db.String(50), nullable = False)

class Sertler(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(50), nullable = False)
    kampaniya_id = db.Column(db.Integer, db.ForeignKey('kampaniya.id'), nullable=True)

class UserKredit(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(40), nullable = False)
    last_name = db.Column(db.String(40), nullable = False)
    phone = db.Column(db.Integer, nullable = False)
    fin_code = db.Column(db.Integer, nullable = False)

    def __init__(self,first_name,last_name,phone,fin_code):
        self.first_name=first_name
        self.last_name=last_name
        self.phone=phone
        self.fin_code=fin_code

    def save(self):
        db.session.add(self)
        db.session.commit()


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

