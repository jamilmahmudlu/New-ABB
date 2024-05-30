from extentions import db
from flask_login import UserMixin

class Online(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(500), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    month = db.Column(db.Integer, nullable = False)
    percent = db.Column(db.Integer, nullable = False)
    button_1 = db.Column(db.String(50), nullable = False)
    button_2 = db.Column(db.String(50), nullable = False)  

class Etrafli1(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    title_mini = db.Column(db.String(100), nullable = False)
    title_mini_2 = db.Column(db.String(100), nullable = False)
    title_mini_3 = db.Column(db.String(100), nullable = False)
    title_mini_4 = db.Column(db.String(100), nullable = False)
    title_mini_5 = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(50), nullable = False)
    description_2 = db.Column(db.String(50), nullable = False)
    description_3 = db.Column(db.String(50), nullable = False)
    button = db.Column(db.String(50), nullable = False)

class Kampaniya(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(500), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(50), nullable = False)
    description_2  = db.Column(db.String(50), nullable = False)

class Sertler(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(50), nullable = False)

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
