max = 60.0
min = 0.0

def dekat(jarak):
    if jarak <= min:
        return 1.0
    elif jarak > min & jarak < max:
        return (max-jarak)/(max-min)
    else:
        return 0.0
    
def jauh(jarak):
    if jarak <= min:
        return 0.0
    elif jarak > min & jarak < max:
        return (jarak-max)/(max-min)
    else:
        return 1.0