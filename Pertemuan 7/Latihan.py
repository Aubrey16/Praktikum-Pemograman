def addMahasiswa():
    jumlah = int (input("jumlah mahasiswa : "))
    mahasiswa = []
    while(jumlah > 0 ):
        nama = input ("Nama mahasiswa: ")
        mahasiswa.append(nama)
        jumlah = jumlah - 1

    while(True):
        panggil(mahasiswa)
        jumlah = jumlah - 1
        if (jumlah<0):
            break

# menghapus data mahasiswa 
def removeDataMahasiswa(arrayMahasiswa):
    mahasiswa = arrayMahasiswa
    print("Data mahasiswa %s" %arrayMahasiswa)
    mahasiswa.remove(input("Hapus mahasiswa: "))
    print("Data mahasiswa %s" %mahasiswa)
    panggil(mahasiswa)

# urutkan data mahasiswa
def ascMahasiswa(arrayMahasiswa):
    mahasiswa = arrayMahasiswa
    mahasiswa.sort()
    print(mahasiswa)
    panggil(mahasiswa)

# lihat data mahasiswa 
def viewMahasiswa(arrayMahasiswa):
    mahasiswa = arrayMahasiswa
    for x in mahasiswa:
        print("nama mahasiswa: %s" %x)
    panggil(mahasiswa)

def panggil(arrayMahasiswa):
    print("------Pilihan-----")
    print("1 Tambah data")
    print("2 Hapus data")
    print("3 Urutkan data")
    print("4 Lihat data")
    print("5 Tutup")

    pilih = int(input("pilih: "))
    if(pilih==1):
        addMahasiswa()
    elif(pilih==2):
        removeDataMahasiswa()
    elif(pilih==3):
        ascMahasiswa()
    elif(pilih==4):
        viewMahasiswa()
    elif(pilih==5):
        print("selesai")

addMahasiswa()