def fonksiyon(arg1 = 0, arg2 = 1):
        print arg1, arg2

print "fonksioyn (2,3): "
fonksiyon(2,3)
print "fonksiyon (): "
fonksiyon()

def fib(sayi):
        a,b = 0,1
        for i in range(0,sayi):
                print b,
                a,b = b,a+b

fib(10)



