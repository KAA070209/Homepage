from flask import Flask, render_template, url_for, request, redirect
from dotenv import dotenv_values

application = Flask(__name__)

application.config.update(dotenv_values(".env"))


@application.route('/index')
def index():
    return render_template("index.html")

@application.route("/")
def profil():
    return render_template("profil.html")

@application.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nama = request.form["nama"]
        email = request.form["email"]
        pesan = request.form["pesan"]
        return render_template("contact.html", sukses=True, nama=nama)
    return render_template("contact.html")



@application.route("/suhu", methods=["GET", "POST"])
def suhu():
    if request.method == "POST":
        AzkaCuaca = request.form["AzkaCuaca"]
        AzkaSuhu = int(request.form["AzkaSuhu"])

        if AzkaCuaca == "Hujan":
            if AzkaSuhu <= 25:
                AzkaSaran = "Bawa Payung dan Jaket"
            else:
                AzkaSaran = "Bawa Payung aja"
        elif AzkaCuaca == "Cerah":
            if AzkaSuhu > 30:
                AzkaSaran = "Pakai Kacamata Hitam dan Minum Air"
            else:
                AzkaSaran = "Nikmati Hari Ini"
        else:
            AzkaSaran = "Data Tidak Valid"

        return render_template("suhu.html",
                               AzkaCuaca=AzkaCuaca,
                               AzkaSuhu=AzkaSuhu,
                               AzkaSaran=AzkaSaran)
    return render_template("suhu.html")


@application.route("/gaji", methods=["GET", "POST"])
def gaji():
    if request.method == "POST":
        AzkaNama = request.form["AzkaNama"]
        AzkaStatus = request.form["AzkaStatus"]
        AzkaGaji = int(request.form["AzkaGaji"])
        AzkaLembur = request.form["AzkaLembur"]
        AzkaJam = int(request.form["AzkaJam"])

        if AzkaStatus == "Tetap":
            if AzkaGaji >= 5000000:
                AzkaBonus = int(AzkaGaji * 0.1)
            else:
                AzkaBonus = int(AzkaGaji * 0.05)

        elif AzkaStatus == "Kontrak":
            if AzkaGaji >= 5000000:
                AzkaBonus = int(AzkaGaji * 0.03)
            else:
                AzkaBonus = 0
        else:
            AzkaStatus = "Data Tidak Sesuai"
            AzkaBonus = 0

        if AzkaLembur == "Iya":
            if AzkaJam >= 10:
                AzkaTambahan = 200000
            elif AzkaJam < 10 and AzkaJam >= 1:
                AzkaTambahan = 100000
            else:
                AzkaLembur = "Data Tidak Valid"
                AzkaTambahan = 0
        elif AzkaLembur == "Tidak":
            AzkaTambahan = 0
        else:
            AzkaLembur = "Data Tidak Valid"
            AzkaTambahan = 0

        AzkaGajiKotor = AzkaGaji + AzkaBonus + AzkaTambahan
        AzkaPajak = int(AzkaGajiKotor * 0.02)
        AzkaGajiBersih = AzkaGajiKotor - AzkaPajak

        return render_template(
            "gaji.html",
            AzkaNama=AzkaNama,
            AzkaStatus=AzkaStatus,
            AzkaGaji=AzkaGaji,
            AzkaBonus=AzkaBonus,
            AzkaJam=AzkaJam,
            AzkaTambahan=AzkaTambahan,
            AzkaGajiKotor=AzkaGajiKotor,
            AzkaPajak=AzkaPajak,
            AzkaGajiBersih=AzkaGajiBersih
        )


    return render_template("gaji.html")



@application.route("/ujian", methods=["GET", "POST"])
def ujian():
    if request.method == 'POST':
        AzkaNamaUjian = request.form["AzkaNamaUjian"]
        AzkaUTS = int(request.form["AzkaUTS"])
        AzkaUAS = int(request.form["AzkaUAS"])
        AzkaTugas = int(request.form["AzkaTugas"])
        AzkaPraktek = int(request.form["AzkaPraktek"])
        AzkaAkhir = (AzkaUTS*0.25) + (AzkaUAS*0.35) + (AzkaTugas*0.20) + (AzkaPraktek*0.20)
        if AzkaAkhir >= 85:
            AzkaPredikat = "Lulus dengan Predikat A"
        elif 75 <= AzkaAkhir < 85:
            if AzkaPraktek >= 80:
                AzkaPredikat = "Lulus dengan Predikat B"
            else:
                AzkaPredikat = "Remedial Praktek"
        elif 65 <= AzkaAkhir < 75:
            if AzkaTugas >= 70:
                AzkaPredikat = "Lulus dengan Predikat C"
            else:
                AzkaPredikat = "Remedial Tugas"
        elif 50 <= AzkaAkhir < 65:
            if AzkaUAS >= 60:
                AzkaPredikat = "Remedial UTS & Tugas"
            else:
                AzkaPredikat = "Remedial UAS"
        else:
            AzkaPredikat = "Tidak Lulus"

        return render_template("ujian.html",
                               AzkaNamaUjian=AzkaNamaUjian,
                               AzkaUTS=AzkaUTS,
                               AzkaUAS=AzkaUAS,
                               AzkaTugas=AzkaTugas,
                               AzkaPraktek=AzkaPraktek,
                               AzkaAkhir=AzkaAkhir,
                               AzkaPredikat=AzkaPredikat)

    return render_template("ujian.html")

