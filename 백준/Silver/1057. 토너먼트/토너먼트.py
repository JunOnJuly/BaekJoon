N, k, l = map(int, input().split())

cnt = 1
while True:
    k = k//2 + 1 if k%2 else k//2
    l = l//2 + 1 if l%2 else l//2
    
    if k == l:
        break
    
    cnt += 1
    
print(cnt)