from .rules import rules1, rules2, rules3, rules4, rules5, rules6, rules7, rules8

def inferensi(harga, jarak, waktu):
    pilih = rules1(harga, jarak, waktu)  # Directly call the rule function
    pertimbangkan = max(rules2(harga, jarak, waktu), rules3(harga, jarak, waktu), rules5(harga, jarak, waktu))
    jangan = max(rules4(harga, jarak, waktu), rules6(harga, jarak, waktu), rules7(harga, jarak, waktu), rules8(harga, jarak, waktu))

    if max(pilih, pertimbangkan, jangan) == pilih:
        return "Pilih Vendor"
    elif max(pilih, pertimbangkan, jangan) == pertimbangkan:
        return "Pertimbangkan Vendor"
    else:
        return "Jangan pilih vendor tersebut"
