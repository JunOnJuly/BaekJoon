from collections import defaultdict


def solution(N, data_list):
    # enter 횟수
    enter = 0
    # 채팅 기록 dict
    chat_log_dict = defaultdict(int)
    # 임시 기록
    temp_count_set = set()
    # 채팅 기록을 순회하며 카운트
    for idx, data in enumerate(data_list):
        # enter 을 기점으로 기록 카운트 후 기록을 초기화
        if data == 'ENTER': 
            for name in list(temp_count_set):
                chat_log_dict[name] += 1
            temp_count_set = set()
        # 일반적인 경우 그냥 데이터 추가
        else:
            temp_count_set.add(data)
    # 순회가 끝나면 기록 카운트
    for name in list(temp_count_set):
        chat_log_dict[name] += 1


    return sum(chat_log_dict.values())


N = int(input())
data_list = [input() for _ in range(N)]
print(solution(N, data_list))