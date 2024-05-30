from app import app
from flask import render_template
from models import Kart,Imkan,Tarif,Sans

@app.route('/kartlar/')
def kartlar():
    kartlar = Kart.query.all()
    return render_template("index.html",kartlar = kartlar)


@app.route('/etrafli/<int:kart_id>')
def etrafli(kart_id):
    kart = Kart.query.get_or_404(kart_id)
    imkanlar = Imkan.query.filter_by(kart_id =kart_id).all()
    sanslar = Sans.query.filter_by(kart_id =kart_id).all()
    tarifler = Tarif.query.filter_by(kart_id =kart_id).all()
    return render_template("etrafli.html", kart=kart, imkanlar=imkanlar, tarifler=tarifler, sanslar=sanslar)
    
@app.route('/abb/')
def abb():
    return render_template("main.html")




