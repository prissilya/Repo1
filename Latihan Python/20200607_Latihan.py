# import math
# print('Mencari luas dan keliling setengah lingkaran')
# class setengahlingkaran :
#     def __init__ (self,r):
#         self.jarijari = r
#     def luassetlingk (self):
#         self.luaslingk = (math.pi*(self.jarijari**2))/2
#         return self.luaslingk
#     def kelsetlingk (self):
#         self.kelilinglingk = math.pi * self.jarijari
#         return self.kelilinglingk

# jarijarilingk = int(input('Masukkan jari-jari lingkaran (cm): '))
# setlingk = setengahlingkaran (jarijarilingk)

# luassetengahlingkaran = setlingk.luassetlingk()
# kelilingsetengahlingkaran = setlingk.kelsetlingk()

# print ('Luas setengah lingkaran dengan jari-jari '+str(jarijarilingk)+'cm adalah: '+str(luassetengahlingkaran)+'cm2')
# print ('Luas setengah lingkaran dengan jari-jari '+str(jarijarilingk)+'cm adalah: '+str(kelilingsetengahlingkaran)+'cm')

# print('Mencari luas dan keliling layang-layang')
# class layanglayang :
#     def __init__ (self,d1,d2,s1,s2):
#         self.rusuk1 = d1
#         self.rusuk2 = d2
#         self.sisi1 = s1
#         self.sisi2 = s2
#     def luaslayang (self):
#         self.luaslayang2 = 0.5 * self.rusuk1 * self.rusuk2
#         return self.luaslayang2
#     def kellayang (self):
#         self.kelilinglayang2 = 2 * (self.sisi1 + self.sisi2)
#         return self.kelilinglayang2

# rusuky = int(input('Masukkan rusuk vertikal layang-layang (cm): '))
# rusukx = int(input('Masukkan rusuk diagonal layang-layang (cm): '))
# sisiatas = int(input('Masukkan sisi atas layang-layang (cm): '))
# sisibawah = int(input('Masukkan sisi bawah layang-layang (cm): '))
# layangan = layanglayang(rusuky,rusukx,sisiatas,sisibawah)

# luaslay = layangan.luaslayang()
# kellay = layangan.kellayang()

# print('Luas layang-layang dari rusuk vertikal '+str(rusuky)+'cm, rusuk diagonal '+str(rusukx)+'cm, sisi atas '+str(sisiatas)+'cm dan sisi bawah '+str(sisibawah)+'cm adalah : '+str(luaslay)+'cm2')
# print('Keliling layang-layang dari rusuk vertikal '+str(rusuky)+'cm, rusuk diagonal '+str(rusukx)+'cm, sisi atas '+str(sisiatas)+'cm dan sisi bawah '+str(sisibawah)+'cm adalah : '+str(kellay)+'cm')

# print('Mencari luas dan keliling jajargenjang')
# class jajargenjang :
#     def __init__ (self,a,b,c):
#         self.alas = a
#         self.tinggi = b
#         self.miring = c
#     def luasjajargenjang (self):
#         self.luasjar = self.alas * self.tinggi
#         return self.luasjar
#     def kelilingjajargenjang (self):
#         self.kelilingjar = 2 * (self.alas + self.miring)
#         return self.kelilingjar

# alasjar = int(input('Masukkan alas jajar genjang (cm): '))
# tinggijar = int(input('Masukkan tinggi jajar genjang (cm): '))
# miringjar = int(input('Masukkan sisi miring jajar genjang (cm): '))
# jajar = jajargenjang(alasjar,tinggijar,miringjar)

# luasjargen = jajar.luasjajargenjang()
# kelilingjargen = jajar.kelilingjajargenjang()

