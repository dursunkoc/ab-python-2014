#-*- encoding: utf-8 -*-

from depolama.arayuz import DepolamaArayuzu
import pickle

class DosyaDepolayicisi(DepolamaArayuzu):

    def __init__(self, dosya):
        self.dosya = dosya
        self.kisiler = self.__oku()

    def __oku(self):
        try:
            kisiler = pickle.load(open(self.dosya, "rb"))
        except IOError:
            kisiler = []

        return kisiler

    def __yaz(self, kisiler):
        pickle.dump(kisiler, open(self.dosya, "wb"))


    def kaydet(self, kisi):
        self.kisiler.append(kisi)
        self.__yaz(self.kisiler)

    def getir(self, query):
        eslesenler = []

        for kisi in self.kisiler:
            eslestimi = True
            for k,v in query.items():
                if getattr(kisi, k, None) != v:
                    eslestimi = False

            if eslestimi:
                eslesenler.append(kisi)

        return eslesenler

    def __iter__(self):
        self.index = len(self.kisiler)
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.kisiler[self.index]


