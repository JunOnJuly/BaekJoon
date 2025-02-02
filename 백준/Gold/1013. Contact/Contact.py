import sys
import re

input = sys.stdin.readline


def solution(T, strings):
    # 정규 표현식 컴파일
    p = re.compile('(100+1+|01)+')
    for string in strings:
        if p.fullmatch(string):
            print('YES')
        
        else:
            print('NO')


# 입력
T = int(input().strip())
strings = [input().strip() for _ in range(T)]

solution(T, strings)