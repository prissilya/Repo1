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
        print('Input salah, silakan ulangi kembali');
        exit

for pointer_row_ke_kursi_tersedia in range(0,row_kursi_tersedia):
    book_kursi = [] 
    for counter in range(0,len(book_baris_kursi)):
        if (book_baris_kursi[counter] == pointer_row_ke_kursi_tersedia+1):
            book_kursi.append(book_kolom_kursi[counter])
    
    print (susunan_kursi(banyak_kursi_tersedia_per_baris,book_kursi))