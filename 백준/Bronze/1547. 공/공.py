p=1
for i in range(int(input())):
    a,b=map(int,input().split())
    if p==a:p=b
    elif p==b:p=a
print(p)