from flask import render_template, request, redirect, url_for
from app import app
from .rumus.hasil import inferensi

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/proses', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
<<<<<<< Updated upstream
        try:
            harga = int(request.form['harga'])  # Convert to integer
        except ValueError:
            harga = 0  # Handle invalid input (e.g., non-integer input)

        # Ensure harga is within the valid range
        if harga < 0:
            harga = 0
        elif harga > 20000000:
            harga = 20000000
            
        try:
            jarak = int(request.form['jarak'])  # Convert to integer
        except ValueError:
            jarak = 0  # Handle invalid input

        # Ensure jarak is within the valid range
        if jarak < 0:
            jarak = 0
        elif jarak > 60:
            jarak = 60
        
        try:
            waktu = float(request.form['waktu'])  # Convert to float (if it's a decimal)
        except ValueError:
            waktu = 0  # Handle invalid input

        # Ensure waktu is within the valid range
        if waktu < 0:
            waktu = 0
        elif waktu > 3:
            waktu = 3
            
        # Call the inferensi function
        result = inferensi(harga, jarak, waktu)
        return render_template('hasil.html', jawaban=result)
=======
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
>>>>>>> Stashed changes

    return render_template('input_data.html')