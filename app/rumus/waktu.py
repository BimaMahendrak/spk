max = 3
min = 0

def cepat(waktu):
    if waktu <= min:
        return 1
    elif waktu > min and waktu < max:
        return (max-waktu)/(max-min)
    else:
        return 0
    
def lambat(waktu):
    if waktu <= min:
        return 0
    elif waktu > min and waktu < max:
        return (waktu-max)/(max-min)
    else:
        return 1