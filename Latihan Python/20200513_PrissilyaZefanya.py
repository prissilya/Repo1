array = int(input('Masukkan Jumlah Array yang diinginkan : '))
list = []
for i in range (1,array+1):
    data = int(input('Masukkan data ke-'+str(i)+' : '))
    list.append(data)
pilih = input('Menu :\n1. Lihat Array\n2. Sort Array\n3. Nilai tertinggi dan terendah\n4. Jumlah Ganjil dan Genap\n5. Keluar\n\nSilahakan pilih salah satu dari menu di atas : ')
if (pilih=='1'):
    print(list)
elif (pilih=='2'):
    sort = input('1. Ascending\n2. Descending\n\nPilih salah satu : ')
    if (sort=='1'):
        def sort_ascending (x):
            for j in range (len(x)):
                for k in range (j+1,len(x)):
                    if x[j]>x[k]:
                        x[j],x[k] = x[k],x[j]
            return x
        print('Urutan list kamu dari yang paling kecil adalah : '+str(sort_ascending(list)))
    elif (sort=='2'):
        def sort_descending (y):
            for j in range (len(y)):
                for k in range (j+1,len(y)):
                    if y[j]<y[k]:
                        y[j],y[k] = y[k],y[j]
            return y
        print('Urutan list kamu dari yang paling besar adalah : '+str(sort_descending(list)))
    else :
        print('Masukkan data yang benar'+str(sort))
elif (pilih=='3'):
    sort_ascending(list)
    print ('Nilai terendah dari list adalah : '+str(list[0]))
    sort_descending (list)
    print('Nilai tertinggi dari list adalah : '+str(list[0]))
elif (pilih=='4'):
    def bilangan(x):
        ganjil=[]
        genap=[]
        for i in range(len(x)):
            if (x[i]%2==0):
                genap.append(x[i])
            else:
                ganjil.append(x[i])
        print('Berikut adalah value genap dari list kamu : '+str(genap))
        print('Berikut adalah value ganjil dari list kamu : '+str(ganjil))
    bilangan(list)
elif (pilih=='5'):
    print('Terima kasih')
else:
    print('Silahkan masukkan pilihan yang benar\n'+pilih)
