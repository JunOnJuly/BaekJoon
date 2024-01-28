def solution(a, b):
    # a, b 소인수분해
    a_set, b_set = set(split_num(a)), set(split_num(b))
    # 공통 약수
    com_div = a_set&b_set
    # 최대공약수
    print(max(com_div))
    # 최소공배수
    print(a*b//max(com_div))


# 약수를 구하는 함수
def split_num(num):
    # 수의 제곱근
    root_num = int(num**(1/2))
    # 약수
    split_num_list = []
    # 순회
    for idx in range(1, root_num+1):
        # 나누어떨어지면 약수 리스트에 추가
        if not num%idx:
            split_num_list.append(idx)
            split_num_list.append(num//idx)
    # 정렬
    split_num_list = sorted(split_num_list)
    return split_num_list


a, b = map(int, input().split())
solution(a, b)