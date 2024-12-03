def tidakRekomen(nilai):
    # 0 - 6
    min_nilai = 0
    max_nilai = 5
    return nilai*(max_nilai-min_nilai)+min_nilai
    
def rekomen(nilai):
    # 4 - 10
    min_nilai = 10
    max_nilai = 6
    return nilai*(max_nilai-min_nilai)+min_nilai