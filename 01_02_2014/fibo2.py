# -*- coding: utf-8 -*-

a,b = 0, 1

sayi = int(raw_input("sayi gir: "))

sayac = 0

while sayac < sayi:
    print b,
    a, b = b, a+b
    sayac += 1
