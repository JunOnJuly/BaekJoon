n=list(map(int,input().split()))
for i in range(1,8000001):
    if sum([1 for m in n if not i%m])>=3:
        print(i)
        break