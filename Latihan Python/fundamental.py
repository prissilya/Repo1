# nama = 'Prissil'
# usia = 30
# jenis_kelamin = 'Perempuan'
# pendidikan_terakhir = 'S1'

# print (nama)
# print (usia)
# print (jenis_kelamin)
# print (pendidikan_terakhir)
# print (type(nama))
# print (type(usia))
# print (type(jenis_kelamin))
# print (type(pendidikan_terakhir))

# nama = input ('Masukkan nama Anda = ')
# umur = input ('Masukkan umur Anda = ')
# status_perkawinan = input ('Masukkan status perkawinan Anda = ')

# print ('Nama Saya adalah '+nama+' yang berumur '+umur+' dengan status perkawinan '+status_perkawinan)

# nama = input('Nama kamu? : ')
# umur = input('Umur kamu? : ')
# jenis_kelamin = input('Jenis kelamin kamu? : ')
# pekerjaan = input('Pekerjaan kamu? : ')

# print('Nama : '+nama)
# print('Umur : '+umur)
# print('Jenis Kelamin: '+jenis_kelamin)
# print('Pekerjaan : '+pekerjaan)
# print('Nama saya '+nama+', umur saya '+umur+', jenis kelamin saya '+jenis_kelamin+', pekerjaan saya adalah '+pekerjaan+'.')

# import math

# print(8**5)
# print(round(9.9))
# print(-9.5*7)
# print(100%70)

# x = 'Halo Dunia'

# print(len(x))
# print(x.index('Dunia'))
# print(x.split(' '))
# print(x.lower())
# print(x.upper())
# print(x.capitalize())

# Nama = input ('Nama : ')
# Jenis_Kelamin = input ('Jenis Kelamin : ')
# Umur = int (input ('Umur : '))
# Umur = Umur + 3

# print(Nama)
# print(Jenis_Kelamin)
# print(Umur)

# print('Nama saya adalah '+Nama+' berjenis kelamin '+Jenis_Kelamin+' berusia '+str(Umur)+' di 3 tahun yang akan datang.')

# import math
# x = input ('Masukkan angka X : ')
# x = int(x)
# y = input ('Masukkan angka Y : ')
# y = int(y)
# z = input ('Masukkan angka Z : ')
# z = int(z)
# w = math.pow(((x+y*z)/(x*y)),z)

# print(w)

# import math
# angka = int(input ('Silahkan masukkan angka berapapun : '))
# angka1 = math.pow(angka,2)

# print('Kuadrat dari '+str(angka)+' = '+str(angka1))

# import math
# jumlahhari = input('Masukkan Jumlah Hari : ')
# jumlahhari = int(jumlahhari)
# tahun = math.floor (jumlahhari/360)
# sisahari1 = (jumlahhari-360)
# bulan = math.floor (sisahari1/30)
# sisahari2 = (sisahari1 - (bulan*30))
# minggu = math.floor(sisahari2/7)
# sisahari3 = (sisahari2 - (minggu*7))

# print (str(jumlahhari)+' hari = '+str(tahun)+' tahun '+str(bulan)+' bulan '+str(minggu)+' minggu '+str(sisahari3)+' hari')

# x = 'Halo Dunia'
# print(len(x))
# print(x.index('Dunia'))
# print(x.split(' '))
# print(x.lower())
# print(x.upper())
# print(x.capitalize())

# nilai = int(input('Masukkan Nilai : '));
# if (nilai>80):
#     print("Excellent!");
# elif (nilai>=60 and nilai<=80):
#     print("Good Job!");
# else:
#     print("Don't Give Up!");

# angka = input('Masukkan angka : ')
# angka = int(angka)
# if((angka%2)==0):
#     print('Angka '+str(angka)+' tergolong bilangan GENAP!');
# else:
#     print('Angka '+str(angka)+' tergolong bilangan GANJIL!');

# massa = float(input('Masukkan berat badan anda dalam kg : '))
# tinggi = float(input('Masukkan tinggi badan anda dalam cm : '))
# print('Berat badan anda adalah '+str(massa)+' kg dan tinggi badan anda adalah '+str(tinggi)+' cm.')
# IMT = massa/((tinggi/100)**2)
# if(IMT<18.5):
#     print('IMT = '+str(IMT)+', berat badan kurang!')
# elif(IMT>=18.5 and IMT<=24.9):
#     print('IMT = '+str(IMT)+', berat badan ideal!')
# elif(IMT>=25 and IMT<=29.9):
#     print('IMT = '+str(IMT)+', berat badan berlebih!')
# elif(IMT>=30 and IMT<=39.9):
#     print('IMT = '+str(IMT)+', berat badan sangat berlebih!')
# else:
#     print('IMT = '+str(IMT)+', obesitas!')

