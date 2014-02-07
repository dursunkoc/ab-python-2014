#-*- encoding: utf-8 -*-

from depolama.arayuz import DepolamaArayuzu
from siniflar.kisi import Kisi
from araclar.getfields import info
import sqlite3


class SqliteDepolayicisi(DepolamaArayuzu):
    def __init__(self, dosya):
        self.dosya = dosya
        self.connection = sqlite3.connect(self.dosya)
        self.cursor = self.connection.cursor()

    def __getir_sql_sorgusu(self, filtre):
        pass

    def getir(self, filtre):
        pass

    def __kaydet_sql_sorgusu(self, kisi):
        ozellikler = info(kisi)
        degerler = ",".join(["'"+getattr(kisi, ozellik)+"'" for ozellik in ozellikler])

        if isinstance(kisi, Kisi):
            type = "Kisi"
        else:
            raise TypeError("Tanımlı bir tip olmadığından kaydedilemedi")

        sql = "INSERT INTO kisiler (type, {1}) VALUES ('{0}', {2})".format(type, ",".join(ozellikler), degerler)

        return sql

    def kaydet(self, kisi):
        sql = self.__kaydet_sql_sorgusu(kisi)
        print sql
        self.cursor.execute(sql)
        self.connection.commit()
