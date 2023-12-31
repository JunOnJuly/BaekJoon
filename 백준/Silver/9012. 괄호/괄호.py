import sys
input = sys.stdin.readline


def solution(string):
    # 스택 사용
    stack = []
    # string 순회
    for char in string:
        # ( 이면 삽입
        if char == '(':
            stack.append('(')
        # ) 이면
        else:
            # 스택이 비거나 스택의 마지막이 ) 이면 'NO'
            if not stack or stack.pop() == ')':
                return('NO')
    # 스택이 비어있으면 'YES'
    if not stack:
        return('YES')
    else:
        return('NO')


T = int(input())
for _ in range(T):
    string = input().strip()
    print(solution(string))