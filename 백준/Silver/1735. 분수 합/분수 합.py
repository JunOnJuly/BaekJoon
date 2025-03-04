a,b=map(int,input().split())
c,d=map(int,input().split())
e=(a*d)+(b*c)
f=b*d
while True:
    g=min(e,f)
    for i in range(2,g+1):
        if not e%i and not f%i:
            e//=i
            f//=i
            break
    if g==min(e,f):
        print(f'{e} {f}')
        break