import os, sys, time

stokItem= [
    {
        'ID': '1',
        'Merk' : 'Gibsun',
        'Tipe' : 'Les Mail',
        'Thn. Produksi' : '1958',
    }
]
deskripsiItem = ['ID', 'Merk', 'Tipe', 'Thn. Produksi']

def exit():
    print("\n Terimakasih telah menggunakan program ini...")
    for i in range(3,0,-1): 
        print(f"Anda akan otomatis keluar pada {i} detik lagi!")
        time.sleep(1)
        print("\033[F\033[K", end='')
    return sys.exit()

def showItem(stokItem: list):

    def checkOneItem(stokItem, inTemp2):
        for i in stokItem:
            if i['ID'] == inTemp2:
                print(f"\nBerikut informasi mengenai item ID : {inTemp2}")
                for j in deskripsiItem:
                    if j == deskripsiItem[-1]:
                        print(f"{j} : {i[j]}", end='\n')
                    else:
                        print(f"{j} : {i[j]}", end='|\t')
                input('''...Tekan "ENTER" untuk melanjutkan...''')
                return showItem(stokItem)
        else: 
            print("\nData tidak ditemukan...")
            input('''...Tekan "ENTER" untuk melanjutkan...''')
            return showItem(stokItem)

    os.system("cls")
    print("==MIKE's GUITAR STORE==")
    print("==Laporan Stok Item==")
    print("1. Tampilkan seluruh data")
    print("2. Tampilkan data tertentu")
    print("3. Kembali ke menu utama")
    try:
        inTemp = int(input("Pilih salah satu nomor antara 1-3: "))
    except:
        print("\nMasukan tidak valid. Mohon beri masukan anatara nomor 1-3!") 
        input('''...Tekan "ENTER" untuk melanjutkan...''')
        return showItem(stokItem)
    if inTemp<1 or inTemp>3:
            print("\nMasukan tidak valid. Mohon beri masukan anatara nomor 1-3!") 
            input('''...Tekan "ENTER" untuk melanjutkan...''')
            return showItem(stokItem)
    if inTemp == 1:
        if len(stokItem) == 0:
            print("\nTidak ada stok apa-apa...")
            input('''...Tekan "ENTER" untuk melanjutkan...''')
            return showItem(stokItem)
        else:
            print('\nBerikut informasi mengenai stok item')
            for i in stokItem:
                for j in deskripsiItem:
                    if j == deskripsiItem[-1]:
                        print(f"{j} : {i[j]}", end='\n')
                    else:
                        print(f"{j} : {i[j]}", end='|\t')
            input('''...Tekan "ENTER" untuk melanjutkan...''')
            return showItem(stokItem)
    elif inTemp == 2:
        if len(stokItem) == 0:
            print("\nTidak ada stok apa-apa...")
            input('''...Tekan "ENTER" untuk melanjutkan...''')
            return showItem(stokItem)
        else:
            inTemp2 = input("\nMasukan ID item: ")
            checkOneItem(stokItem, inTemp2)

    elif inTemp == 3:
        main()


    
