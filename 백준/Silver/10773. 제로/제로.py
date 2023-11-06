def solution(K, data_list):
    # 스택
    stack = []
    # 0이 아니면 넣고
    # 0이면 pop
    for num in data_list:
        if num:
            stack.append(num)
        else:
            stack.pop()

    return sum(stack)


K = int(input())
data_list = [int(input()) for _ in range(K)]
print(solution(K, data_list))