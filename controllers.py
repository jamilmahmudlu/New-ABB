from app import app
from flask import  render_template, request, redirect
from form import *
from models import *

@app.route('/abb/')
def abb():
    return render_template("style.html")

@app.route('/kreditler/')
def kreditler():
    kreditler = Online.query.all()
    return render_template("kredit.html", kreditler = kreditler)

@app.route('/etrafli-kreditler/<int:kredit_id>')
def etrafli_kreditler(kredit_id):
    etraflikreditler = Etrafli1.query.get_or_404(kredit_id)
    return render_template("online-kredit.html", etraflikreditler = etraflikreditler)

@app.route('/kampaniyalar/')
def kampaniyalar():
    kampaniyalar = Kampaniya.query.all()
    return render_template("kampaniyalar.html", kampaniyalar = kampaniyalar)

@app.route('/etrafli-kampaniyalar/<int:kampaniya_id>')
def etrafli_kampaniyalar(kampaniya_id):
    kampaniyalar = Kampaniya.query.all(kampaniya_id)
    sertler = Sertler.query.filter_by(kampaniya_id = kampaniya_id).all()
    return render_template("etrafli-kampaniya.html", kampaniyalar = kampaniyalar, sertler = sertler)

@app.route('/register/', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    my_data = request.form

    if request.method == 'POST':
        form  = RegisterForm(data = my_data)
        if form.validate_on_submit():
            my_new_user = UserKredit(first_name = form.first_name.data, last_name = form.last_name.data, phone = form.phone.data, fin_code = form.fin_code.data )
            my_new_user.save()
        return redirect ('/kreditler/')
    return render_template('register.html', form = form)