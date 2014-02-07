# -*- coding:utf-8 -*-

import random
class AmiralBatti():
        
        def __init__(self, oyunMatris):
                self.oyunMatris = oyunMatris
                self.oyunMatrisGemiSayisi = 0
                self.oyuncuMatrisGemiSayisi = 0
                #Oyun Gemi sayisini hesaplar
                for m in range(len(oyunMatris)):
                        self.oyunMatrisGemiSayisi += oyunMatris[m].count("G") 
                #
                self.oyuncuMatris = [["0" for x in range(10)] for y in range(10)]
        
        def ates(self,x,y):
                #Oyuncu Gemi sayisini hesaplar
                self.oyuncuMatrisGemiSayisi = 0
                for m in range(len(self.oyuncuMatris)):
                        self.oyuncuMatrisGemiSayisi += self.oyuncuMatris[m].count("X") 
                #
                if self.oyunMatrisGemiSayisi == self.oyuncuMatrisGemiSayisi:
                        print "oyunu kazandiniz"
                        exit()
                         
                if self.oyunMatris[x][y] == "G":
                        print "vurdunuz"
                        self.oyuncuMatris[x][y] = "X"
                else:
                        print "vuramadiniz"
                        self.oyuncuMatris[x][y] = "&"
                self.goster()

    
        def goster(self):
                oyuncuMatris = self.oyuncuMatris
                print " ", " ".join([str(x) for x in range(len(oyuncuMatris))])
                for i, x in enumerate(oyuncuMatris):
                    print i, " ".join([str(y) for y in x])
        
# Rasgele bir tane 5 uzunlukta gemi olustur
yeniOyunMatris = [["0" for x in range(10)] for y in range(10)]
for k in range(4):
    a = random.randint(0,9)
    b = random.randint(0,5)
    for i in range(0,5):
        while yeniOyunMatris[a][b+i] != "G":
            yeniOyunMatris[a][b+i] = "G"
    b = random.randint(0,9)
    a = random.randint(0,5)
    for i in range(0,4):
        while yeniOyunMatris[a+i][b] != "G":
            yeniOyunMatris[a+i][b] = "G"
#


yeniOyun = AmiralBatti(yeniOyunMatris)
yeniOyun.goster()
girdi=""
while girdi !="cikis":   
        girdi = raw_input("Örnek girdi = x,y: | Çıkmak için 'cikis' yazin> ")
        if girdi == "cikis":
               break
        yeniOyun.ates(int(girdi.split(",")[0]),int(girdi.split(",")[1]))
