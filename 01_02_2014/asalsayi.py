# -*- coding: utf-8 -*-

for sayi in range(2,100):
  for i in range(2, int(sayi ** 0.5) + 1):
    if  sayi % i == 0:
      break
  else:
    print sayi
