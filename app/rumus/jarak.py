max = 60
min = 0

def dekat(jarak):
    if jarak <= min:
        return 1
    elif jarak > min and jarak < max:
        return (max-jarak)/(max-min)
    else:
        return 0
    
def jauh(jarak):
    if jarak <= min:
        return 0
    elif jarak > min and jarak < max:
        return (jarak-max)/(max-min)
    else:
        return 1