import sys

input = sys.stdin.readline


def solution(X):
    print(bin(X)[2:].count('1'))


# 입력
X = int(input().strip())

solution(X)