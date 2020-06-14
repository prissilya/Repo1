# x = (['Saya','Kamu','Dia','Mereka'],{'Nama':'Prissil','Usia':'30 tahun'},1,5,6,[[1,2,3],[4,5,6]],True)
# y = 'Aku seorang kapiten',
# print(x)
# print('Tipe data x adalah : '+str(type(x)))
# print('Tipe data x[0] adalah : '+str(type(x[0])))
# print('Isi data x[0][1] adlah : '+str(x[0][1]))
# print('Tipe data x[1] adalah : '+str(type(x[1])))
# print('Isi data x[1],["Nama"] adalah : '+str(x[1]['Nama']))
# print('Tipe data x[2] adalah : '+str(type(x[2])))
# print('Isi data x[2] adalah : '+str(x[2]))
# print('Tipe data x[5] adalah : '+str(type(x[5])))
# print('Isi data x[5][0][1] adalah : '+str(x[5][0][1]))
# print('Tipe data x[6] adalah : '+str(type(x[6])))
# print('Isi data dari x[6] adalah : '+str(x[6]))
# print(y)
# print('Tipe data y adalah : '+str(type(y)))


# x = int(input('Masukkan jumlah : '))
# angka = []
# for i in range (1,x+1):
#     import random
#     random1 = random.randint(1,50)
#     angka.append(random1)
# b = angka

# y = set(b)
# print(b)
# print(y)

# genap = []
# ganjil = []
# for i in range (len(b)):
#     if b[i] %2 == 0:
#         genap.append(b[i])
#     else:
#         ganjil.append(b[i])
# print('List angka adalah : '+str(angka))
# print('List value genap dari angka adalah : '+str(genap))
# print('List value ganjil dari angka adalah : '+str(ganjil))

# listangkax2 = [w*2 for w in angka]
# listganjilx2 = [x*2 for x in ganjil]
# listgenapx2 = [y*2 for y in genap]

# print('Angka dikali 2 adalah : '+str(listangkax2))
# print('Ganjil dikali 2 adalah : '+str(listganjilx2))
# print('Genap dikali 2 adalah : '+str(listgenapx2))

# import math
# x = int(input('Masukkan nilai X : '))
# y = int(input('Masukkan nilai Y : '))
# z = int(input('Masukkan nilai Z : '))
# w = int(input('Masukkan nilai W : '))
# m = int(input('Masukkan nilai M : '))

# print(lambda x,y,z,w,m : (((x**y)//z)**w)/m))

# x = ['Merdeka','Hello','Hellos','Sohib','Kari ayam']
# low = [y.lower() for y in x]
# check = []
# search = 'ka'
# for i in range (len(x)):
#     if search in low[i]:
#         check.append(x[i])
# print(check)


# x = int(input('Masukkan jumlah kata dalam list : '))
# list = []
# for i in range (1,x+1):
#     kata = input('Masukkan kata ke-'+str(i)+' : ')
#     list.append(kata)
# print(list)
# low = [j.lower() for j in list]
# check = []
# search = input('Ingin mencari apa : ')
# search = search.lower()
# for k in range (len(list)):
#     if search in low[k]:
#         check.append(list[k])
# print(check)

# x = int(input('Masukkan jumlah deretan angka : '))
# def prima (angka):
#     bilangan = []
#     for j in range (2,angka+1):
#         if angka%j == 0:
#             bilangan.append(True)
#     if sum(bilangan) == 1:
#         return True
#     else:
#         return False

# def fizzbuzz (angka):
#     for i in range (1,angka+1):
#         if prima(i):
#             print('Prime')
#         elif i%7 == 0:
#             print('Fizz')
#         elif i%9 == 0:
#             print('Buzz')
#         elif i%63 == 0:
#             print('FizzBuzz')
#         else:
#             print(i)
#     return()
# fizzbuzz(x)

# index = int(input('Masukkan fibo : '))
# def fibo (index):
#     inisiasi = [1,1,2]
#     for i in range (3,index):
#         inisiasi.append(inisiasi[i-3]+inisiasi[i-1])
#     return inisiasi[index-1]
# print(fibo(index))

# index = int(input('Masukkan fibo : '))
# def fibo (index):
#     inisiasi = [1,15]
#     for j in range (2,index-1):
#         inisiasi.append(inisiasi[j-2]+inisiasi[j-1])
#     return inisiasi

# def reverselist (list):
#     list = (fibo(index))
#     for k in range (0,(len(list)//2)):
#         tempList = list [k]
#         list [k] = list[len(list)-1-k]
#         list[len(list)-1-k] = tempList
#     return list

# print (fibo(index))
# print (reverselist(fibo(index)))


# index = int(input('Masukkan fibo : '))
# def fibo (index):
#     inisiasi = [10,7,1,8]
#     for j in range (4,index-1):
#         inisiasi.append(inisiasi[j-4]+inisiasi[j-1])
#     return inisiasi

