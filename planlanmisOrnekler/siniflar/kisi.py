#-*- encoding: utf-8 -*-

from hatalar.ad import *
from hatalar.soyad import *
from hatalar.email import *
from hatalar.tckno import *
from hatalar.telno import *
import re

class Kisi:
    """
    Kisilere ait bilgilerimizi tuttugumuz sınıf
    """

    def __init__(self, ad=None, soyad=None, email=None, tckno=None, telno=None):
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.tckno = tckno
        self.telno = telno

    def __str__(self):
        return "{0} {1} {2} {3} {4}".format(self.ad, self.soyad, self.email, self.tckno, self.telno)

    def set_ad(self, ad):
        """
        Ad alfanumerik olmalıdır
        """
        if ad.isalpha():
            self.ad = ad
        else:
            raise GecersizAd("{0} geçersiz karakterler içeriyor".format(ad))

    def set_soyad(self, soyad):
        """
        Ad alfanumerik olmalıdır
        """
        if soyad.isalpha():
            self.soyad = soyad
        else:
            raise GecersizSoyad("{0} geçersiz karakterler içeriyor".format(soyad))

    def set_email(self, email):
        """
        Ad alfanumerik olmalıdır
        """
        fields = email.split('@')
        if len(fields) != 2:
            raise GecersizEmail("{0} geçersiz bir email adresi".format(email))

        self.email = email

    def set_tckno(self, tckno):
        """
        * 11 hanelidir.
        * Her hanesi rakamsal değer içerir.
        * İlk hane 0 olamaz.
        * 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından,
          2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında,
          elde edilen sonucun 10'a bölümünden kalan, yani
          Mod10'u bize 10. haneyi verir.
        * 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından
          elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
        """
        if len(tckno) != 11:
            raise GecersizTckno("Tck No 11 haneli olmalıdır")

        for c in tckno:
            if not c.isdigit():
                raise GecersizTckno("Tck No Sadece Sayılardan oluşmalıdır")

        if tckno[0] == "0":
            raise GecersizTckno("Tck No da ilk hane 0 olamaz")

        toplam1 = 0
        toplam2 = 0

        for i in range(0, 9, 2):
            toplam1 += int(tckno[i])
        for i in range(1, 8, 2):
            toplam2 += int(tckno[i])

        if (toplam1 * 7  - toplam2) % 10 != int(tckno[9]):
            raise GecersizTckno("Toplamlar eşit değil")

        toplam3 = 0
        for c in tckno[:-1]:
            toplam3 += int(c)

        if (toplam3 % 10) != int(tckno[-1]):
            raise GecersizTckno("Toplamlar eşit değil")

        self.tckno = tckno

    def set_telno(self, telno):
        """
        Regex telno kontrolü ekleyelim.
        """
        telno_kalip = re.compile(r'^(\d{3})-(\d{3})-(\d{2})-(\d{2})$')
        if telno_kalip.match(telno):
            self.telno = telno
        else:
            raise GecersizTelno("{0} geçersiz bir tel numarası!")

