from flask import Flask, redirect, request, render_template, abort, session
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/mydb'
app.config['SECRET_KEY'] = 'our_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

admin = Admin(app)
from models import *
from extensions import *
from controllers import *

class SecureModelView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)

admin.add_view(SecureModelView(User, db.session))
admin.add_view(SecureModelView(Kart, db.session))
admin.add_view(SecureModelView(Imkan, db.session))
admin.add_view(SecureModelView(Sans, db.session))
admin.add_view(SecureModelView(Tarif, db.session))
admin.add_view(SecureModelView(Online, db.session))
admin.add_view(SecureModelView(Etrafli1, db.session))
admin.add_view(SecureModelView(Kampaniya, db.session))
admin.add_view(SecureModelView(Sertler, db.session))
admin.add_view(SecureModelView(UserKredit, db.session))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get("username") == "admin" and request.form.get("password") == "admin1234":
            session['logged_in'] = True
            return redirect('/admin/')
        else:
            return render_template("login.html", failed=True)
    return render_template("login.html")

@app.route('/logout/')
def logout():
    session.clear()
    return 'Logged out.'

if __name__ == '__main__':
    db.init_app(app)
    migrate.init_app(app, db)
    app.run(port=5000, debug=True)
