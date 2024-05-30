from flask import Flask
from flask import  render_template 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/mydb'
app.config['SECRET_KEY'] = 'our_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from models import *
from extentions import *
from controllers import *




if __name__ == '__main__':
    app.init_app(app)
    app.init_app(migrate)
    app.run(port=5000,debug=True)