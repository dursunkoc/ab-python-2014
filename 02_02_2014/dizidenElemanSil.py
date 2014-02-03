def sil(dizi, eleman):
        """ 
          
          istenen elemani diziden temizleyen fonksiyon
       
        """
        for i in range(0,dizi.count(eleman)):
                dizi.remove(eleman)
        return dizi

dizi = ["a","e","c","d","e","e","e"]
print dizi
print sil(dizi, "e")