@application.route("/Belanja", methods=["GET", "POST"])
def Belanja():
    if request.method == 'POST':
        AzkaNamaBelanja = request.form["AzkaNamaBelanja"]
        AzkaNamaBarang = request.form["AzkaNamaBarang"]
        AzkaBarang = int (request.form["AzkaBarang"])
        AzkaJumlah = int (request.form["AzkaJumlah"])
        AzkaTotalBelanja = AzkaBarang*AzkaJumlah
        if AzkaTotalBelanja >= 50000:
            AzkaDiskon = int  (AzkaTotalBelanja*0.1)
        elif AzkaTotalBelanja >= 20000 and AzkaTotalBelanja <=50000 :
            AzkaDiskon = int (AzkaTotalBelanja*0.05)
        elif AzkaTotalBelanja < 20000 :
            AzkaDiskon = int (AzkaTotalBelanja*0)
        AzkaTotalBayar = AzkaTotalBelanja - AzkaDiskon
        return render_template("Belanja.html",
                                AzkaNamaBelanja=AzkaNamaBelanja,
                                AzkaNamaBarang=AzkaNamaBarang,
                                AzkaBarang=AzkaBarang,
                                AzkaJumlah=AzkaJumlah,
                                AzkaTotalBelanja=AzkaTotalBelanja,
                                AzkaDiskon=AzkaDiskon,
                                AzkaTotalBayar=AzkaTotalBayar)

    return render_template("Belanja.html")

@application.route("/Rata", methods=["GET", "POST"])
def Rata():
    if request.method == 'POST':
        AzkaNamaSiswa = request.form["AzkaNamaSiswa"]
        AzkaMapel1 = request.form["AzkaMapel1"]
        AzkaMapel2 = request.form["AzkaMapel2"]
        AzkaMapel3 = request.form["AzkaMapel3"]
        AzkaNilai1 = int (request.form["AzkaNilai1"])
        AzkaNilai2 = int (request.form["AzkaNilai2"])
        AzkaNilai3 = int (request.form["AzkaNilai3"])
        AzkaHasil = int (AzkaNilai1+AzkaNilai2+AzkaNilai3)
        AzkaRataRata = int (AzkaHasil /3 )
        if AzkaRataRata >= 90 :
            AzkaKategori = "A (Sangat Baik)"
        elif AzkaRataRata >= 75 :
            AzkaKategori = "B (Baik)"
        elif AzkaRataRata >= 60 :
            AzkaKategori = "C (Cukup)"
        elif AzkaRataRata < 60 :
            AzkaKategori = "D (Kurang)"
        
        return render_template("Rata-Rata.html",
                                AzkaNamaSiswa=AzkaNamaSiswa,
                                AzkaMapel1=AzkaMapel1,
                                AzkaMapel2=AzkaMapel2,
                                AzkaMapel3=AzkaMapel3,
                                AzkaNilai1=AzkaNilai1,
                                AzkaNilai2=AzkaNilai2,
                                AzkaNilai3=AzkaNilai3,
                                AzkaKategori=AzkaKategori,
                                AzkaRataRata=AzkaRataRata)

    return render_template("Rata-Rata.html")