# print('Luas jajar genjang dengan alas '+str(alasjar)+'cm, tinggi '+str(tinggijar)+'cm dan sisi miring '+str(miringjar)+'cm adalah: '+str(luasjargen)+'cm2')
# print('Luas jajar genjang dengan alas '+str(alasjar)+'cm, tinggi '+str(tinggijar)+'cm dan sisi miring '+str(miringjar)+'cm adalah: '+str(kelilingjargen)+'cm')

# print('Mencari luas dan keliling belah ketupat')
# class ketupat :
#     def __init__ (self,r1,r2,s):
#         self.diagonal1 = r1
#         self.diagonal2 = r2
#         self.sisi = s
#     def luasketupat (self):
#         self.luastupat = 0.5 * self.diagonal1 * self.diagonal2
#         return self.luastupat
#     def kelilingketupat (self):
#         self.kelilingtupat = 4 * self.sisi
#         return self.kelilingtupat

# ruas1ketupat = int(input('Masukkan diagonal 1 ketupat (cm): '))
# ruas2ketupat = int(input('Masukkan diagonal 2 ketupat (cm): '))
# sisiketupat = int(input('Masukkan sisi ketupat (cm): '))
# tupat = ketupat(ruas1ketupat,ruas2ketupat,sisiketupat)

# luasketupat1 = tupat.luasketupat()
# kelilingketupat1 = tupat.kelilingketupat()

# print('Luas ketupat dengan diagonal 1 '+str(ruas1ketupat)+'cm, diagonal 2 '+str(ruas2ketupat)+'cm dan sisi '+str(sisiketupat)+'cm adalah: '+str(luasketupat1)+'cm2')
# print('Keliling ketupat dengan diagonal 1 '+str(ruas1ketupat)+'cm, diagonal 2 '+str(ruas2ketupat)+'cm dan sisi '+str(sisiketupat)+'cm adalah: '+str(kelilingketupat1)+'cm')

# print('Mencari luas dan keliling trapesium')
# class trapesium:
#     def __init__ (self,a,b,ka,ki,ti):
#         self.atas = a
#         self.bawah = b
#         self.kanan = ka
#         self.kiri = ki
#         self.tinggi1 = ti
#     def luastrap (self):
#         self.luastrape = ((self.atas + self.bawah) * self.tinggi1)/2
#         return self.luastrape
#     def keltrap (self):
#         self.keltrape = self.atas + self.bawah + self.kanan + self.kiri
#         return self.keltrape

# sisiatas = int(input('Masukkan sisi atas trapesium (cm): '))
# sisibawah = int(input('Masukkan sisi bawah trapesium (cm): '))
# sisikanan = int(input('Masukkan sisi kanan trapesium (cm): '))
# sisikiri = int(input('Masukkan sisi kiri trapesium (cm): '))
# tinggitrap = int(input('Masukkan tinggi trapesium (cm): '))
# trape = trapesium(sisiatas,sisibawah,sisikanan,sisikiri,tinggitrap)

# luastrapesium = trape.luastrap()
# kelilingtrapesium = trape.keltrap()

# print('Luas trapesium dengan sisi atas '+str(sisiatas)+'cm, sisi bawah '+str(sisibawah)+'cm, sisi kanan '+str(sisikanan)+'cm, sisi kiri '+str(sisikiri)+'cm dan tinggi '+str(tinggitrap)+'cm adalah: '+str(luastrapesium)+'cm2')
# print('Keliling trapesium dengan sisi atas '+str(sisiatas)+'cm, sisi bawah '+str(sisibawah)+'cm, sisi kanan '+str(sisikanan)+'cm, sisi kiri '+str(sisikiri)+'cm dan tinggi '+str(tinggitrap)+'cm adalah: '+str(kelilingtrapesium)+'cm')

# class student:
#     def __init__ (self,name,nim,age):
#         self.nama = name
#         self.nomor = nim
#         self.umur = age
#     def getnomor (self):
#         return self.nomor
#     def getnama (self):
#         return self.nama
#     def getage (self):
#         return self.umur

