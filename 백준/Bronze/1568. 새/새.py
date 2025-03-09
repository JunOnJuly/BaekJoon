n=int(input())
c=0
while n:
    i=1
    while n>=i:
        n-=i
        i+=1
        c+=1
print(c)