@application.route("/beasiswa", methods=["GET", "POST"])
def beasiswa():
    if request.method == 'POST':
        AzkaNamaSiswaBeasiswa = request.form["AzkaNamaSiswaBeasiswa"]
        AzkaNilai =int (request.form["AzkaNilai"])
        AzkaPenghasilan = int (request.form["AzkaPenghasilan"])
        AzkaJumlah = int (request.form["AzkaJumlah"])
        AzkaStatus = request.form["AzkaStatus"]
        if AzkaNilai >= 85 :
            AzkaPoin1 = 30
        else:
            AzkaPoin1 = 0

        if AzkaPenghasilan <=2000000:
            AzkaPoin2 = 20
        else:
            AzkaPoin2 = 0

        if AzkaJumlah > 2 :
            AzkaPoin3 =10 
        else:
            AzkaPoin3 = 0

        if AzkaStatus != "MilikSendiri" :
            AzkaPoin4 = 10
        else:
            AzkaPoin4 = 0

        AzkaHasilAkhir = AzkaPoin1+AzkaPoin2+AzkaPoin3+AzkaPoin4

        if AzkaHasilAkhir >= 60:
            AzkaHasil= "Anda berhak mendapatkan beasiswa"
        else:
            AzkaHasil = "Belum berhak mendapatkan beasiswa"

        return render_template("beasiswa.html",
                                AzkaNamaSiswaBeasiswa=AzkaNamaSiswaBeasiswa,
                                AzkaNilai=AzkaNilai,
                                AzkaPenghasilan=AzkaPenghasilan,
                                AzkaJumlah=AzkaJumlah,
                                AzkaStatus=AzkaStatus,
                                AzkaHasil=AzkaHasil,
                                AzkaHasilAkhir=AzkaHasilAkhir)

    return render_template("beasiswa.html")

@application.route("/member", methods=["GET", "POST"])
def member():
    if request.method == 'POST':
        AzkaNamaMember = request.form["AzkaNamaMember"]
        AzkaMember = request.form["AzkaMember"]
        AzkaBarang = request.form["AzkaBarang"]
        AzkaJumlah = int (request.form["AzkaJumlah"])
        if AzkaBarang == "Martabak":
            AzkaHargaNormal = 30000
        elif AzkaBarang =="Pizza":
            AzkaHargaNormal = 55000
        elif AzkaBarang == "Burger":
            AzkaHargaNormal = 20000
        elif AzkaBarang == "Spagheti":
            AzkaHargaNormal = 15000
        elif AzkaBarang == "Roti Bakar":
            AzkaHargaNormal = 15000
        
        if AzkaMember == "Reguler":
            AzkaDiskon = int (AzkaHargaNormal*0.02)
        elif AzkaMember == "Premium":
            AzkaDiskon = int (AzkaHargaNormal*0.04)
        else:
            AzkaDiskon=0

        DiskonMember = AzkaHargaNormal - AzkaDiskon
        AzkaTotal = int (DiskonMember*AzkaJumlah)
        if AzkaTotal >= 500000 and AzkaMember == "Premium":
            AzkaDiskon = int (AzkaTotal*0.02)
        else:
            AzkaDiskon=0

        AzkaHasil=AzkaTotal-AzkaDiskon
        return render_template("Diskon_Barang_Member.html",
                                    AzkaNamaMember=AzkaNamaMember,
                                    AzkaMember=AzkaMember,
                                    AzkaBarang=AzkaBarang,
                                    AzkaJumlah=AzkaJumlah,
                                    AzkaTotal=AzkaTotal,
                                    DiskonMember=DiskonMember,
                                    AzkaHargaNormal=AzkaHargaNormal,
                                    AzkaDiskon=AzkaDiskon,
                                    AzkaHasil=AzkaHasil)

    return render_template("Diskon_Barang_Member.html")  
@application.route("/tiket", methods=["GET", "POST"])
def tiket():
    if request.method == 'POST':
        AzkaNamaTiket = request.form["AzkaNamaTiket"]
        AzkaUmur = int (request.form["AzkaUmur"])
        AzkaHari = request.form["AzkaHari"]
        if AzkaUmur <= 12 :
            AzkaHarga = 30000
        elif AzkaUmur <= 17 :
            AzkaHarga = 40000
        elif AzkaUmur >= 18 :
            AzkaHarga = 50000

        if AzkaHari == "Senin" or AzkaHari == "Selasa" or AzkaHari == "Rabu"  or AzkaHari =="Kamis" :
            AzkaDiskon = 5000
        elif AzkaHari == "Jumat" :
            AzkaDiskon =  3000
        else :
            AzkaDiskon = 0

        AzkaTotal = AzkaHarga - AzkaDiskon

        return render_template("tiket.html",
                                AzkaNamaTiket=AzkaNamaTiket,
                                AzkaUmur=AzkaUmur,
                                AzkaHari=AzkaHari,
                                AzkaHarga=AzkaHarga,
                                AzkaTotal=AzkaTotal,
                                AzkaDiskon=AzkaDiskon)

    return render_template("tiket.html")
    
