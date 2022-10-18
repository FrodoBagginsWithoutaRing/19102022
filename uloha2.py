
#def obdlznik(dlzka:int,znak:str):
    #print(dlzka)
#dlzka=10
#znak='*'
def obdlzik(dlzka,znak):

        for i in range(1,dlzka+1):
            print(znak,end='')
        print('')
        print(znak,(dlzka-4)*(' '),znak)
        for i in range(1,dlzka+1):
            print(znak,end='')
obdlzik(12,'*')
