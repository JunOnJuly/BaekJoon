import sys


def solution(str_data, target_str):
    # 스택
    stack = []
    # 스택에 한 글자씩 입력
    for string in str_data:
        stack.append(string)
        # 입력된 글자가 타깃 문자열의 마지막 글자이고 길이가 충분하면
        if len(stack) >= len(target_str) and string == target_str[-1]:
            # 마지막 문자열이 타깃 문자열인지 판단
            if ''.join(stack[-len(target_str):]) == target_str:
                # 스택에서 팝
                for _ in range(len(target_str)):
                    stack.pop()
    # 남은 문자가 없으면
    if not stack:
        return "FRULA"
    # 있으면
    else:
        return ''.join(stack)
    

str_data = sys.stdin.readline().strip()
target_str = sys.stdin.readline().strip()
print(solution(str_data, target_str))