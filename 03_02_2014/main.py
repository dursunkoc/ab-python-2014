from siniflar.kisi import Kisi
from depolama.dosya import DosyaDepolayacisi
from ayarlar import *

class Main():

    def __init__(self):
        self.depolayici = DosyaDepolayacisi(DOSYA)

    def menu(self):
        print "Kisi ekle [ekle]"
        print "Kisi ara  [ara]"
        print "Cikis     [cikis]"
    
    def ekle(self):
        ad = raw_input("Ad: ")
        soyad = raw_input("Soyad: ")
        eposta = raw_input("Eposta: ")
        telno = raw_input("Telno: ")
        tckno = raw_input("Tckno: ")

        eklenen_kisi = Kisi(ad, soyad, eposta, telno, tckno)
        self.depolayici.kaydet(eklenen_kisi)
        print eklenen_kisi, "\n"
        
        print "Kisi basariyla eklendi."

    def ara(self, sorgu):
        kisiler = self.depolayici.getir(sorgu)
        print kisiler

    def calistir(self):
        girdi = ""
        while girdi != "cikis":
            self.menu()
            girdi = raw_input("Yapmak istediginiz islem: ")

            if girdi == "ekle":
                self.ekle()
            if girdi == "ara":
                print "Ornek sorgu formati: ad=kisi_adi&soyad=kisi_soyadi..."
                sorgu = raw_input("Sorguyu yaziniz: ")
                self.ara(sorgu)


main = Main()
main.calistir()
