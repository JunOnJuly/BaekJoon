import sys

input = sys.stdin.readline


def solution(string: str):
    result = ''
    for idx in range(len(string)):
        if string[idx].isupper():
            result += string[idx].lower()
        else:
            result += string[idx].upper()
    
    return result


# 입력
string = input().strip()
print(solution(string))