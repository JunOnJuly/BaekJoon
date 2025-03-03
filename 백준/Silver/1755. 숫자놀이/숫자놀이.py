d=['zero','one','two','three','four','five','six','seven','eight','nine']
m,n=map(int,input().split())
w=[''.join([str(d.index(l)) for l in k.split()]) for k in sorted([' '.join([d[int(j)] for j in str(i)]) for i in list(range(m,n+1))])]
for i in range(0,len(w),10):
    print(*w[i:i+10])