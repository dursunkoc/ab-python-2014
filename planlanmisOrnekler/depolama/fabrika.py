#-*- encoding: utf-8 -*-

from depolama.dosya import DosyaDepolayicisi
from depolama.sqlite import SqliteDepolayicisi
from hatalar.depolayici import DepolayiciHatasi
from settings import *

class DepolamaFabrikasi:

    @staticmethod
    def depolayiciyi_getir():
        if DEPOLAYICI['type'] == "dosya":
            return DosyaDepolayicisi(DEPOLAYICI['db'])
        elif DEPOLAYICI['type'] == "sqlite":
            return SqliteDepolayicisi(DEPOLAYICI['db'])
        else:
            raise DepolayiciHatasi("{0} tipinde depolayıcı bulunamadı!")