# listitem = list(range(1,11,2))
# print(listitem)
# for item in range(1,11,2):
#     print(item)


# for item in range(1,11):
#     print('Nomor urut '+str(item))

# for item in range(0,51,5):
#     print('Nomor urut '+str(item))

# z = ''
# for item in range(0,5):
#     for item1 in range(0,5):
#         z+=' * '
#     z+='\n'
# print(z)

# z=''
# for item in range (5,0,-1):
#     for item1 in range (0,item):
#         z+=' * '
#     z+='\n'
# print(z)

# def prissil():
#     print('Hai, apa kabar?')
# prissil()
# for item in range (1,6):
#     print('Saya anak rajin '+str(item))
# prissil()

# y = int(input('Masukkan nilai pangkat (yang diinginkan) atas value 5 : '))
# def prissil(x):
#     print(5**x)
# prissil(y)

# panjang = int(input('Masukkan panjang balok (CM) : '))
# lebar = int(input('Masukkan lebar balok (CM) : '))
# tinggi = int(input('Masukkan tinggi balok (CM) : '))
# def prissil (p,l,t):
#     print ('Volume balok adalah = '+str(p*l*t)+' cm kubik')
# prissil(panjang,lebar,tinggi)

# def total (x,y):
#     z=x+y
#     return z
# print (total(4,5))
# print (total(5,6))


# def total (x,y):
#     z=x+y
#     print(z)
# total(4,5)
# total(5,6)

# import math
# panjang = int(input('Masukkan panjang persegi (cm) : '))
# lebar = int(input('Masukkan lebar persegi (cm) : '))
# def persegipanjang (p,l):
#     luas = p*l
#     return luas
# print ('Luas Persegi Panjang adalah :'+str(persegipanjang (panjang,lebar)))

# jarijari = int(input('Masukkan jari-jari tabung (cm) : '))
# tinggi = int(input('Masukkan tinggi tabung (cm) : '))
# def tabung (r,t):
#     volume = math.pi*(r**2)*t
#     return volume
# print('Volume Tabung adalah : '+str(tabung(jarijari,tinggi)))

# totalin = persegipanjang(panjang,lebar) * tabung(jarijari,tinggi)
# print('Nilai perkalian Luas Persegi dan Volume Tabung adalah : '+str(totalin))

# x = int(input('Masukkan nilai X : '))
# y = int(input('Masukkan nilai Y : '))
# a = int(input('Masukkan nilai A : '))
# b = int(input('Masukkan nilai B : '))
# def luaspersegi (x):
#     if (x<2):
#         luas = x*y
#         return luas
#     else:
#         lain = (x*y)*sisi(a,b)
#         return lain
# def sisi (a,b):
#     c = a%b
#     return c
# print(luaspersegi(x))

# teman = ['Shinta','Sidha','Neshya','Kristina','Hilma']
# print('Berikut adalah nama teman-teman saya :')
# for item in teman:
#     print(item)
# print('Nama teman saya yang ke-3 adalah : '+str(teman[2]))
# print('Nama teman saya yang ke-5 adalah : '+str(teman[4]))
# print('Dua orang diantara teman saya bernama : '+str(teman[0]+' dan '+str(teman[3])))
# print('Total teman saya adalah sebanyak : '+str(len(teman))+' orang.')

# list = []
# stop = False
# item = 1
# while (not stop):
#     data = input('Inputkan hobi ke-'+str(item)+' : ')
#     list.append(data)
#     data2 = input('Mau isi lagi? (y/t) : ')
#     if (data2 == 'y'):
#         stop = False
#         item += 1
#     elif (data2 == 't'):
#         stop = True
#         print('======================\nKamu memiliki '+str(len(list))+' hobi :')
#         for j in list:
#             print(j)
#     else :
#         stop = True
#         print('Masukkan Keyword yang benar\n======================\n'+'Kamu memiliki '+str(len(list))+' hobi :\n'+data)

# def fungsi_Sort_ascending(arr):
#     for i in range (len(arr)):
#         for j in range (i+1,len(arr)):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j] = arr[j],arr[i]
#     return arr
# def fungsi_Sort_descending(arr2):
#     for i in range (len(arr2)):
#         for j in range (i+1,len(arr2)):
#             if arr2[i]<arr2[j]:
#                 arr2[i],arr2[j] = arr2[j],arr2[i]
#     return arr2
# x=[40,100,1,5,25,10]
# fungsi_Sort_ascending(x)
# print('Nilai paling kecil dari X adalah : '+str(x[0]))
# fungsi_Sort_descending(x)
# print('Nilai paling besar dari X adalah : '+str(x[0]))