@application.route("/vocher", methods=["GET" , "POST"])
def vocher():
    if request.method == 'POST':
        AzkaPelanggan = request.form['AzkaPelanggan']
        AzkaBarang = request.form['AzkaBarang']
        AzkaHarga = int ( request.form['AzkaHarga'])
        AzkaJumlah = int( request.form['AzkaJumlah'])
        AzkaStatus = request.form['AzkaStatus']
        AzkaMetode = request.form['AzkaMetode']

        AzkaTotalBarang = AzkaHarga*AzkaJumlah
        if AzkaStatus == "Gold":
            AzkaDiskon = int (AzkaTotalBarang*0.2)
        elif AzkaStatus == "Silver":
            AzkaDiskon = int (AzkaTotalBarang*0.1)
        else:
            AzkaDiskon = int (AzkaTotalBarang*0)

        if AzkaMetode== "Transfer":
            AzkaAdmin = 2500
        else:
            AzkaAdmin = 0

        AzkaTotalBelanja = AzkaTotalBarang - AzkaDiskon + AzkaAdmin

        if AzkaTotalBelanja > 500000 and AzkaStatus=="Gold":
            AzkaVocher = "Anda Mendapatkan Vocher Bonus"
        else:
            AzkaVocher = ""

        return render_template("vocher.html",
                                AzkaPelanggan=AzkaPelanggan,
                                AzkaBarang=AzkaBarang,
                                AzkaJumlah=AzkaJumlah,
                                AzkaStatus=AzkaStatus,
                                AzkaMetode=AzkaMetode,
                                AzkaAdmin=AzkaAdmin,
                                AzkaHarga=AzkaHarga,
                                AzkaTotalBelanja=AzkaTotalBelanja,
                                AzkaTotalBarang=AzkaTotalBarang,
                                AzkaDiskon=AzkaDiskon,
                                AzkaVocher=AzkaVocher)
        
    return render_template("vocher.html")

@application.route("/bioskop", methods=["GET", "POST"])
def bioskop():
    if request.method == 'POST':
        AzkaNamaBioskop = request.form["AzkaNamaBioskop"]
        AzkaFilm = request.form["AzkaFilm"]
        AzkaJadwal = request.form["AzkaJadwal"]
        AzkaJumlah = int (request.form["AzkaJumlah"])
        AzkaPembayaran = request.form["AzkaPembayaran"]
        if AzkaFilm == "GalaksiBiru" :
            AzkaHarga = 40000
        elif AzkaFilm == "MisteriSenja" :
            AzkaHarga = 45000
        elif AzkaFilm == "AksiTanpaBatas" :
            AzkaHarga = 50000

        if AzkaPembayaran == "Transfer":
            AzkaAdmin = 2000
        else:
            AzkaAdmin = 0

        AzkaSub = AzkaJumlah * AzkaHarga

        if AzkaJumlah >= 5 :
            AzkaDiskon = int (AzkaSub*0.1)
        else:
            AzkaDiskon = 0

        AzkaTotal = AzkaSub - AzkaDiskon + AzkaAdmin

        return render_template("bioskop_bugigin.html",
                                AzkaNamaBioskop=AzkaNamaBioskop,
                                AzkaFilm=AzkaFilm,
                                AzkaJadwal=AzkaJadwal,
                                AzkaHarga=AzkaHarga,
                                AzkaTotal=AzkaTotal,
                                AzkaDiskon=AzkaDiskon,
                                AzkaAdmin=AzkaAdmin,
                                AzkaSub=AzkaSub,
                                AzkaJumlah=AzkaJumlah)

    return render_template("bioskop_bugigin.html")


@application.route("/kasir", methods=["GET", "POST"])
def kasir():
    if request.method == 'POST':
        AzkaNamaKasir = request.form["AzkaNamaKasir"]
        AzkaHarga = int(request.form["AzkaHarga"])
        AzkaBarang = request.form["AzkaBarang"]
        AzkaJumlahBarang = int(request.form["AzkaJumlahBarang"])
        AzkaPembayaran = request.form["AzkaPembayaran"]
        AzkaKategori = request.form["AzkaKategori"]

        AzkaSub = AzkaHarga * AzkaJumlahBarang

        if AzkaKategori == "Makanan":
            if AzkaSub >= 50000:
                AzkaDiskon = int(AzkaSub * 0.1)
            else:
                AzkaDiskon = int(AzkaSub * 0.05)

        elif AzkaKategori == "Minuman":
            if AzkaHarga >= 30000:
                AzkaDiskon = int(AzkaSub * 0.07)
            else:
                AzkaDiskon = int(AzkaSub * 0.03)

        elif AzkaKategori == "lainnya":
            if AzkaHarga >= 100000:
                AzkaDiskon = int(AzkaSub * 0.08)
            else:
                AzkaDiskon = int(AzkaSub * 0.02)

        else:
            AzkaDiskon = 0   


        if AzkaPembayaran == "Transfer":
            AzkaAdmin = 2500
        else:
            AzkaAdmin = 0

        AzkaTotal = AzkaSub - AzkaDiskon + AzkaAdmin

        return render_template(
            "kasir.html",
            AzkaKategori=AzkaKategori,
            AzkaNamaKasir=AzkaNamaKasir,
            AzkaBarang=AzkaBarang,
            AzkaJumlahBarang=AzkaJumlahBarang,
            AzkaHarga=AzkaHarga,
            AzkaSub=AzkaSub,
            AzkaPembayaran=AzkaPembayaran,
            AzkaDiskon=AzkaDiskon,
            AzkaAdmin=AzkaAdmin,
            AzkaTotal=AzkaTotal
        )

    return render_template("kasir.html")

