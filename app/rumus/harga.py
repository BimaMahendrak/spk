max = 20000000.0
min = 0.0

def murah(harga):
    if harga <= min:
        return 1.0
    elif harga > min & harga < max:
        return (max-harga)/(max-min)
    else:
        return 0.0
    
def mahal(harga):
    if harga <= min:
        return 0.0
    elif harga > min & harga < max:
        return (harga-max)/(max-min)
    else:
        return 1.0