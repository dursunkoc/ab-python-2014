def dir2(obj):
    yontemler = []
    for e in dir(obj):
            if "__" not in e:
                yontemler.append(e)
    return yontemler

def x():
   print "x"
