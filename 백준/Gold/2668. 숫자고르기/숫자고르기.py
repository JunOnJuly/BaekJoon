def solution(N, table):
    # 스택 리스트
    stack_list = []
    # 자신의 값을 가지면 미리 넣어두기
    for i in range(N+1):
        if table[i][0] == table[i][1]:
            stack_list.append(i)
    # 테이블 순회하며 DFS
    for idx in range(N):
        # 방문 명단
        memo = [0 if num in stack_list else 1 for num in range(N+1)]
        # 0일때는 스킵, stack_list 에 포함되면 스킵
        if idx and idx not in stack_list:
            # 스택
            stack = [idx]
            while True:
                # 다음 경로
                next_num = table[stack[-1]][1]
                # 방문하지 않은 경우
                if memo[next_num]:
                    # 다음 경로가 시작점일 때
                    if next_num == stack[0]:
                        # 스택 리스트에 삽입
                        stack_list.extend(stack)
                        break
                    # 아니면 그냥 경로에 추가
                    stack.append(next_num)
                    memo[next_num] = 0
                else:
                    break

    return len(stack_list), sorted(stack_list)


N = int(input())
table = [[i+1, int(input())] for i in range(N)]
table = [[0, -1]] + table
length, stack_list = solution(N, table)
print(length)
for num in stack_list:
    print(num)