def insertItem(stokItem: list):
    
    def cekKosong(inTemp):
        if len(inTemp) == 4:
            try:
                for i in range(3):
                    inTemp[i] = inTemp[i].upper()
                inTemp[-1] = int(inTemp[-1])
                return False
            except:
                print(f"Pastikan untuk format {deskripsiItem[0]}, {deskripsiItem[1]}, {deskripsiItem[2]} => Huruf, Angka dan {deskripsiItem[-1]} => Int (bilangan bulat)")
                return True
        else: return True
        
    def cekAvail(stokItem, ID):
        for i in stokItem:
            if i['ID'] == ID: return False
        else: return True

    os.system("cls")
    print("==MIKE's GUITAR STORE==")
    print("==Masukan Stok Item==")
    print("1. Masukan item")
    print("2. Kembali ke menu utama")      
    try:
        inTemp = int(input("Pilih salah satu nomor antara 1-2: "))
    except:
        print("\nMasukan tidak valid. Mohon beri masukan anatara nomor 1-2!") 
        input('''...Tekan "ENTER" untuk melanjutkan...''')
        return insertItem(stokItem)
    if inTemp<1 or inTemp>2:
            print("\nMasukan tidak valid. Mohon beri masukan anatara nomor 1-2!") 
            input('''...Tekan "ENTER" untuk melanjutkan...''')
            return insertItem(stokItem)

    if inTemp == 1:
        inTemp = input(f"\nMasukan detail dari item (contoh {deskripsiItem[0]}; {deskripsiItem[1]}; {deskripsiItem[2]}; {deskripsiItem[3]}) : ").split(';')
        inTempDict = {}
        if cekKosong(inTemp):
            print(f'Data yang anda masukan kurang lengkap mohon periksa masukan {deskripsiItem[1]}; {deskripsiItem[2]}; {deskripsiItem[3]}!')
        elif cekAvail(stokItem, inTemp[0]):
            for i in range(len(list(inTemp))):
                inTempDict[str(deskripsiItem[i])] = inTemp[i]
            inYN = input("Apakah data akan disimpan Y/N? ")
            if inYN.lower() == 'y': 
                stokItem.append(inTempDict)
                print("Data berhasil dimasukan!")
            else:
                print("Data batal dimasukan")
                input('''...Tekan "ENTER" untuk melanjutkan...''')
                return insertItem(stokItem)
        else:
            print("ID item sudah pernah ada, mohon masukan ID item yang berbeda!")
        input('''...Tekan "ENTER" untuk melanjutkan...''')
        return insertItem(stokItem)
    elif inTemp == 2:
        return main()

def updateItem(stokItem: list):

    def cekAvail(stokItem, ID):
        for i in stokItem:
            if i['ID'] == ID:
                for j in deskripsiItem:
                    if j == deskripsiItem[-1]:
                        print(f"{j} : {i[j]}", end='\n')
                    else:
                        print(f"{j} : {i[j]}", end='|\t')
                return True
        else: return False

    def changeKolom(stokItem, inTempChange, inTarget):
        if inTempChange.lower() != deskripsiItem[0].lower():
            for i in deskripsiItem:
                if i.lower() == inTempChange.lower():
                    inKolomChange = input(f"Masukan {i} baru: ")
                    for j in stokItem:
                        if j['ID'] == inTarget:
                            try:
                                j[str(i)] = inKolomChange if inTempChange.lower() != deskripsiItem[-1].lower() else int(inKolomChange)
                                print("Data berhasil di update!")
                                input('''...Tekan "ENTER" untuk melanjutkan...''')
                                return updateItem(stokItem)
                            except:
                                print(f"Untuk format {deskripsiItem[1]}, {deskripsiItem[2]} => Huruf, Angka dan {deskripsiItem[-1]} => Int (bilangan bulat)")
                                input('''...Tekan "ENTER" untuk melanjutkan...''')
                                for _ in range(3):
                                    print("\033[F\033[K", end='')
                                return changeKolom(stokItem, inTempChange, inTarget)
                            
                            
            else:
                print("\nKolom tidak ditemukan!") 
                input('''...Tekan "ENTER" untuk melanjutkan...''')
                return updateItem(stokItem)
        else:
            print(f"!!!{deskripsiItem[0]} Tidak dapat dirubah!!!")
            input('''...Tekan "ENTER" untuk melanjutkan...''')
            return updateItem(stokItem)

    os.system("cls")
    print("==MIKE's GUITAR STORE==")
    print("==Perbarui Stok Item==")
    print("1. Perbarui item")
    print("2. Kembali ke menu utama")
    try:
        inTemp = int(input("Pilih salah satu nomor anatara 1-2: "))
    except:
        print("\nMasukan tidak valid. Mohon beri masukan anatara nomor 1-2!") 
        input('''...Tekan "ENTER" untuk melanjutkan...''')
        return updateItem(stokItem)
    if inTemp<1 or inTemp>2:
        print("\nMasukan tidak valid. Mohon beri masukan anatara nomor 1-2!") 
        input('''...Tekan "ENTER" untuk melanjutkan...''')
        return updateItem(stokItem)
    if inTemp == 1:
        inTarget = input("\nMasukan ID item: ")
        if cekAvail(stokItem, inTarget):

            inAccess = input("Apakah data benar Y/N? ")
            if inAccess.lower()  == 'y':
                inTempChange = input(f"Masukan kolom item yang ingin diedit: ")
                changeKolom(stokItem, inTempChange, inTarget)
            elif inAccess.lower() == 'n' :
                return updateItem(stokItem) 
        else:
            print("\nData tidak ditemukan!") 
            input('''...Tekan "ENTER" untuk melanjutkan...''')
            return updateItem(stokItem)
    elif inTemp == 2:
        return main()

