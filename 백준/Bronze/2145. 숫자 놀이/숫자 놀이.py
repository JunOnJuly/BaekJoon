while i:=int(input()):
    while i//10:
        i=sum(map(int,str(i)))
    print(i)