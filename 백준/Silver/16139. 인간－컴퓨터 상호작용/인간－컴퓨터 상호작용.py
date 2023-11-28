S = list(input())
q = int(input())

for _ in range(q):
    a, l, r = input().split()
    l, r = map(int, [l, r])

    answer = 0
    for i in range(l, r + 1):
        if S[i] == a:
            answer += 1
    print(answer)