@application.route("/operasi", methods=["GET", 'POST'])
def operasi():
    azka = 5
    bazka = 10

    Azka1 = azka + bazka
    Azka2 = azka - bazka
    Azka3 = azka / bazka
    Azka4 = azka * bazka

    Azka5 = azka == bazka
    Azka6 = azka > bazka
    Azka7 = azka < bazka
    Azka8 = azka <= bazka
    Azka9 = azka >= bazka

    return render_template('operasi.html',
                            azka=azka,
                            bazka=bazka,
                            Azka1=Azka1,
                            Azka2=Azka2,
                            Azka3=Azka3,
                            Azka4=Azka4,
                            Azka5=Azka5,
                            Azka6=Azka6,
                            Azka7=Azka7,
                            Azka8= Azka8,
                            Azka9=Azka9)

    return render_template('operasi.html')

@application.route('/biodata', methods=['GET', 'POST'])
def biodata():
        
    if request.method == "POST":
        AzkaNIS = request.form["AzkaNIS"]
        AzkaLengkap = request.form["AzkaLengkap"]
        AzkaAsal = request.form["AzkaAsal"]
        AzkaLama = request.form["AzkaLama"]
        AzkaLamaBulan =request.form["AzkaLamaBulan"]
        AzkaJurusan = request.form["AzkaJurusan"]
        AzkaTempat = request.form['AzkaTempat']
        AzkaTanggal = request.form["AzkaTanggal"]
        AzkaJenis = request.form['AzkaJenis']
        AlamatAzka = request.form['AlamatAzka']
        AzkaHobi = request.form['AzkaHobi']


        return render_template("biodata.html",
                                        AzkaNIS=AzkaNIS,
                                        AzkaLengkap=AzkaLengkap,
                                        AzkaAsal=AzkaAsal,
                                        AzkaLama=AzkaLama,
                                        AzkaLamaBulan=AzkaLamaBulan,
                                        AzkaJurusan=AzkaJurusan,
                                        AzkaTempat=AzkaTempat,
                                        AzkaTanggal=AzkaTanggal,
                                        AzkaJenis=AzkaJenis,
                                        AlamatAzka=AlamatAzka,
                                        AzkaHobi=AzkaHobi)
    
    return render_template("biodata.html")


@application.route("/dasar", methods=["GET", "POST"])
def dasar():
    Azkahasil = []
    if request.method == "POST":
        Azkajumlah = request.form.get("Azkajumlah")
        if Azkajumlah and Azkajumlah.isdigit():
            Azkajumlah = int(Azkajumlah)
            Azkahasil = [i for i in range(1, Azkajumlah + 1)]
        return render_template("dasar.html", Azkahasil=Azkahasil)

    return render_template("dasar.html")

@application.route("/faktorial", methods=["GET", "POST"])
def faktorial():
    AzkahasilFak = None
    AzkaangkaFak = None
    if request.method == "POST":
        AzkaangkaFak = request.form.get("AzkaangkaFak")
        if AzkaangkaFak and AzkaangkaFak.isdigit():
            AzkaangkaFak = int(AzkaangkaFak)
            Azkafaktorial = 1
            for i in range(1, AzkaangkaFak + 1):
                Azkafaktorial *= i
            AzkahasilFak = Azkafaktorial
        return render_template("faktorial.html", AzkaangkaFak=AzkaangkaFak, AzkahasilFak=AzkahasilFak)
    return render_template("faktorial.html")

@application.route("/Perkalian", methods=["GET", "POST"])
def Perkalian():
    AzkahasilPer = []
    AzkaangkaPer = None
    if request.method == "POST":
        AzkaangkaPer = request.form.get("AzkaangkaPer")
        if AzkaangkaPer and AzkaangkaPer.isdigit():
            AzkaangkaPer = int(AzkaangkaPer)
            for iazka in range(1, 11):
                AzkahasilPer.append(f"{AzkaangkaPer} x {iazka} = {AzkaangkaPer * iazka}")
        return render_template("Perkalian.html", AzkaangkaPer=AzkaangkaPer, AzkahasilPer=AzkahasilPer)
    return render_template("Perkalian.html")

