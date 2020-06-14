# def jumlah_kata(x):
#     kata = {}
#     for i in x.lower().split():
#         if i in kata.keys():
#             kata[i]+=1
#         else:
#             kata[i]=1
#     for keys, j in kata.items():
#         print("Jumlah kata '{}' ada sebanyak {}".format(keys.capitalize(),j))

# kata = input('Masukkan kalimat : ')
# jumlah_kata(kata)

# def gambar(list):
#     list_angka = []
#     for angka in list:
#         list_angka.append(int(angka))
#     z=''
#     for i in list_angka:
#         if (i == 1 or i == 4):
#             z+= '    '
#         else:
#             z+= '  __ '
#     z+='\n'
#     for i in list_angka:
#         if (i == 2 or i == 3):
#             z+= ' __| '
#         elif (i == 5 or i == 6):
#             z+= ' |__ '
#         elif (i == 1 or i == 7):
#             z+= '    | '
#         elif (i == 0):
#             z+= ' |  | '
#         else:
#             z+= ' |__| '
#     z+='\n'
#     for i in list_angka:
#         if (i == 2):
#             z+= ' |__ '
#         elif (i == 3 or i == 5 or i == 9):
#             z+= '  __| '
#         elif(i == 1 or i == 4 or i == 7):
#             z+= '    | '
#         else:
#             z+= ' |__| '
#     z+='\n'
#     return z

# list = input('Masukkan angka : ').split()
# print(gambar(list))


# def angka_urut(x):
#     y = ''
#     for i in range (1,x*(x-1)+2,x):
#         for j in range (i,i+x,1):
#             y+=str(j)+' '
#         y+='\n'
#     return y

# def angka_random(y):
#     z=''
#     for i in range (0,y):
#         for j in range (0,y):
#             import random
#             rand = random.randint(1,100)
#             z+=str(rand)+' '
#     return z

# while True:
#     ukuran = int(input('Masukkan ukuran : '))
#     print('Menu :\n1. Angka Urut\n2. Angka random\n\n')
#     pilih = input('Pilih menu : ')
#     if pilih == '1':
#         print(angka_urut(ukuran))
#     elif pilih == '2':
#         print(angka_random(ukuran))
#     else:
#         print('Masukkan yang benar')
#         break


# import math
# x = int(input('Masukkan jumlah : '))
# angka = []
# for i in range (x):
#     import random
#     rand = random.randint(1,100)
#     angka.append(rand)

# ratarata = sum(angka)/len(angka)

# total = 0
# for i in angka:
#     kuadrat = (i-ratarata)**2
#     total+=kuadrat

# variansi = total / (len(angka))
# stddev = math.sqrt(variansi)


# import math
# def ascending (angka):    
#     for i in range (len(angka)):
#         for j in range (i+1,len(angka)):
#             if angka[i] > angka[j]:
#                 angka[i],angka[j] = angka[j],angka[i]
#     return angka

# x = int(input('Masukkan jumlah : '))
# angka = []
# for i in range (1,x+1):
#     import random
#     rand = random.randint(1,100)
#     angka.append(rand)
# b = ascending(angka)
# print(b)

# n_median = (len(b)+1)/2
# print(n_median)
# if (len(b))%2 == 0:
#     me_bawah = int(math.floor(n_median))
#     me_atas = int(math.ceil(n_median))
#     median = (b[me_bawah-1]+b[me_atas-1])/2
#     print(me_atas)
#     print(me_bawah)
# else:
#     median = b[int(n_median-1)]
# print(median)


import math
from collections import Counter
def ascending (angka):    
    for i in range (len(angka)):
        for j in range (i+1,len(angka)):
            if angka[i] > angka[j]:
                angka[i],angka[j] = angka[j],angka[i]
    return angka

x = int(input('Masukkan jumlah : '))
angka = []
for i in range (1,x+1):
    import random
    rand = random.randint(1,10)
    angka.append(rand)
b = ascending(angka)
print(b)

n = len(b)
data = Counter(b)
get_mode = dict(data)
modus = [k for k, v in get_mode.items() if v == max(list(data.values()))]
if len(modus) == n:
    datamodus = 'No mode found'
else:
    datamodus = 'Mode is / are : '+str(modus)

print(data)
print(get_mode)
print(max(get_mode.values()))
print(max(get_mode))
print(datamodus)


def jumlah_kata(x):
    kata = {}
    for i in x.lower().split():
        if i in kata.keys():
            kata[i]+=1
        else:
            kata[i]=1
    for keys, j in kata.items():
        print("Jumlah kata '{}' ada sebanyak {}".format(keys.capitalize(),j))

kata = input('Masukkan kalimat : ')
jumlah_kata(kata)