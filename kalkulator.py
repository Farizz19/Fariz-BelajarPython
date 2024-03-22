operator = '*','/','+','-'

nama = input('Masukkan Nama Anda : ')
password = input('Masukkan Password Anda : ')
print('\n')

if nama == 'fariz' and password == 123:
    print('Selamat Datang,', nama)

print('=========================')
print('PROGRAM KALKULATOR PYTHON')
print('=========================')
print('\n')

nilai1 = input('Masukkan Nilai 1 : ')
nilai2 = input('Masukkan Nilai 2 : ')
op = input('Masukkan Operator Aritmatika : ')

def kalkulator(n1, n2):
    if op == '+':
        hasil = int(n1) + int(n2)
        print('Hasil Penjumlahan : ',hasil)
    elif op == '-':
        hasil = int(n1) - int(n2)
        print('Hasil Pengurangan : ',hasil)
    elif op == '*':
        hasil = int(n1) * int(n2)
        print('Hasil Perkalian : ',hasil)
    elif op == '/':
        hasil = int(n1) / int(n2)
        print('Hasil Pembagian : ',hasil)
    else:
        print('Program Error')
        
kalkulator(nilai1, nilai2)
print('\n')