#aturan fuzzy
def turun(a,b,x):
    derajatanggota = (1 if x <=a else (b - x) / (b - a) if x>=b else 0)
    yield derajatanggota

def naik(a,b,x):
    derajatanggota = (0 if x<=a else (x-a)/(b-a) if x >= b else 1)
    yield derajatanggota

def segitig(a,b,c,x):
    derajatanggota = ((x - a) / (b - a) if a <= x <= b else (c - x) / (c - b) if b <= x <= c else 0)
    yield derajatanggota

#daftar keanggotaan
def anggota(jamkerja,barang,gagal):
    jamkerja_sedikit = lambda x: turun(20,40,x)
    jamkerja_sedang = lambda x: segitig(20,40,60, x)
    jamkerja_banyak = lambda x: naik(40,60,x)

    barang_sedikit =lambda x: turun(30,60,x)
    barang_sedang = lambda x: segitig(30,60,105,x)
    barang_banyak = lambda x: naik(60,105, x)

    gagal_sedikit = lambda x: turun(2,3,x)
    gagal_sedang = lambda x: segitig(1,3,6,x)
    gagal_banyak = lambda x: naik(3,6,x)

    #list index untuk rule (0,1,2)
    hasil_jamkerja = [next(jamkerja_sedikit(jamkerja)), next(jamkerja_sedang(jamkerja)), next(jamkerja_banyak(jamkerja))]
    hasil_barang = [next(barang_sedikit(barang)), next(barang_sedang(barang)), next(barang_banyak(barang))]
    hasil_gagal = [next(gagal_sedikit(gagal)), next(gagal_sedang(gagal)), next(gagal_banyak(gagal))]

    inferen(hasil_jamkerja, hasil_barang, hasil_gagal)

def z_baik(x,alfa):
    bbaik = alfa[x] * (70-40) + 70
    yield bbaik
def z_buruk(x,alfa):
    bburuk = 40 - (alfa[x]) * (70-40)
    yield bburuk

def inferen(hasil_jamkerja, hasil_barang, hasil_gagal):
    x = 0
    alfa=[]
    z = []
    lst=[]

    for i, hsljam in enumerate(hasil_jamkerja):
        for j, hslbrg in enumerate (hasil_barang):
            for k, hsgggl in enumerate (hasil_gagal):
                if hsljam > 0 and hslbrg > 0 and hsgggl > 0:
                    lst.clear()
                    lst.extend([hsljam,hslbrg,hsgggl])
                    alfa.append(min(lst))

                    print(alfa)
                    print(z)

                    if i == 0 and j == 0 and k == 2: #1
                        z.append (next(z_buruk(x,alfa)))
                    elif i == 0 and j == 0 and k == 1: #2
                        z.append (next(z_buruk(x,alfa)))
                    elif i == 0 and j == 0 and k == 0: #3
                        z.append (next(z_buruk(x,alfa)))
                    elif i == 0 and j == 1 and k == 2: #4
                        z.append (next(z_buruk(x,alfa)))
                    elif i == 0 and j == 1 and k == 1: #5
                        z.append (next(z_buruk(x,alfa)))
                    elif i == 0 and j == 1 and k == 0: #6
                        z.append (next(z_buruk(x,alfa)))
                    elif i == 0 and j == 2 and k == 2: #7
                        z.append (next(z_buruk(x,alfa)))
                    elif i == 0 and j == 2 and k == 1: #8
                        z.append (next(z_baik(x, alfa)))
                    elif i == 0 and j == 2 and k == 0: #9
                        z.append (next(z_baik(x, alfa)))
                    elif i == 1 and j == 0 and k == 2: #10
                        z.append (next(z_buruk(x,alfa)))
                    elif i == 1 and j == 0 and k == 1: #11
                        z.append (next(z_buruk(x,alfa)))
                    elif i == 1 and j == 0 and k == 0: #12
                        z.append (next(z_baik(x, alfa)))
                    elif i == 1 and j == 1 and k == 2: #13
                        z.append (next(z_buruk(x,alfa)))
                    elif i == 1 and j == 1 and k == 1: #14
                        z.append (next(z_baik(x, alfa)))
                    elif i == 1 and j == 1 and k == 0: #15
                        z.append (next(z_baik(x, alfa)))
                    elif i == 1 and j == 2 and k == 2: #16
                        z.append (next(z_buruk(x,alfa)))
                    elif i == 1 and j == 2 and k == 1: #17
                        z.append (next(z_baik(x, alfa)))
                    elif i == 1 and j == 2 and k == 0: #18
                        z.append (next(z_baik(x, alfa)))
                    elif i == 2 and j == 0 and k == 2: #19
                        z.append (next(z_buruk(x,alfa)))
                    elif i == 2 and j == 0 and k == 1: #20
                        z.append (next(z_baik(x, alfa)))
                    elif i == 2 and j == 0 and k == 0: #21
                        z.append (next(z_baik(x, alfa)))
                    elif i == 2 and j == 1 and k == 2: #22
                        z.append (next(z_buruk(x,alfa)))
                    elif i == 2 and j == 1 and k == 1: #23
                        z.append (next(z_baik(x, alfa)))
                    elif i == 2 and j == 1 and k == 0: #24
                        z.append (next(z_baik(x, alfa)))
                    elif i == 2 and j == 2 and k == 2: #25
                        z.append (next(z_baik(x, alfa)))
                    elif i == 2 and j == 2 and k == 1: #26
                        z.append (next(z_baik(x, alfa)))
                    elif i == 2 and j == 2 and k == 0: #27
                        z.append (next(z_baik(x, alfa)))
                    x +=1
    defuzzy(alfa,z)

def defuzzy(alfa, z):
    hasil = [a*b for a, b in zip(alfa,z)]
    defuz = sum(hasil) / sum(alfa)
    print("Hasil Defuzzifikasi = ", round(defuz, 2), "%")
    print(alfa)
    # print(z)

jamker = int(input("Jumlah Jam Kerja:"))
jumbarang = int(input("Jumlah barang:"))
barangagal = int(input("Barang Gagal:"))
anggota(jamker,jumbarang,barangagal)