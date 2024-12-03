from .rules import rules1, rules2, rules3, rules4, rules5, rules6, rules7, rules8
from .rekomendasi import rekomen, tidakRekomen

zadeh=[]
predikat=[]

def inferensi(harga, jarak, waktu):
    if harga <= 12000000: #murah
        if jarak <= 32: #dekat
            if waktu <= 2: #cepat
                a = rules1(harga, jarak, waktu)
                b = rekomen(a)
                predikat.append(a)
                zadeh.append(a*b)
            if waktu >= 1: #lambat
                a = rules2(harga, jarak, waktu)
                b = rekomen(a)
                predikat.append(a)
                zadeh.append(a*b)
        if jarak >= 28: #jauh
            if waktu <= 2: #cepat
                a = rules3(harga, jarak, waktu)
                b = rekomen(a)
                predikat.append(a)
                zadeh.append(a*b)
            if waktu >= 1: #lambat
                a = rules4(harga, jarak, waktu)
                b = tidakRekomen(a)
                predikat.append(a)
                zadeh.append(a*b)
    if harga >= 8000000: #mahal
        if jarak <= 32: #dekat
            if waktu <= 2: #cepat
                a = rules5(harga, jarak, waktu)
                b = rekomen(a)
                predikat.append(a)
                zadeh.append(a*b)
            if waktu >= 1: #lambat
                a = rules6(harga, jarak, waktu)
                b = tidakRekomen(a)
                predikat.append(a)
                zadeh.append(a*b)
        if jarak >= 28: #jauh
            if waktu <= 2: #cepat
                a = rules7(harga, jarak, waktu)
                b = tidakRekomen(a)
                predikat.append(a)
                zadeh.append(a*b)
            if waktu >= 1: #lambat
                a = rules8(harga, jarak, waktu)
                b = tidakRekomen(a)
                predikat.append(a)
                zadeh.append(a*b)

    crips = sum(zadeh)/sum(predikat)

    if crips < 5:
        return "Direkomendasikan", crips
    else:
        return "Tidak Direkomendasikan", crips