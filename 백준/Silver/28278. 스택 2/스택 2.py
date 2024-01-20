import sys
input = sys.stdin.readline


N = int(input())
stack = []
for _ in range(N):
    query = list(map(int, input().split()))
    if query[0] == 1:
        stack.append(query[1])
    elif query[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif query[0] == 3:
        print(len(stack))
    elif query[0]== 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)