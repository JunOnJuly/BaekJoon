def solution(never_listen_list, never_look_list):
    # set 으로 변환
    never_listen_set = set(never_listen_list)
    never_look_set = set(never_look_list)
    # 교집합
    never_lisok_set = never_listen_set & never_look_set
    never_lisok_list = sorted(list(never_lisok_set))

    print(len(never_lisok_list))
    for never_lisok in never_lisok_list:
        print(never_lisok)


N, M = map(int, input().split())
never_listen_list = [input() for _ in range(N)]
never_look_list = [input() for _ in range(M)]
solution(never_listen_list, never_look_list)