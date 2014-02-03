def tersCevir(dizi):
        dizi2 = []
        for i in range(len(dizi)-1, -1, -1):
                dizi2.append(dizi[i])
        return dizi2



def tersCevir(dizi):
    dizi2= []
    for i in range(1, len(dizi)+1):
        dizi2.append(dizi[-i])
    return dizi2

dizi = [1,2,3,4,5]
dizi2 = tersCevir2(dizi)
print dizi2
