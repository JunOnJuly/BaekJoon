def solution(T, P):
    # KMP 알고리즘
    KMP_table = KMP(P)
    # 카운트
    cnt = 0
    # 등장 위치
    idx_list = []
    # 순회
    # P 인덱스
    idx_P = 0
    # T 를 순회
    for idx_T in range(0, len(T)):
        # 같은 문자열이 나올 때 까지
        while idx_P > 0 and T[idx_T] != P[idx_P]:
            # P 인덱스 이동
            idx_P = KMP_table[idx_P-1]
        # 같은 문자열이 나왔으면
        if T[idx_T] == P[idx_P]:
            # 마지막까지 모두 같으면
            if idx_P == (len(P)-1):
                # 일치 리스트, 카운트 추가
                idx_list.append(idx_T - len(P) + 2)
                cnt += 1
                # P 인덱스 이동
                idx_P = KMP_table[idx_P]
            # 마지막이 아니면
            else:
                # P 인덱스 이동
                idx_P += 1
    print(cnt)
    print(*idx_list)


# KMP 알고리즘
def KMP(P):
    # KMP 테이블
    # 최대 경계 너비
    KMP_table = [0]*(len(P))
    # 최대 경계 너비
    max_lim = 0
    # 비교 인덱스
    # 비교 인덱스가 늘어나는 것은 비교하는 전체 길이가 늘어나는 효과도 있음
    comp = 1
    # 최대 경계 너비 최신화
    while True:
        # 비교 인덱스가 전체 길이를 벗어나면 끝
        if comp >= len(P):
            KMP_table[0] = 0
            # P 의 길이가 2 이상이면
            if len(P) >= 2:
                KMP_table[1] = 0
            return KMP_table
        # 이전까지 최대 경계 너비 인덱스에 걸쳐있는 문자와 비교
        # 같으면 경계 너비 + 1
        if P[comp] == P[max_lim]:
            max_lim += 1
            # 비교하는 인덱스의 최대 경계 너비 최신화
            KMP_table[comp] = max_lim
            # 비교 인덱스 + 1
            comp += 1
        # 다르면
        else:
            # 이전 인덱스까지는 같았으면
            if max_lim:
                # 이전 최대 경계 너비로 돌아가서 다시 검사
                # 간접적으로 비교 길이를 늘이는 효과
                max_lim = KMP_table[max_lim-1]
            # 이전 인덱스에서도 달랐으면
            else:
                # 일치하는 문자가 없는 것이므로 최신화
                KMP_table[comp] = 0
                # 다음 길이
                comp += 1

    
T = input()
P = input()
solution(T, P)