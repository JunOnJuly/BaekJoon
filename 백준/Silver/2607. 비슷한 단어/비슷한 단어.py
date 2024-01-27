from collections import defaultdict, Counter


def solution(data_list):
    # 딕셔너리 리스트
    dict_list = [defaultdict(int, Counter(data)) for data in data_list]
    # 기준 딕셔너리
    main_dict = dict_list[0]
    # 비슷한 단어 카운트
    sim_count = 0
    # 딕셔서너리 리스트 순회
    for sub_dict in dict_list[1:]:
        # 글자 수가 2 이상 차이나면 패스
        if abs(sum([value for value in main_dict.values()]) - sum([value for value in sub_dict.values()])) >= 2:
            continue
        # 차이 리스트
        diff_list = [0 for _ in range(26)]
        # 각 알파벳에 대해 차이 구하기
        for asc in range(ord("A"), ord("Z")+1):
            # 차이 리스트 채우기
            diff_list[asc-ord("A")] = abs(main_dict[chr(asc)]-sub_dict[chr(asc)])
        # 문자 수가 모든 차이의 합이 2 이하이고 모든 차이가 1 이하면 비슷한 단어
        if sum(diff_list) <= 2 and all([num<=1 for num in diff_list]):
            sim_count += 1
    print(sim_count)


data_list = [input() for _ in range(int(input()))]
solution(data_list)