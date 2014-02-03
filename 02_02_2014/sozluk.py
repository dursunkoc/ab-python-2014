numaralar = {}

kac = raw_input("kac tane isim eklemek istiyorsunuz? : ")

for i in range(0,int(kac)):    
    isim = raw_input("isim: ")
    numara = raw_input("numara: ")
    numaralar[isim] = numara

print numaralar
