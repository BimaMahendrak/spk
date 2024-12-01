max = 20000000
min = 0

def murah(harga):
    if harga <= min:
        return 1
    elif harga > min and harga < max:
        return (max-harga)/(max-min)
    else:
        return 0
    
def mahal(harga):
    if harga <= min:
        return 0
    elif harga > min and harga < max:
        return (harga-max)/(max-min)
    else:
        return 1