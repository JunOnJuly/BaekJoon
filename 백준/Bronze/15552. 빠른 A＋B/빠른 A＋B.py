import sys
input=sys.stdin.readline
for i in range(int(input().strip())):
    print(sum(map(int,input().strip().split())))