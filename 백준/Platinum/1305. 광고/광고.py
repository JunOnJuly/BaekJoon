def solution(L, data):
    # KMP 의 실패함수만 사용
    # 앞과 뒤의 가장 긴 일치 문자열을 찾음
    # 일치하는 문자 수 리스트
    # KMP_table[i] = 앞에서부터 i 까지의 문자열의 맨 앞과 맨 뒤의 겹치는 문자 수
    KMP_table = [0 for _ in range(len(data))]
    # S 인덱스
    S_idx = 0
    # 데이터순회
    for data_idx in range(1, len(data)):
        # 같은 문자가 나올때 까지 혹은 같은 문자가 하나도 없을 때 까지
        while S_idx > 0 and data[data_idx] != data[S_idx]:
            # 디버그
            # debug(KMP_table, data, S_idx, data_idx)
            # 안겹치면 이전에 겹치던 문자로 이동해서 비교하려고 인덱스 이동
            S_idx = KMP_table[S_idx-1]
        # 같은 문자가 나오면
        if data[data_idx] == data[S_idx]:
            # 디버그
            # debug(KMP_table, data, S_idx, data_idx)
            # 다음 문자 비교하기 위해 인덱스 이동
            S_idx += 1
            # 겹치는 문자가 연속으로 나왔으므로 테이블 최신화
            KMP_table[data_idx] = S_idx
    # 가장 짧은 광고는 지금 보이는 문자열에서 앞과 뒤의 겹치는 문자를 뺀 것
    print(len(data) - KMP_table[len(data)-1])


def debug(KMP_table, data, S_idx, data_idx):
    print('------------------------------------')
    print(f'KMP_table : {KMP_table}')
    print('------------------------------------')
    print(' '*S_idx + 'S')
    print(' '*S_idx + 'v')
    print(data)
    print(' '*data_idx + '^')
    print(' '*data_idx + 'D')


L = int(input())
data = input()
solution(L, data)