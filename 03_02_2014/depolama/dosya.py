import pickle

class DosyaDepolayacisi:
    def __init__(self, dosya):
        self.dosya = dosya
        self.kisiler = self.__oku()

    def __yaz(self):
        pickle.dump(self.kisiler, open(self.dosya, "w"))

    def kaydet(self, kisi):
        self.kisiler.append(kisi)
        self.__yaz()
    
    def __oku(self):
        try:
           return pickle.load(open(self.dosya))
        except IOError:
           return []

    def getir(self, sorgu):
        self.kisiler = self.__oku()
        bulunanlar = []

        for kisi in self.kisiler:
            kontrol_listesi = sorgu.split("&")
            buldukmu = True

            for kontrol in kontrol_listesi:
                liste = kontrol.split("=")
                deger = getattr(kisi, liste[0])
                if deger != liste[1]:
                   buldukmu = False
                   break

            if buldukmu:
               bulunanlar.append(kisi)

        return bulunanlar
