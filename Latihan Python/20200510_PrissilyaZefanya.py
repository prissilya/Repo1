# soal1
# jumlahhari = int(input('Masukkan Jumlah Hari : '))
# tahun = 360
# bulan = 30
# minggu = 7
# tahun1 = jumlahhari//tahun
# bulan1 = (jumlahhari -(tahun1*tahun))//bulan
# minggu1 = (jumlahhari - ((tahun1*tahun)+(bulan1*bulan)))//minggu
# hari = (jumlahhari - ((tahun1*tahun)+(bulan1*bulan)+(minggu1*minggu)))
# if (jumlahhari>=1):
#     print(str(tahun1)+' tahun '+str(bulan1)+' bulan '+str(minggu1)+' minggu '+str(hari)+' hari.')
# else:
#     print('Masukkan Jumlah Hari yang Benar')

#soal2
# listitem = list (range(1,11,2))
# print(listitem)
# print(sum(listitem)/len(listitem))

#soal3
# input1 = input('Masukkan kata : ')
# input1 = input1.lower()
# input2 = input('Masukkan huruf yang ingin dihitung : ')
# input2 = input2.lower()
# print(input1.count(input2))

#soal4
# jarak = int(input('Masukkan Jarak antara Mobil 1 dengan Mobil 2 (KM) : '))
# pkl = int(input('Masukkan Waktu Berangkat (Asumsi Bersamaan) : Pkl. '))
# kecepatan1 = int(input('Masukkan Kecepatan Mobil 1 (KM / Jam) : '))
# kecepatan2 = int(input('Masukkan Kecepatan Mobil 2 (KM / Jam) : '))
# w = jarak / (kecepatan1+kecepatan2)
# w = w*60
# wjam = int(w//60)
# wmenit = int(w%60)
# jamtabrakan = pkl+wjam
# print (str(jamtabrakan)+':'+str(wmenit))

#soal5
# x = int(input('Masukkan Jumlah Baris : '))
# z = ''
# for item in range (0,x):
#     for item in range (0,item+1):
#         z+=' * '
#     z+='\n\n'
# print(z)

#soal6
# x = int(input('Masukkan banyak data : '))
# jumlah = x+1
# total = 0
# for item in range (1,jumlah):
#     data = input('Masukkan Data ke-'+str(item)+' :')
#     total = total+int(data)
# ratarata = total / jumlah
# print('Rata-rata '+str(jumlah)+' data tersebut adalah '+str(ratarata))

#soal7
import math
y = input('Pilihan 1 : Menghitung Luas Segitiga Siku-Siku\nPilihan 2 : Menghitung Luas Jajaran Genjang\nPilihan 3 : Menghitung Rata-Rata Nilai\nPilihan 4 : Menghitung Variansi dan Std Dev\nPerhatikan Pilihan Di Atas, Silahkan Masukkan Pilihan Anda : ')
if (y=='1'):
    alas = int(input('Masukkan alas segitiga : '))
    tinggi = int(input('Masukkan tinggi segitiga : '))
    LSegitiga = 1/2*alas*tinggi
    print('Dengan alas = '+str(alas)+' cm dan tinggi = '+str(tinggi)+' cm, maka luas segitiga siku-siku adalah : '+str(LSegitiga)+' cm kuadrat.')
elif (y=='2'):
    alas1 = int(input('Masukkan alas jajaran genjang : '))
    tinggi1 = int(input('Masukkan tinggi jajaran genjang : '))
    LJarGen = alas1*tinggi1
    print('Dengan alas = '+str(alas1)+' cm dan tinggi = '+str(tinggi1)+' cm, maka luas jajaran genjang adalah : '+str(LJarGen)+' cm kuadrat.')
elif (y=='3'):
    x = int(input('Masukkan banyak data : '))
    jumlah = x+1
    total = 0
    for item in range (1,jumlah):
        data = input('Masukkan Data ke-'+str(item)+' : ')
        total = total+int(data)
    ratarata = total / x
    print('Rata-rata '+str(x)+' data tersebut adalah '+str(ratarata))
elif (y=='4'):
    x = int(input('Masukkan banyak data : '))
    total = 0
    a = 0
    for item in range (1,x+1):
        data = input('Masukkan Data ke-'+str(item)+' : ')
        total = total+int(data)
        ratarata = total / x
        xi = int(data)**2
        a = a+xi
        b = x-1
    varian = (a-(x*(ratarata**2)))/b
    stddev = math.sqrt(varian)
    print('Nilai variansi dari '+str(x)+' data tersebut adalah : '+str(varian)+' dan nilai standar deviasinya adalah : '+str(stddev)+'.')
else:
    print('Masukkan pilihan yang benar')



    