# def reverselist ():
#     list = (fibo(index))
#     for k in range (0,(len(list)//2)):
#         tempList = list [k]
#         list [k] = list[len(list)-1-k]
#         list[len(list)-1-k] = tempList
#     return list

# def bubblesort():
#     list1 = (reverselist())
#     for l in range (len(list1),0,-1):
#         for m in range (0,l-1):
#             if list1[m]<list1[m+1]:
#                 temp = list1[m]
#                 list1[m] = list1[m+1]
#                 list1[m+1] = temp
#     return list1

# print (fibo(index))
# print (reverselist())
# print (bubblesort())

# class Prissil:
#     def __init__ (self,name,age,job,bornplace):
#         self.nama = name
#         self.umur = age
#         self.pekerjaan = job
#         self.tempatlahir = bornplace

# prissil1 = Prissil('Prissil',30,'IRT','Jakarta')
# print(prissil1.nama)
# print(prissil1.umur)
# print(prissil1.pekerjaan)
# print(prissil1.tempatlahir)
# print(prissil1.__dict__)

# class prissil:
#     def __init__ (self,name,gender,age):
#         self.nama = name
#         self.jk = gender
#         self.usia = age
#     def kalimat (self):
#         print('Nama saya adalah '+self.nama+' yang berjenis kelamin '+self.jk+' dan berusia '+self.usia+'.')

# contoh = prissil('Prissil','Perempuan','30')
# contoh.kalimat()

# contoh.nama = 'Arief'
# contoh.kalimat()


# class prissil:
#     def __init__ (self,name,gender,birthplace):
#         self.nama = name
#         self.jk = gender
#         self.tempatlahir = birthplace
#     def kalimat (self):
#         print('Nama saya adalah '+self.nama+' yang berjenis kelamin '+self.jk+' dan lahir di '+self.tempatlahir+'.')

# class prissilya(prissil):
#     def __init__ (self,name,gender,birthplace,age,job):
#         super().__init__(name,gender,birthplace)
#         self.usia = age
#         self.pekerjaan = job
#     def kalimat1 (self):
#         print('Nama saya adalah '+self.nama+', yang berjenis kelamin '+self.jk+', lahir di '+self.tempatlahir+', berusia '+str(self.usia)+' dan bekerja sebagai '+self.pekerjaan+'.')
#     def kalimat2 (self):
#         print('Nama saya adalah '+self.nama+', yang berjenis kelamin '+self.jk+', lahir di '+self.tempatlahir+', 2 tahun lagi berusia '+str(self.usia+2)+' dan bekerja sebagai '+self.pekerjaan+'.')


# contoh = prissil('Prissil','Perempuan','Jakarta')
# contoh.kalimat()
# print(contoh.__dict__)

# contoh1 = prissilya('Prissil','Perempuan','Jakarta',30,'IRT')
# contoh1.kalimat1()
# contoh1.kalimat2()
# print(contoh1.__dict__)

class vokal:
    def __init__ (self,teks):
        self.kata = teks
        self.a = 0
        self.i = 0
        self.u = 0
        self.e = 0
        self.o = 0
    def A (self):
        for x in range (len(self.kata)):
            if self.kata[x] == 'a' or self.kata[x] == 'A':
                self.a = self.a + 1
        return self.a
    def I (self):
        for x in range (len(self.kata)):
            if self.kata[x] == 'i' or self.kata[x] == 'I':
                self.i = self.i + 1
        return self.i
    def U (self):
        for x in range (len(self.kata)):
            if self.kata[x] == 'u' or self.kata[x] == 'U':
                self.u = self.u + 1
        return self.u
    def E (self):
        for x in range (len(self.kata)):
            if self.kata[x] == 'e' or self.kata[x] == 'E':
                self.e = self.e + 1
        return self.e
    def O (self):
        for x in range (len(self.kata)):
            if self.kata[x] == 'o' or self.kata[x] == 'O':
                self.o = self.o + 1
        return self.o

teks = input('Masukkan kalimat yang diinginkan : ')
contoh = vokal(teks)

jumlahA = contoh.A()
jumlahI = contoh.I()
jumlahU = contoh.U()
jumlahE = contoh.E()
jumlahO = contoh.O()

print ('Jumlah huruf A pada kalimat : "',teks,'" adalah: ',jumlahA)
print ('Jumlah huruf I pada kalimat : "',teks,'" adalah: ',jumlahI)
print ('Jumlah huruf U pada kalimat : "',teks,'" adalah: ',jumlahU)
print ('Jumlah huruf E pada kalimat : "',teks,'" adalah: ',jumlahE)
print ('Jumlah huruf O pada kalimat : "',teks,'" adalah: ',jumlahO)