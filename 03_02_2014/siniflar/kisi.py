class Kisi:
    def __init__(self, ad=None, soyad=None, telno=None, email=None, tckno=None):
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.telno = telno
        self.tckno = tckno

    def __str__(self):
        return self.ad + " " + self.soyad
