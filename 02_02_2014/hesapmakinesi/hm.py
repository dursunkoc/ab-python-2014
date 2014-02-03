from lib.moduller import *

s1 = int(raw_input("sayi1: "))
s2 = int(raw_input("sayi2: "))
islem = raw_input("islem: + - / * us kok: ")

if islem == "+":
        print topla(s1,s2)
elif islem == "-":
        print cikart(s1,s2)
elif islem == "/":
        print bol(s1,s2)
elif islem == "*":
        print carp(s1,s2)
elif islem == "us":
        print us(s1,s2)
elif islem == "kok":
        print kok(s1,s2)
else:
        print "yanlis bir sey girdiniz"



