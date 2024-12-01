max = 3.0
min = 0.0

def cepat(waktu):
    if waktu <= min:
        return 1.0
    elif waktu > min & waktu < max:
        return (max-waktu)/(max-min)
    else:
        return 0.0
    
def lambat(waktu):
    if waktu <= min:
        return 0.0
    elif waktu > min & waktu < max:
        return (waktu-max)/(max-min)
    else:
        return 1.0