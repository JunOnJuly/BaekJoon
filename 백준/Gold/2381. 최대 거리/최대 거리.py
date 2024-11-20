import sys

input = sys.stdin.readline


def solution(N, idxs):
    # |a-c| + |b-d| = 
    # (a+b) - (c+d) (a>=c and b>=d)
    # (c+d) - (a+b) (a<c and b<d)
    # (a-b) - (c-d) (a>=c and b<d)
    # (c-d) - (a-b) (a<c and b>=d)
    # (a+b) (c+d) (a-b) (c-d) 로 이루어져 있음
    # 즉 모든 인덱스의 (x+y) (x-y) 의 최소 / 최댓값을 구해놓으면 빠르게 각 계산값의 최소 / 최댓값을 구할 수 있음
    sums = list(sorted([x+y for x, y in idxs]))
    subs = list(sorted([x-y for x, y in idxs]))

    print(max(sums[-1]-sums[0], subs[-1]-subs[0]))


# 입력
N = int(input().strip())
idxs = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, idxs)