# range keseluruhan 0 - 20 juta
max_harga = 20000000
min_harga = 0
# range tengah 8 juta - 12 juta 
max_tengah = 12000000
min_tengah = 8000000

def murah(harga):
    # 0 - 12 juta
    if harga <= min_tengah:
        return 1.0
    elif harga >= max_tengah:
        return 0.0
    else:
        return (max_harga-harga)/(max_harga-min_tengah)
    
def mahal(harga):
    # 8 juta - 20 juta
    if harga <= max_tengah:
        return 0.0
    elif harga >= max_harga:
        return 1.0
    else:
        return (harga-max_tengah)/(max_harga-max_tengah)