# -*- coding: utf-8 -*-

a = raw_input("Bir sayi giriniz: ")
toplam = 0

if not a.isdigit():
  print "bir sayi girmeniz gerekiyor."
  exit()

else:
  a = int(a)

while a > 0:
  toplam += a
  a -= 1

print toplam
