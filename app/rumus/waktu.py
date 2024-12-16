# range keseluruhan 0 - 3
max_waktu = 3
min_waktu = 0
# range tengah 1 - 2 
max_tengah = 2
min_tengah = 1

def cepat(waktu):
    # 0 - 2
    if waktu < min_waktu:
        return 1.0
    elif waktu > max_tengah:
        return 0.0
    else:
        return (max_tengah-waktu)/(max_tengah-min_waktu)
    
def lambat(waktu):
    # 1 - 3
    if waktu < min_tengah:
        return 0.0
    elif waktu > max_waktu:
        return 1.0
    else:
        return (waktu-min_tengah)/(max_waktu-min_tengah)