def deleteItem(stokItem: list):

    def cekAvail(stokItem, ID):
        for i in stokItem:
            if i['ID'] == ID:
                for j in deskripsiItem:
                    if j == deskripsiItem[-1]:
                        print(f"{j} : {i[j]}", end='\n')
                    else:
                        print(f"{j} : {i[j]}", end='|\t')
                return True
        else: return False

    os.system("cls")
    print("==MIKE's GUITAR STORE==")
    print("==Hapus Stok Item==")
    print("1. Hapus item")
    print("2. Kembali ke menu utama")
    try:
        inTemp = int(input("Pilih salah satu nomor anatara 1-2: "))
    except:
        print("\nMasukan tidak valid. Mohon beri masukan anatara nomor 1-2!") 
        input('''...Tekan "ENTER" untuk melanjutkan...''')
        return deleteItem(stokItem)
    if inTemp<1 or inTemp>2:
        print("\nMasukan tidak valid. Mohon beri masukan anatara nomor 1-2!") 
        input('''...Tekan "ENTER" untuk melanjutkan...''')
        return deleteItem(stokItem)
    if inTemp == 1:
        inTarget = input("\nMasukan ID item: ")
        if cekAvail(stokItem, inTarget):
            inAccess = input("Apakah data benar Y/N? ")
            if inAccess.lower()  == 'y':
                for i in stokItem:
                    if i['ID'] ==  inTarget:
                        stokItem.remove(i)
                        print('Data berhasil dihapus!')
                        input('''...Tekan "ENTER" untuk melanjutkan...''')
                        return deleteItem(stokItem)
            elif inAccess.lower() == 'n':
                return deleteItem(stokItem) 
        else:
            print("\nData tidak ditemukan!") 
            input('''...Tekan "ENTER" untuk melanjutkan...''')
            return deleteItem(stokItem)
    elif inTemp == 2:
        return main()

def main():
    os.system("cls")
    print("==MIKE's GUITAR STORE==")
    print("==Database Stok Gitar==")
    print("1. Daftar Stok")
    print("2. Masukan Item")
    print("3. Perbarui Stok")
    print("4. Hapus Item")
    print("5. Exit/ Keluar")
    try:    
        in0 = int(input("Pilih salah satu nomor antara 1-5: "))
    except:
        print("\nMasukan tidak valid. Mohon beri masukan anatara nomor 1-5!") 
        input('''...Tekan "ENTER" untuk melanjutkan...''')
        return main()
    if in0<1 or in0>5:
        print("\nMasukan tidak valid. Mohon beri masukan anatara nomor 1-5!") 
        input('''...Tekan "ENTER" untuk melanjutkan...''')
        return main()
    
    if in0 == 1: showItem(stokItem)
    elif in0 == 2: insertItem(stokItem)
    elif in0 == 3: updateItem(stokItem)
    elif in0 == 4: deleteItem(stokItem)
    elif in0 == 5: exit()

if __name__ == '__main__' :
    main()