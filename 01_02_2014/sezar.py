# -*- coding: utf-8 -*-

secenek = raw_input("Şifrelemek için 1'e \n Çözmek için 2'ye basınız: ")
anahtar = raw_input("Anahtar'ı giriniz: ")
metin = raw_input("Metin'i giriniz: ")

sonuc = ""

if int(secenek) == 1:
  for harf in metin:
    sonuc += chr((ord(harf) + int(anahtar)) % 255)
elif int(secenek) == 2:
  for harf in metin:
    sonuc += chr(abs(ord(harf) - int(anahtar)) % 255)

else:
  exit()

print sonuc
