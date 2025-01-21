d={chr(i):0 for i in range(ord('a'), ord('z')+1)}
for c in input():
    d[c]+=1
print(*d.values())