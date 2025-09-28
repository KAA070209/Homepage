import os
from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv

# load .env
load_dotenv()

app = Flask(__name__, template_folder='templates')
app.secret_key = os.getenv("SECRET_KEY", "azka123")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profil")
def profil():
    return render_template("profil.html")


@app.route("/suhu", methods=["GET", "POST"])
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


@app.route("/gaji", methods=["GET", "POST"])
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



@app.route("/ujian", methods=["GET", "POST"])
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

@app.route("/Belanja", methods=["GET", "POST"])
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

@app.route("/Rata", methods=["GET", "POST"])
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

@app.route("/beasiswa", methods=["GET", "POST"])
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

@app.route("/member", methods=["GET", "POST"])
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
@app.route("/tiket", methods=["GET", "POST"])
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
    
@app.route("/vocher", methods=["GET" , "POST"])
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

@app.route("/bioskop", methods=["GET", "POST"])
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


@app.route("/kasir", methods=["GET", "POST"])
def kasir():
    if request.method == 'POST':
        AzkaNamaKasir = request.form["AzkaNamaKasir"]
        AzkaHarga = int (request.form["AzkaHarga"])
        AzkaBarang = request.form["AzkaBarang"]
        AzkaJumlahBarang = int (request.form["AzkaJumlahBarang"])
        AzkaPembayaran = request.form["AzkaPembayaran"]
        AzkaKategori = request.form["AzkaKategori"]
        AzkaSub = AzkaHarga*AzkaJumlahBarang
        if AzkaKategori == "Makanan":
            if AzkaSub >= 50000:
                AzkaDiskon = int (AzkaSub*0.1)
            else:
                AzkaDiskon= int (AzkaSub*0.05)   
        elif AzkaSub == "Minuman" :
            if AzkaHarga >= 30000:
                AzkaDiskon = int (AzkaSub*0.07)
            else:
                AzkaDiskon = int (AzkaSub*0.03)
        elif AzkaSub == "lainnya" :
            if AzkaHarga >= 100000:
                AzkaDiskon = int (AzkaSub*0.08)
            else :
                AzkaDiskon = int (AzkaSub*0.02)

        if AzkaPembayaran == "Transfer" :
            AzkaAdmin = 2500
        else:
            AzkaAdmin = 0


        AzkaTotal = AzkaSub - AzkaDiskon + AzkaAdmin

        return render_template("kasir.html",AzkaKategori=AzkaKategori,AzkaNamaKasir=AzkaNamaKasir,AzkaBarang=AzkaBarang,AzkaJumlahBarang=AzkaJumlahBarang,AzkaHarga=AzkaHarga,AzkaSub=AzkaSub,AzkaPembayaran=AzkaPembayaran,AzkaDiskon=AzkaDiskon,AzkaTotal=AzkaTotal)

    return render_template("kasir.html")

@app.route("/operasi", methods=["GET", 'POST'])
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

@app.route('/biodata', methods=['GET', 'POST'])
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


@app.route("/dasar", methods=["GET", "POST"])
def dasar():
    Azkahasil = []
    if request.method == "POST":
        Azkajumlah = request.form.get("Azkajumlah")
        if Azkajumlah and Azkajumlah.isdigit():
            Azkajumlah = int(Azkajumlah)
            Azkahasil = [i for i in range(1, Azkajumlah + 1)]
        return render_template("dasar.html", Azkahasil=Azkahasil)

    return render_template("dasar.html")

@app.route("/faktorial", methods=["GET", "POST"])
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

@app.route("/Perkalian", methods=["GET", "POST"])
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

@app.route("/Bil_Genap", methods=["GET", "POST"])
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

@app.route("/jumlah_nama", methods=["GET", "POST"])
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

@app.route("/input", methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        AzkaAngkaR = int(request.form['AzkaAngkaR'])
        return render_template('nilai_rata_rata.html', AzkaAngkaR=AzkaAngkaR)
    return render_template('nilai_rata_rata.html')


@app.route("/nilai_rata_rata", methods=['GET','POST'])
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

@app.route("/jil_nap", methods=['GET','POST'])
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

@app.route("/prima", methods=['GET','POST'])
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

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5001, debug=True)