# def bilangan(arr):
#     ganjil=[]
#     genap=[]
#     for i in range(len(x)):
#         if (x[i]%2==0):
#             genap.append(x[i])
#         else:
#             ganjil.append(x[i])
#     print(ganjil)
#     print(genap)
# x=[40, 100, 1, 5, 25, 10]
# bilangan(x)

# array = int(input('Masukkan Jumlah Array yang diinginkan : '))
# list = []
# for i in range (1,array+1):
#     data = int(input('Masukkan data ke-'+str(i)+' : '))
#     list.append(data)
# def bilangan(x):
#     ganjil=[]
#     genap=[]
#     for i in range(len(x)):
#         if (x[i]%2==0):
#             genap.append(x[i])
#         else:
#             ganjil.append(x[i])
#     print('Berikut adalah value genap dari list kamu : '+str(genap))
#     print('Berikut adalah value ganjil dari list kamu : '+str(ganjil))
# bilangan(list)

# x = {'Nama':'Prissil','Tempat Lahir':'Jakarta','Tanggal Lahir':'1 Sep','Hobi':'Tidur','Alamat':'Bekasi'}
# print(x['Nama'])
# print(x['Tempat Lahir'])
# print(x['Tanggal Lahir'])
# print(x['Hobi'])
# print(x['Alamat'])

# x = {'Nama':'Prissil','Tempat Lahir':'Jakarta','Tanggal Lahir':'1 Sep','Hobi':'Tidur','Alamat':'Bekasi','Asal Sekolah':{'SD':'Harapan Baru Bekasi','SMP':'18 Bekasi','SMA':'Mutiara 17 Agustus','D3':'Tarakanita','S1':'UI'},'Medsos':{'FB':'Xxx','Twitter':'Yyy','IG':'Zzz','LinkedIn':'Prissilya Zefanya'}}
# x['Nama'] = 'Nunu'
# x['Tempat Lahir'] = 'Bekasi'
# for i in x:
#     print(x[i])


# isian = input('Menu utama : \n1. Identitas\n2. Pendidikan\n3. Portofolio\n\nPilih salah satu : ')
# if (isian=='1'):
#     nama = input('Masukkan nama : ')
#     lahir = input('Masukkan TTL : ')
#     alamat = input('Masukkan alamat : ')
#     pekerjaan = input('Masukkan pekerjaan : ')
#     def identitas (x):
#         identitas = {'nama':nama,'lahir':lahir,'alamat':alamat,'pekerjaan':pekerjaan}
#         return identitas
#     identitas(identitas)
#     # print('Nama saya adalah %s'%identitas['nama'])
#     # print('Tempat tanggal lahir saya adalah %s'%identitas['lahir'])
#     # print('Saya tinggal di %s'%identitas['alamat'])
#     # print('Saya bekerja sebagai %s'%identitas['pekerjaan'])
# elif (isian=='2'):
#     sd = input('Masukkan nama SD : ')
#     smp = input('Masukkan nama SMP : ')
#     sma = input('Masukkan nama SMA : ')
#     ptinggi = input('Masukkan nama perguruan tinggi : ')
#     def pendidikan(x):
#         pendidikan = {'sd':sd,'smp':smp,'sma':sma,'ptinggi':ptinggi}
#         return pendidikan
#     pendidikan(pendidikan)
#     # print('Saya SD di '+pendidikan.get('sd'))
#     # print('Saya SMP di '+pendidikan.get('smp'))
#     # print('Saya SMA di '+pendidikan.get('sma'))
#     # print('Saya kuliah di '+pendidikan.get('ptinggi'))
# elif (isian=='3'):
#     porto = int(input('Masukkan portofolio yang kamu punya : '))
#     # for i in range (1,porto+1):
#     #     data = input('Masukkan porto '+i+' : ')
#     project = int(input('Masukkan project yang kamu ikuti : '))
#     # for j in range (1,project+1):
#     #     data1 = input('Masukkan project '+j+' : ')
#     def riwayat (x):
#         riwayat = {'porto':porto,'project':project}
#         return riwayat
#     print(riwayat(riwayat))
#     # print('Porto yang saya punya adalah '+riwayat[porto])
#     # print('Project yang saya punya adalah '+riwayat[project])
# else:
#     print('Masukkan kode yang benar')