@application.route("/Bil_Genap", methods=["GET", "POST"])
def Bil_Genap():
    AzkahasilGen = None
    AzkaangkaGen = None
    AzkaGenap = 0  
    if request.method == "POST":
        AzkaangkaGen = request.form.get("AzkaangkaGen")
        if AzkaangkaGen and AzkaangkaGen.isdigit():
            AzkaangkaGen = int(AzkaangkaGen)
            AzkaGenap = 0  
            for i in range(2, AzkaangkaGen + 1):
                if i % 2 == 0:
                    AzkaGenap += i
                AzkahasilGen = AzkaGenap
        return render_template("Bil_Genap.html", AzkaangkaGen=AzkaangkaGen, AzkahasilGen=AzkahasilGen, AzkaGenap=AzkaGenap)
    return render_template("Bil_Genap.html")

@application.route("/jumlah_nama", methods=["GET", "POST"])
def jumlah_nama():
    AzkaNamaA = ""
    HasilAzka = []

    if request.method == "POST":
        AzkajumlahA = request.form.get("AzkajumlahA")
        AzkaNamaA = request.form.get("AzkaNamaA")
        if AzkajumlahA and AzkajumlahA.isdigit():
            AzkajumlahA = int(AzkajumlahA)
            for inama in range(AzkajumlahA):
                HasilAzka.append(f"{inama + 1}. {AzkaNamaA}")

        return render_template("jumlah_nama.html", AzkajumlahA=AzkajumlahA, AzkaNamaA=AzkaNamaA, HasilAzka=HasilAzka)
    return render_template("jumlah_nama.html")

