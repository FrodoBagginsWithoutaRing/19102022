
def fak(cislo):
    vys=1
    for i in range(2,cislo+1):
        vys*=i
    return vys
def komb(n,k):
    return fak(n)//(fak(k)*fak(n-k))

def psc(riadok:int):
    p=-1
    for cr in range(riadok):
        for space in range(1, (riadok-cr)):
            print(' ',end='')
            #if p//
        for k in range (0,cr+1):
            print (komb(cr,k),end=' ')
        print('')
        p=p+1
psc(10)

def trojuholnik(dlzka:int):
    for tri in range(dlzka):
        for uholnik in range(1,(dlzka-tri)):
            print(' ',end='')
        for hviezdy in range (0,tri+1):
            print('*',end=' ')
        print('')
trojuholnik(0)
