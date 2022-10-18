def epitaf(n,text=''):
    x='*'
    a=int(len(text))
    if a%2==0:
        for i in range(0,int((n//2))-int((a//2))):
            print(x, end='')
        print(text,end='')
        for i in range(int((n/2))+int((a//2)),40):
            print(x, end='')
        print("")
    else:
        for i in range(0,int((n//2))-int(((a+1)//2))):
            print(x, end='')
        print(text,end='')
        for i in range(int((n/2))+int((a//2)),40):
            print(x, end='')
        print("")
sir = 40
epitaf(sir)
epitaf(sir, 'Ján Botto')
epitaf(sir, 'Žltá ľalija')
epitaf(sir, '-')
epitaf(sir, 'Stojí stojí mohyla')
epitaf(sir, 'Na mohyle zlá chvíľa')
epitaf(sir, 'na mohyle tŕnie chrastie')
epitaf(sir, 'a v tom tŕní chrastí rastie')
epitaf(sir)

