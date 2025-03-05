n,k=map(int,input().split())
m=list(map(int,input().split(',')))
while k:
    m=[m[i+1]-m[i] for i in range(len(m)-1)]
    k-=1
print(','.join(map(str,m)))