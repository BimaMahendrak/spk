# range keseluruhan 0 - 32
max_jarak = 60
min_jarak = 0
# range tengah 28 - 32 
max_tengah = 32
min_tengah = 28

def dekat(jarak):
    # 0 - 32
    if jarak <= min_tengah:
        return 1.0
    elif jarak >= max_tengah:
        return 0.0
    else:
        return (max_jarak-jarak)/(max_jarak-min_tengah)
    
def jauh(jarak):
    # 28 - 60
    if jarak <= max_tengah:
        return 0.0
    elif jarak >= max_jarak:
        return 1.0
    else:
        return (jarak-max_tengah)/(max_jarak-max_tengah)