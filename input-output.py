print('=============================')
print('PROGRAM MENCARI LUAS SEGITIGA')
print('=============================')

nilaialas = input('Masukkan Nilai Alas : ')
nilaitinggi = input('Masukkan Nilai Tinggi : ')

def segitiga(a, t):
    luas = 0.5 * int(a) * int(t)
    # print(f'Luas Segitiga Dengan Alas {nilaialas} dan Tinggi {nilaitinggi} Adalah : ', float(luas))
    print('Luas Segitiga Adalah : ', float(luas))

segitiga(nilaialas, nilaitinggi)