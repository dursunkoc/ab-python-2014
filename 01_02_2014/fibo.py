# -*- coding: utf-8 -*-

sayi = raw_input("sayi giriniz: ")

if not sayi.isdigit():
  print "sayi giriniz"
  exit()

else:
  sayi = int(sayi)

dongu = 0
temp = 0
a = 1
b = 1

print a

while dongu < sayi:
    print b
    temp = b
    b = a + b
    a = temp
    dongu += 1

