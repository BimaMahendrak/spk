from flask import render_template, request, redirect, url_for
from app import app


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/proses', methods=['GET','POST'])
def input():
    if request.method == 'POST':
        harga = request.form['harga']
        if harga < 0:
            harga = 0
        elif harga > 20000000:
            harga = 20000000
        jarak = request.form['jarak']
        if jarak < 0:
            jarak = 0
        elif jarak > 60:
            jarak = 60
        waktu = request.form['waktu']
        if waktu < 0:
            waktu = 0
        elif waktu > 3:
            waktu = 3
        result="Halo"
        return render_template('hasil.html', jawaban=result)
    return render_template('input_data.html')

