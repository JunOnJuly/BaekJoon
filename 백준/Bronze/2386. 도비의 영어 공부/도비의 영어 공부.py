while (S:=input())!='#':
    a,s=S.split(' ',1)
    s=s.lower()
    print(f'{a} {s.count(a)}')