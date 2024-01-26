def solution(N, data_list):
    # 좋은 단어 수
    cnt = 0
    # 데이터 순회
    for data in data_list:
        # 스택
        stack = []
        # 문장 순회
        for string in data:
            # 스택의 마지막과 같으면 패스
            if stack and string == stack[-1]:
                # 스택 팝
                stack.pop()
            # 다르면 스택에 추가
            else:
                stack.append(string)
        if not stack:
            cnt += 1
    print(cnt)


N = int(input())
data_list = [list(input()) for _ in range(N)]
solution(N, data_list)