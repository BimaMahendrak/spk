from flask import render_template, request, redirect, url_for
from app import app
from .rumus.hasil import inferensi

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/proses', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        nama = request.form['nama']

        harga = request.form['harga']
        hargaa = float(harga)
        if hargaa < 0:
            hargaa = 0
        elif hargaa > 20000000:
            hargaa = 20000000
            
        jarak = request.form['jarak']
        jarakk = float(jarak)
        if jarakk < 0:
            jarakk = 0
        elif jarakk > 60:
            jarakk = 60
        
        waktu = request.form['waktu']
        waktuu = float(waktu)
        if waktuu < 0:
            waktuu = 0
        elif waktuu > 3:
            waktuu = 3

        result, data= inferensi(hargaa, jarakk, waktuu)
        harga = f"{int(harga):,}".replace(",", ".") 
        return render_template('hasil.html', jawaban=result, nama=nama, harga=harga, jarak=jarak, waktu=waktu, data=data)
    return render_template('input_data.html')