@application.route("/input", methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        AzkaAngkaR = int(request.form['AzkaAngkaR'])
        return render_template('nilai_rata_rata.html', AzkaAngkaR=AzkaAngkaR)
    return render_template('nilai_rata_rata.html')


@application.route("/nilai_rata_rata", methods=['GET','POST'])
def nilai_rata_rata():
    AzkaAngkaR =  request.form.get('AzkaAngkaR')
    AzkaList = []
    AzkaRataRataR=None
    if AzkaAngkaR:  
        AzkaAngkaR = int(AzkaAngkaR)
    
        if f"AzkaNilaiR1" in request.form:
            for AzkaJumlahR in range(1, AzkaAngkaR + 1):
                AzkaNilaiR = request.form.get(f"AzkaNilaiR{AzkaJumlahR}")
                if AzkaNilaiR:
                    AzkaList.append(int(AzkaNilaiR))

            if AzkaList:
                AzkaRataRataR = sum(AzkaList) / len(AzkaList)



    return render_template(
        'nilai_rata_rata.html',
        AzkaAngkaR=AzkaAngkaR,
        AzkaRataRataR=AzkaRataRataR
    )

@application.route("/jil_nap", methods=['GET','POST'])
def jil_nap():
    AzkaKet = []
    AzkaAngkaJ = request.form.get('AzkaAngkaJ')
    if AzkaAngkaJ and AzkaAngkaJ.isdigit():
        AzkaAngkaJ = int(AzkaAngkaJ)
        for iazkaa in range(1, AzkaAngkaJ+1):
            if iazkaa %2 == 0:
                AzkaKet.append(f"{iazkaa} Genap")
            else:
                AzkaKet.append(f"{iazkaa} Ganjil")

    return render_template('jil_nap.html', AzkaAngkaJ=AzkaAngkaJ,AzkaKet=AzkaKet )

@application.route("/prima", methods=['GET','POST'])
def prima():
    AzkaKetP = []
    AzkaAngkaP = request.form.get('AzkaAngkaP')
    if not AzkaAngkaP:
        return render_template('prima.html', AzkaAngkaP=None, AzkaKetP=[])
    AzkaAngkaP = int(AzkaAngkaP)
    for AzkaNilaiP in range(1,AzkaAngkaP+1):
        AzkaCek = 0
        for AzkaBilangan in range(1, AzkaNilaiP+1):
            if  AzkaNilaiP %AzkaBilangan == 0:
                AzkaCek += 1
        if AzkaCek == 2 :
            AzkaKetP.append(f"{AzkaBilangan} Prima")
        else:
            AzkaKetP.append(f"{AzkaBilangan} Bukan Prima")

    return render_template('prima.html', AzkaAngkaP=AzkaAngkaP,AzkaKetP=AzkaKetP )

@application.route('/penjumlahan', methods=['GET', 'POST'])
def penjumlahan():
    if request.method == "POST":
        AzkaAngkaP = int(request.form['AzkaAngkaP'])

        iP = 1
        AzkajumlahP = 0

        while iP <= AzkaAngkaP:
            AzkajumlahP += iP
            iP += 1

        return render_template('penjumlahan.html', AzkajumlahP=AzkajumlahP, AzkaAngkaP=AzkaAngkaP)

    return render_template('penjumlahan.html')

@application.route("/ganjil_genap_while", methods=['GET','POST'])
def ganjil_genap_while():
    if request.method == "POST":
            AzkaAngkaW = int(request.form['AzkaAngkaW'])
            iW = 1
            AzkajumlahgenapW = 0
            Azkajumlah_ganjilW = 0

            while iW <= AzkaAngkaW:
                if iW % 2 == 0:
                    AzkajumlahgenapW += iW
                else:
                    Azkajumlah_ganjilW += iW
                iW += 1

            return render_template(
                    'ganjil_genap_while.html',
                    AzkaAngkaW=AzkaAngkaW,
                    AzkajumlahgenapW=AzkajumlahgenapW,
                    Azkajumlah_ganjilW=Azkajumlah_ganjilW
                )
    return render_template('ganjil_genap_while.html')

@application.route('/daringcpdk1', methods=['GET', 'POST'])
def daringcpdk1():
    AzkahasilCPDK = ""
    if request.method == 'POST':
        AzkabatasCPDK = int(request.form['AzkabatasCPDK'])
        for iAzkaCPDK in range(1, AzkabatasCPDK + 1):
            for jAzkaCPDK in range(1, AzkabatasCPDK + 1):
                AzkahasilCPDK += str(iAzkaCPDK * jAzkaCPDK) + " "
            AzkahasilCPDK += "<br>"
        return render_template('daringcpdk1.html', AzkahasilCPDK=AzkahasilCPDK)
    return render_template("daringcpdk1.html")

@application.route('/daringcpdk2', methods=['GET', 'POST'])
def daringcpdk2():
    AzkahasilCPDK2 = ""
    if request.method == 'POST':
        AzkabatasCPDK2 = int(request.form['AzkabatasCPDK2'])
        for iAzkaCPDK2 in range(1, AzkabatasCPDK2 + 1):
            for jAzkaCPDK2 in range(1, AzkabatasCPDK2 + 1):
                AzkahasilCPDK2 += str(iAzkaCPDK2) + " "
            AzkahasilCPDK2 += "<br>"
        return render_template('daringcpdk2.html', AzkahasilCPDK2=AzkahasilCPDK2)
    return render_template("daringcpdk2.html")

@application.route('/daringcpdk3', methods=['GET', 'POST'])
def daringcpdk3():
    AzkahasilCPDK3 = ""
    if request.method == 'POST':
        AzkabatasCPDK3 = int(request.form['AzkabatasCPDK3'])
        for iAzkaCPDK3 in range(AzkabatasCPDK3):
            AzkaangkaCPDK3 = 1
            for jAzkaCPDK3 in range(iAzkaCPDK3 + 1):
                AzkahasilCPDK3 += str(AzkaangkaCPDK3) + " "
                AzkaangkaCPDK3 = AzkaangkaCPDK3 * (iAzkaCPDK3-jAzkaCPDK3)//(jAzkaCPDK3+1)
            AzkahasilCPDK3 += "<br>"
        return render_template('daringcpdk3.html', AzkahasilCPDK3=AzkahasilCPDK3)
    return render_template("daringcpdk3.html")

@application.route('/daringcpdk4', methods=['GET', 'POST'])
def daringcpdk4():
    if request.method == 'POST':
        jumlah_kelas_Azka = int(request.form['jumlah_kelas_Azka'])
        jumlah_siswa_Azka = int(request.form['jumlah_siswa_Azka'])
        return redirect(url_for('input_nilai', jumlah_kelas_Azka=jumlah_kelas_Azka, jumlah_siswa_Azka=jumlah_siswa_Azka))
    return render_template('daringcpdk4.html', page='home_Azka')


@application.route('/input_nilai', methods=['GET', 'POST'])
def input_nilai():
    jumlah_kelas_Azka = int(request.args.get('jumlah_kelas_Azka', 0))
    jumlah_siswa_Azka = int(request.args.get('jumlah_siswa_Azka', 0))
    class_names = [chr(65 + i) for i in range(jumlah_kelas_Azka)]
    return render_template('daringcpdk4.html', page='input_Azka',
                           jumlah_kelas_Azka=jumlah_kelas_Azka,
                           jumlah_siswa_Azka=jumlah_siswa_Azka,
                           class_names=class_names)


@application.route('/hasil', methods=['POST'])
def hasil():
    jumlah_kelas_Azka = int(request.form['jumlah_kelas_Azka'])
    jumlah_siswa_Azka = int(request.form['jumlah_siswa_Azka'])

    data_kelas_Azka = {}
    rata_per_kelas_Azka = {}

    for i in range(jumlah_kelas_Azka):
        nama_kelas_Azka = f"Kelas {chr(65 + i)}"
        data_kelas_Azka[nama_kelas_Azka] = []
        total_Azka = 0
        for j in range(jumlah_siswa_Azka):
            Azkanama = request.form[f'Azkanama_{i}_{j}']
            Azkanilai = float(request.form[f'Azkanilai_{i}_{j}'])
            data_kelas_Azka[nama_kelas_Azka].append((Azkanama, Azkanilai))
            total_Azka += Azkanilai
        rata_per_kelas_Azka[nama_kelas_Azka] = total_Azka / jumlah_siswa_Azka

    return render_template('daringcpdk4.html', page='hasil_Azka',
                           data_kelas_Azka=data_kelas_Azka,
                           rata_per_kelas_Azka=rata_per_kelas_Azka)

@application.route('/Segitiga_Angka', methods=['GET', 'POST'])
def Segitiga_Angka():
    AzkahasilSA = ""
    if request.method == 'POST':
        AzkaAngkaSA1 = int(request.form['AzkaAngkaSA1'])
        AzkaAngkaSA2 = int(request.form['AzkaAngkaSA2'])
        for iAzkaSA in range(AzkaAngkaSA1,AzkaAngkaSA2+1):
            for jAzkaSA in range(AzkaAngkaSA1,iAzkaSA+1):
                AzkahasilSA += str(jAzkaSA) + " "
            AzkahasilSA += "<br>"
        return render_template('Segitiga_Angka.html', AzkahasilSA=AzkahasilSA)
    return render_template('Segitiga_Angka.html')

@application.route('/Penjualan_Cabang', methods=['GET', 'POST'])
def Penjualan_Cabang():
    if request.method == 'POST':
        jumlah_cabang_Azka = int(request.form['jumlah_cabang_Azka'])
        return redirect(url_for('input_barang', jumlah_cabang_Azka=jumlah_cabang_Azka))
    return render_template('Penjualan_Cabang.html', page='home')

@application.route('/input_barang', methods=['GET', 'POST'])
def input_barang():
    jumlah_cabang_Azka = int(request.args.get('jumlah_cabang_Azka', 0))

    if request.method == 'POST':
        return redirect(url_for('hasil_Azka'))

    return render_template('Penjualan_Cabang.html', page='input_barang', jumlah_cabang_Azka=jumlah_cabang_Azka)

@application.route('/hasil_detail', methods=['GET', 'POST'])
def hasil_detail():
    if request.method == 'POST' and 'lanjut' in request.form:
        jumlah_cabang_Azka = int(request.form['jumlah_cabang_Azka'])
        data_Azka = []

        for iAzkaCabang in range(jumlah_cabang_Azka):
            jumlah_barang_Azka = int(request.form[f'jumlah_barang_Azka_{iAzkaCabang}'])
            data_Azka.append(jumlah_barang_Azka)

        return render_template('Penjualan_Cabang.html', page='detail_barang', jumlah_cabang_Azka=jumlah_cabang_Azka, data_Azka=data_Azka)
    return redirect(url_for('Penjualan_Cabang'))

@application.route('/hasil_Azka', methods=['POST'])
def hasil_Azka():
    jumlah_cabang_Azka = int(request.form['jumlah_cabang_Azka'])
    grand_total_Azka = 0
    hasil_data_Azka = [] 

    for iAzkaCabang in range(jumlah_cabang_Azka):
        jumlah_barang_Azka = int(request.form[f'jumlah_barang_Azka_{iAzkaCabang}'])
        cabang_data_Azka = []
        total_cabang_Azka = 0
        for jAzkaCabang in range(jumlah_barang_Azka):
            nama_Azka = request.form[f'nama_Azka_{iAzkaCabang}_{jAzkaCabang}']
            harga_Azka = int(request.form[f'harga_Azka_{iAzkaCabang}_{jAzkaCabang}'])
            qty_Azka = int(request.form[f'qty_Azka_{iAzkaCabang}_{jAzkaCabang}'])
            total_Azka = harga_Azka * qty_Azka
            total_cabang_Azka += total_Azka
            cabang_data_Azka.append({'no': jAzkaCabang + 1, 'nama': nama_Azka, 'harga': harga_Azka, 'qty': qty_Azka, 'total': total_Azka})
        hasil_data_Azka.append({'cabang': iAzkaCabang + 1, 'barang': cabang_data_Azka, 'total_cabang': total_cabang_Azka})
        grand_total_Azka += total_cabang_Azka

    return render_template('Penjualan_Cabang.html', page='hasil_Azka', hasil_data_Azka=hasil_data_Azka, grand_total_Azka=grand_total_Azka)
if __name__ == '__main__':
    application.run(debug=True)
