def is_empty(x):
    for i in range(x):
        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == abs(x - i):
            return False
    return True


def n_queens(x):
    global cnt
    if x == n:
        cnt += 1
        return
    else:
        for i in range(n):
            queen[x] = i
            if is_empty(x):
                n_queens(x+1)
                
                
n = int(input())
cnt = 0
queen = [0] * n
n_queens(0)
print(cnt)