#-*- encoding: utf-8 -*-

class GecersizTckno(Exception):
    """
    Geçersiz tckno olduğunda yükseltilen hata
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value