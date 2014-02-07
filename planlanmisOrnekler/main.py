#-*- encoding: utf-8 -*-
#main.py

from settings import *
from siniflar.kisi import Kisi
from depolama.fabrika import DepolamaFabrikasi
from araclar.sqlite import SqliteShell

class Main:
    """
    Kişi ekleme, arama silme işlemlerini yönetir
    """

    def __init__(self):
        self.komut_listesi = []
        self.depolayici = DepolamaFabrikasi.depolayiciyi_getir()

    def print_menu(self):
        print "===Menu==="
        print "- Kişi Ekle   [ekle]"
        print "- Ara         [ara]"
        print "- Herkes      [herkes]"
        print "- Geçmis      [gecmis]"
        print "- Sql Console [sqlite]"
        print "- Çıkış       [cikis]"

    def input(self, prompt):
        str = raw_input(prompt)
        self.komut_listesi.append(str)
        return str

    def ekle(self, args=None):
        kisi = Kisi()

        ad = self.input("Ad: ")
        kisi.set_ad(ad)

        soyad = self.input("Soyad: ")
        kisi.set_soyad(soyad)

        email = self.input("Email: ")
        kisi.set_email(email)

        tckno = self.input("Tck No: ")
        kisi.set_tckno(tckno)

        telno = self.input("Tel No: ")
        kisi.set_telno(telno)

        self.depolayici.kaydet(kisi)
        print "Kisi basariyla eklendi."
        return True

    def gecmis(self, args=None):
        for num, komut in enumerate(self.komut_listesi):
            print "{0:5} => {1}".format(num, komut)

    def ara(self, args):
        """
        tckno=x&ad=y formatında
        """
        query = {}
        for x in args.split("&"):
            k, v = x.split("=")
            query[k] = v

        kisiler = self.depolayici.getir(query)

        for kisi in kisiler:
            print kisi

    def herkes(self, args = None):
        for kisi in self.depolayici:
            print kisi

    def sqlite(self, args):
        shell = SqliteShell(DEPOLAYICI['db'])
        shell.run()

    def run(self):
        while True:
            self.print_menu()

            str = self.input("Secenek: ")
            secenekler = str.split(" ", 1)

            if secenekler[0] in BILINEN_SECENEKLER:
                #Burada default valuede kullanabiliriz ilk başta
                try:
                    islem = getattr(self, secenekler[0])
                    args = islem[1] if len(secenekler) > 1 else None
                    islem(args)
                except AttributeError as e:
                    print e
                    print "Hatalı girdi: {0} su anda gerçekleştirilemiyor.".format(str)
            elif str == "cikis":
                break

if __name__ == "__main__":
    main = Main()
    main.run()
