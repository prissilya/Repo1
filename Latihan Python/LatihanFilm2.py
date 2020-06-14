def susunan_kursi(bangku_tersedia, no_bangku):
    
    ada_isi=False

    occupied = ''
    for pointer_bangku in range (1,bangku_tersedia+1):
        for pointer_no_bangku in range (0,len(no_bangku)):
            if (pointer_bangku == no_bangku[pointer_no_bangku]):
                ada_isi = True
                break
            else:
                ada_isi = False
        if ada_isi == True:
            occupied+=' X '
        else:
            occupied+=' 0 '
    return occupied

def pilih_kursi():
    row_kursi_tersedia = 2
    banyak_kursi_tersedia_per_baris = 10
    banyak_tiket = int(input('Masukan banyak tiket : '))

    book_baris_kursi = []
    book_kolom_kursi = []

    for T in range(banyak_tiket):
        kursi_baris_ke  = int(input('Silakan masukan baris kursi yang anda inginkan : '))
        kursi_kolom_ke  = int(input('Silakan masukan kolom kursi yang anda inginkan : '))

        if kursi_baris_ke <= row_kursi_tersedia and kursi_kolom_ke <= banyak_kursi_tersedia_per_baris:
            book_baris_kursi.append(kursi_baris_ke)
            book_kolom_kursi.append(kursi_kolom_ke)
        else:
            print('Input salah, silakan ulangi kembali')
            exit

    for pointer_row_ke_kursi_tersedia in range(0,row_kursi_tersedia):
        book_kursi = [] 
        for counter in range(0,len(book_baris_kursi)):
            if (book_baris_kursi[counter] == pointer_row_ke_kursi_tersedia+1):
                book_kursi.append(book_kolom_kursi[counter])
        
        print (susunan_kursi(banyak_kursi_tersedia_per_baris,book_kursi))

def pesan_tiket():

    global history_film
    global history_jadwal

    print('List Film :\n1. Avengers\n2. DC\n')
    pilihan_film = input('Silakan Pilih Film : ')

    if(pilihan_film == str(1)):
        history_film.append('Avengers')
    else:
        history_film.append('DC')

    print('Jadwal :\n1. Siang\n2. Malam\n')
    pilihan_jadwal = input('Silakan Pilih Jadwal : ')

    if(pilihan_jadwal == str(1)):
        history_jadwal.append('Siang')
    else:
        history_jadwal.append('Malam')

    pilih_kursi()

    return()

def menu ():
    print('\nMenu :\n1. Pesan tiket\n2. Lihat history\n3. Keluar\n')
    pilihan = input('Silakan Pilih Menu : ')
    return pilihan

def history_pesan():

    global history_film
    global history_jadwal

    for counter in range(0, len(history_film)):
        print(str(history_film[counter])+' pada '+str(history_jadwal[counter]))
    return()    

history_film = []
history_jadwal = []

while True:
    
    dipilih=0
    dipilih=menu()

    if(dipilih == str(1)):
        pesan_tiket()
    elif(dipilih == str(2)):
        history_pesan()
    elif(dipilih == str(3)):
        print('Terima Kasih')
        break
    else:
        print('Silakan Masukan Input Yang Benar !')