from collections import Counter
c=Counter([input() for _ in range(int(input()))])
c=sorted(list(c.items()),key=lambda x:(-x[1],x[0]))
print(c[0][0])