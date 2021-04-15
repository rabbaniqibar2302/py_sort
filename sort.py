def urutasc(mylist):
    for i in range(len(mylist)-1, 0, -1):
        for j in range(i):
            if mylist[j] > mylist[j+1]:
                simpan = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = simpan
    print(mylist)


def urutdsc(mylist):
    for i in range(len(mylist)-1, 0, -1):
        for j in range(i):
            if mylist[j] < mylist[j+1]:
                simpan = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = simpan
    print(mylist)


print("Program Mengurutkan Data Dengan Metode Bubble sort")

angka1 = int(input('Masukan bilangan ke 1  : '))
angka2 = int(input('Masukan bilangan ke 2  : '))
angka3 = int(input('Masukan bilangan ke 3  : '))
angka4 = int(input('Masukan bilangan ke 4  : '))
angka5 = int(input('Masukan bilangan ke 5  : '))
angka6 = int(input('Masukan bilangan ke 6  : '))
angka7 = int(input('Masukan bilangan ke 7  : '))
angka8 = int(input('Masukan bilangan ke 8  : '))
angka9 = int(input('Masukan bilangan ke 9  : '))
angka10 = int(input('Masukan bilangan ke 10 : '))

angka = [angka1, angka2, angka3, angka4, angka5,
         angka6, angka7, angka8, angka9, angka10]

print('=============================')
print('Pilih Metode Pengurutan : ')
print('1.Sorting ascending \n2.Sorting descending')
pilih = input('Metode yang dipilih : ')

print('=============================')
print('Data sebelum diurutkan :')
print(angka)
print('Data setelah diurutkan :')

if pilih == ('1'):
    urutasc(angka)
elif pilih == ('2'):
    urutdsc(angka)
else:
    print("Angka yang anda tulis salah")

home = input('Kembali Kemenu utama (Y/N)? ')
text = print('Program Mengurutkan Data Dengan Metode Bubble sort')
back = print('')
garis = ('============================')
if home == ('Y'):
    garis
    text
    angka1 = int(input('Masukan Bilangan Ke 1  : '))
    angka2 = int(input('Masukan Bilangan Ke 2  : '))
    angka3 = int(input('Masukan Bilangan Ke 3  : '))
    angka4 = int(input('Masukan Bilangan Ke 4  : '))
    angka5 = int(input('Masukan Bilangan Ke 5  : '))
    angka6 = int(input('Masukan Bilangan Ke 6  : '))
    angka7 = int(input('Masukan Bilangan Ke 7  : '))
    angka8 = int(input('Masukan Bilangan Ke 8  : '))
    angka9 = int(input('Masukan Bilangan Ke 9  : '))
    angka10 = int(input('Masukan Bilangan Ke 10 : '))
    garis
    print('Pilih Metode Pengurutan : ')
    print('1.Sorting ascending')
    print('2.Sorting descending')
    pilih = input('Metode yang dipilih : ')
    print('===========================')
    print('Data sebelum diurutkan :')
    str(angka)
    print('Data setelah diurutkan :')
    if pilih == ('1'):
        urutasc(angka)
    else:
        urutdsc(angka)
    home = input('Kembali Kemenu utama (Y/N)? ')
else:
    back
