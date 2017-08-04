nama = []
nip = []
gaji = []
try:
    while True:
        print("Program Input Pegawai")
        print("1. Input Data\n2. Lihat Data\n3. Cari Data\n4. total gaji\n5. Hapus Data\n6. Keluar")
        masuk = input("Masukkan Pilihan : ")
        if masuk == '1':
            try:
                banyak = int(input("Berapa Karyawan : "))
                print("\n=========>masukkan data<=========\n")
                for i in range(banyak):
                    print("Data ke-", (i+1))
                    name = input("Nama\t: ")
                    numb = input("NIP\t\t: ")
                    salary = int(input("Gaji\t: "))
                    nama = nama + [name]
                    nip = nip + [numb]
                    gaji = gaji + [salary]
                    print('-----------------------------------------')
                print("\n=========>Data Berhasil Masuk !<=========\n")
            except :
                print("\n====>>>>>Error!, Salah Masukan!\n")

        elif masuk=='2':
            print("\n=========>Semua data<=========\n")
            if len(gaji) != 0:
                for i in range(len(nama)):
                    print('Nama\t:', nama[i], '\nNIP\t\t:',nip[i],'\nGaji\t:', gaji[i] )
                    print("==========================================")

            else:
                print("\nData Kosong !\n")
        elif masuk=='3':
            reaksi=0
            if len(gaji) != 0:
                cari = input('NIP \t\t:')
                for i in range(len(nip)):
                    if cari ==nip[i]:
                        print("======================================================")
                        print('Nama\t:',nama[i],'\nNIP\t\t:',nip[i], '\nGaji\t:',gaji[i],)
                        print("======================================================")
                        reaksi+=1
                    else:
                        pass
                if reaksi==0:
                    print("\n=====================>Data Tidak ditemukan !\n")
                reaksi=0
            elif len(gaji)==0:
                print("\nData Kosong !\n")
            else:
                print("Error!")

        elif masuk=='4':
            temp=0
            if len(gaji) != 0:
                for i in range(len(gaji)):
                    temp+=gaji[i]
                print("\nJumlah Seluruh Gaji Karyawan : ", temp, '\n')
            else:
                print("\nData Kosong !\n")

        elif masuk=='5':
            aksi = 0
            if len(gaji) != 0:
                while True:
                    print('\n1. Hapus Berdasarkan NIP\n2. Hapus dari belakang\n3. Hapus dari depan\n4. Hapus Semua \n5. Kembali Ke menu ')
                    hapus = input('Masukkam Pilihan Gan : ')
                    if hapus=='1':
                        ni = input("Masukkan NIP : ")
                        for i in range(len(nip)):
                           # print(nip[i])
                            if ni==nip[i]:
                                nip.remove(nip[i])
                                nama.remove(nama[i])
                                gaji.remove(gaji[i])
                                aksi+=1
                        if aksi==0:
                            print("data Tidak ditemukan\n")
                        else:
                            print("berhasil Menghapus!\n")
                        aksi=0
                    elif hapus=='2':
                        if len(nip)==0:
                            print("Data kosong !\n")
                        else:
                            nip.remove(nip[len(nip)-1])
                            nama.remove(nama[len(nip)-1])
                            gaji.remove(gaji[len(nip)-1])
                    elif hapus=='3':
                        if len(nip)==0:
                            print("Data Sudah Kosong!\n")
                        else:
                            nip.remove(nip[0])
                            nama.remove(nama[0])
                            gaji.remove(gaji[0])
                    elif hapus=='4':
                        if len(nip)==0:
                            print("Data Kosong !")
                        else:
                            for i in range(len(nip)):
                                nip.pop()
                                nama.pop()
                                gaji.pop()
                    elif hapus=='5':
                        break
                    else:
                        print("Masukkan Salah !")
            else:
                print("Data Kosong !")
        elif masuk=='6':
            break
        else:
            print("\n=========>salah Inputan<=========\n")
except:
    print("program Eror!")