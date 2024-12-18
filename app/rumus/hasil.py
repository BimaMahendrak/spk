from .rules import rules1, rules2, rules3, rules4, rules5, rules6, rules7, rules8
from .rekomendasi import rekomen, tidakRekomen

def inferensi(harga, jarak, waktu):
    alpha = [] # alpha predikat
    zPredikat = [] #hasil zedah * alpha predikat
    
    rule = rules1(harga, jarak, waktu)
    hasil = rekomen(rule)
    alpha.append(rule)
    zPredikat.append(rule*hasil)

    rule = rules2(harga, jarak, waktu)
    hasil = rekomen(rule)
    alpha.append(rule)
    zPredikat.append(rule*hasil)

    rule = rules3(harga, jarak, waktu)
    hasil = rekomen(rule)
    alpha.append(rule)
    zPredikat.append(rule*hasil)

    rule = rules4(harga, jarak, waktu)
    hasil = tidakRekomen(rule)
    alpha.append(rule)
    zPredikat.append(rule*hasil)

    rule = rules5(harga, jarak, waktu)
    hasil = rekomen(rule)
    alpha.append(rule)
    zPredikat.append(rule*hasil)

    rule = rules6(harga, jarak, waktu)
    hasil = tidakRekomen(rule)
    alpha.append(rule)
    zPredikat.append(rule*hasil)

    rule = rules7(harga, jarak, waktu)
    hasil = tidakRekomen(rule)
    alpha.append(rule)
    zPredikat.append(rule*hasil)

    rule = rules8(harga, jarak, waktu)
    hasil = tidakRekomen(rule)
    alpha.append(rule)
    zPredikat.append(rule*hasil)

    tA = sum(alpha)
    tZ = sum (zPredikat)

    if tA != 0:
        crips = tZ/tA
    else:
        crips = 1

    if crips < 5:
        return "Tidak Direkomendasikan", crips
    else:
        return "Direkomendasikan", crips