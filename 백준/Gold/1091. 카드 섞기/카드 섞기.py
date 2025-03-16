N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

origin_P = P[:]
cnt = 0
while not all([P[p]==p%3 for p in range(len(P))]):
    next_P = P[:]
    for s, p in zip(S, P):
        next_P[s] = p
    
    P = next_P[:]
    if P == origin_P:
        cnt = -1
        break
    
    cnt += 1

print(-1 if cnt==N else cnt)