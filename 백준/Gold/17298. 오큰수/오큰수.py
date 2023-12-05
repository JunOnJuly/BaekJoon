import sys


def solution(N, data_list):
    # 스택
    stack = [0]
    # 데이터 순회
    while True:
        # 모든 데이터를 순회하면
        if stack[-1] == N-1:
            # 스택에 있는 인덱스는 모두 오큰수 -1
            for num in stack:
                data_list[num] = -1
            print(*data_list)
            return
        # 다음 수
        next_idx = stack[-1]+1
        next_num = data_list[next_idx]
        # 스택을 순회하며 더 크면 앞선 수들과 비교 후 오큰수 갱신
        while True:
            # 스택이 비거나 작거나 같으면
            if not stack or (data_list[stack[-1]] >= next_num):
                # 다음 인덱스 스택에 추가 후 종료
                stack.append(next_idx)
                break
            # 앞의 데이터들 비교 후 변경
            elif data_list[stack[-1]] < next_num:
                data_list[stack.pop()] = next_num


N = int(sys.stdin.readline().strip())
data_list = list(map(int, sys.stdin.readline().strip().split()))
solution(N, data_list)