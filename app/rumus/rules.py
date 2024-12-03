from .harga import mahal, murah
from .jarak import jauh, dekat
from .waktu import lambat, cepat

#outuputnya berupa alpha predikat (dia nilai minum)

def rules1(harga, jarak, waktu):
    # murah + dekat + cepat = pilih
    return min(murah(harga), dekat(jarak), cepat(waktu))

def rules2(harga, jarak, waktu):
    # murah + dekat + lambat = pilih
    return min(murah(harga), dekat(jarak), lambat(waktu))

def rules3(harga, jarak, waktu):
    # murah + jauh + cepat = pilih
    return min(murah(harga), jauh(jarak), cepat(waktu))

def rules4(harga, jarak, waktu):
    # murah + jauh + lambat = jangan
    return min(murah(harga), jauh(jarak), lambat(waktu))

def rules5(harga, jarak, waktu):
    # mahal + dekat + cepat = pilih
    return min(mahal(harga), dekat(jarak), cepat(waktu))

def rules6(harga, jarak, waktu):
    # mahal + dekat + lambat = jangan
    return min(mahal(harga), dekat(jarak), lambat(waktu))

def rules7(harga, jarak, waktu):
    # mahal + jauh + cepat = jangan
    return min(mahal(harga), jauh(jarak), cepat(waktu))

def rules8(harga, jarak, waktu):
    # mahal + jauh + lambat = jangan
    return min(mahal(harga), jauh(jarak), lambat(waktu))