# student1 = student('Prissil',1,30)
# student2 = student('Rina',2,23)
# student3 = student('Aris',3,25)

# name1 = student1.getnama()
# name2 = student2.getnama()
# name3 = student3.getnama()

# no1 = student1.getnomor()
# no2 = student2.getnomor()
# no3 = student3.getnomor()

# age1 = student1.getage()
# age2 = student2.getage()
# age3 = student3.getage()

# ratarata = (age1+age2+age3)/3

# print('Nama: '+name1+', nomor urut: '+str(no1)+', usia: '+str(age1))
# print('Nama: '+name2+', nomor urut: '+str(no2)+', usia: '+str(age2))
# print('Nama: '+name3+', nomor urut: '+str(no3)+', usia: '+str(age3))
# print('Rata-rata umur ketiga murid tersebut adalah : '+str(ratarata))


# def waktu (detik):
#     jam = detik // 3600
#     sisadetik = detik - (jam * 3600)
#     menit = sisadetik // 60
#     sisamenit = sisadetik - (menit * 60)
#     if jam > 9 or menit > 9 or sisamenit > 9:
#         print(str(jam)+':'+str(menit)+':'+str(sisamenit))
#     else:
#         print('0'+str(jam)+':0'+str(menit)+':0'+str(sisamenit))

# s = int(input('Masukkan detik yang ingin dikonversi: '))
# waktu(s)


# def rowSumOddNumbers(n) :
#     numbers  = []
#     nilai = 1

#     for i in range(1, n+1) :
#         temp = []
#         for j in range(i) :
#             temp.append(nilai)
#             nilai += 2
#         numbers.append(temp)
    
#     z = ''
#     for num, i in zip(numbers, range(len(numbers))) :
#         for j in range(n-i) :
#             z += '  '
#         for k in num :
#             z += str(k).ljust(4, ' ')
#         z += '\n' 
#     print(z)

#     sum_row = ''
    
#     for num in numbers[-1]:
#         if num == numbers[-1][-1]:
#             sum_row += str(num)
#         else:    
#             sum_row += str(num)
#             sum_row += ' + '
#     sum_row += ' = {}'.format(sum(numbers[-1]))       
    
#     if sum(numbers[-1]) == 1:
#         print(1)
#     else:
#         print(sum_row)   

# rowSumOddNumbers(15)

# x = input('Masukkan kalimat yang ingin dispin: ')
# pisah = x.split()
# kalimatbaru = []
# katabaru = []

# for i in range(len(pisah)):
#     if len(pisah[i])>4:
#         kata = list(pisah[i])
#         xx = len(kata)
#         for j in range(xx):
#             katabaru.append(kata[xx-1])
#             xx-=1
#         kalimatbaru.append(''.join(map(str,katabaru)))
#         katabaru.clear()
#     else:
#         kalimatbaru.append(pisah[i])
# print(kalimatbaru)

# def movezero(x):
#     for i in range(len(x)):
#         for j in range(i+1):
#             if type(x[j])==type(False):
#                 x[i],x[j]=x[i],x[j]
#             elif x[j]==0:
#                 x[i],x[j]=x[j],x[i]
#     return x

# lis = [1,0,4,0,True,'Test',False,0,9,'a']
# print(movezero(lis))


# p0 = int(input('Masukkan jumlah populasi saat ini : '))
# gr = int(input('Masukkan prosentase growth : '))
# adding = int(input('Masukkan asumsi pertambahan pendatang : '))
# maksimum = int(input('Masukkan populasi yang ingin dicapai : '))

# def annual (pop,growth,add,maks):
#     tahun = 0
#     while pop < maks:
#         pop = pop + (pop*(growth/100))+add
#         tahun = tahun + 1
#     print('Membutuhkan '+str(tahun)+' tahun untuk mencapai populasi '+str(maks)+' orang')

# annual(p0,gr,adding,maksimum)




            
