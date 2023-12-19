import sys


def solution(M):
    # 집합
    set_num = set()
    # M 번 입력 받음
    for _ in range(M):
        code_line = sys.stdin.readline().strip().split()
        # 명령어
        code = code_line[0]
        if len(code_line) > 1:
            # 수
            num = int(code_line[1])
        # 명령어 입력
        if code == 'add':
            set_num.add(num)
        elif code == 'remove':
            set_num.discard(num)
        elif code == 'check':
            if num in set_num:
                print(1)
            else:
                print(0)
        elif code == 'toggle':
            if num in set_num:
                set_num.discard(num)
            else:
                set_num.add(num)
        elif code == 'all':
            set_num = set(range(1, 21))
        else:
            set_num = set()


M = int(sys.stdin.readline())
solution(M)