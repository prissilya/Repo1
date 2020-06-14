history_film = []
history_jadwal = []

def menu ():
    print('Menu :\n1. Pesan Tiket\n2. Lihat History\n3. Keluar\n')
    pilih = input('Pilih menu : ')
    return pilih

def pesan_tiket ():
    global history_film
    global history_jadwal

    print ('List film :\n1. Avengers\n2. DC\n')
    film = input('Pilih film : ')
    if film == '1':
        history_film.append('Film Avengers')
    elif film == '2':
        history_film.append('Film DC')
    else:
        print('Input salah. Masukkan yang benar!')
        pesan_tiket()
    
    print ('Jadwal :\n1. Siang\n2. Malam\n')
    jadwal = input('Pilih jadwal : ')
    if jadwal == '1':
        history_jadwal.append(' pada Siang hari')
    elif jadwal == '2':
        history_jadwal.append(' pada Malam hari')
    else:
        print('Input salah. Masukkan yang benar!')
        pesan_tiket()
    pilih_row()
    return()

def pilih_row():
    avail_row = 2
    avail_seat = 10
    tiket = int(input('Masukkan jumlah tiket : '))
    row_list = []
    seat_list = []
    for i in range (tiket):
        row = int(input('Pilih row : '))
        if row <= avail_row:
            row_list.append(row)
        else:
            print('Input salah. Masukkan yang benar!')
            pilih_row()
        seat = int(input('Pilih seat : '))
        if seat <= avail_seat:
            seat_list.append(seat)
    
    print(str(row_list))
    print(str(seat_list))

    for j in range (1,avail_row+1):
        book_list = []
        for k in range (0,len(row_list)):
            if row_list[k]==j:
                book_list.append(seat_list[k])
        print(pilih_seat(avail_seat,book_list))

def pilih_seat(a_seat,no_seat):
    isi = False
    z=''
    for i in range (1,a_seat+1):
        for j in range (len(no_seat)):
            if no_seat[j]==i:
                isi = True
                break
            else:
                isi = False
        if isi == True:
            z+=' X '
        else:
            z+=' 0 '
    return z

def history_pesan():
    global history_film
    global history_jadwal

    for i in range (len(history_film)):
        print(history_film+history_jadwal)
    return ()

while True:
    pilihan = 0
    pilihan = menu()

    if pilihan == '1':
        pesan_tiket()
    elif pilihan == '2':
        history_pesan()
    elif pilihan == '3':
        print('Terima kasih!')
        break
    else:
        print('Input salah. Masukkan yang benar!')
    

