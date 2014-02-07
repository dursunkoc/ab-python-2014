#-*- encoding: utf-8 -*-

from hatalar.ad import *
from hatalar.soyad import *
from hatalar.email import *
from hatalar.tckno import *
from hatalar.telno import *
from siniflar.kisi import Kisi
import re

class Ogrenci(Kisi):
    """
    Ogrencilere ait bilgileri tuttugumuz sinif 
    """

    def __init__(self, ad=None, soyad=None, email=None, tckno=None, telno=None, ogrencino=None):
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.tckno = tckno
        self.telno = telno
        self.ogrencino = ogrencino

	def set_ogrencino(self, ogrencino):
 		ogrencino_kalibi = re.compile("\d{5}")

		if ogrencino_kalibi.match(ogrencino):
			self.telno = telno
		else:
			raise GecersizOgrencino("{0} geçersiz bir ogrenci numarasi")
	
