#-*- encoding: utf-8 -*-

class GecersizEmail(Exception):
    """
    Geçersiz email olduğunda yükseltilen hata
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value