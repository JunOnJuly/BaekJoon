import sys

input = sys.stdin.readline


# 이분매칭
def bimatch(idx, connectable, connected, visited):
    # 이미 방문했으면 패스
    if visited[idx]:
        return False
    
    # 방문 체크
    visited[idx] = True
    # 순회
    for node in connectable[idx]:
        # 매칭할 수 있거나 다른 노드와 매칭시킬 수 있으면
        if connected[node] < 0 or bimatch(connected[node], connectable, connected, visited):
            # 매칭
            connected[node] = idx
            return True
    
    return False


def solution(W, H, board, wish_board):
    # 구슬이 있지만 구슬이 없으면 좋겠는 리스트
    tf_list = []
    # 구슬이 없지만 구슬이 있으면 좋겠는 리스트
    ft_list = []
    # 순회하며 리스트 채우기
    for h in range(H):
        for w in range(W):
            # 구슬이 있지만 없으면 좋겠다면
            if board[h][w] and not wish_board[h][w]:
                tf_list.append([h, w])
            # 구슬이 없지만 있으면 좋겠다면
            elif not board[h][w] and wish_board[h][w]:
                ft_list.append([h, w])
    
    # ft 와 tf 가 다르면 불가능
    if len(ft_list) != len(tf_list):
        print(-1)
        return
    
    # 인접해 있어서 한번에 옮길 수 있는 목록
    # tf -> ft
    connectable = [[] for _ in range(len(tf_list))]
    for t in range(len(tf_list)):
        # 인덱스
        th, tw = tf_list[t]
        for f in range(len(ft_list)):
            # 인덱스
            fh, fw = ft_list[f]
            # 인접해있으면
            if (abs(th-fh)==1 and tw==fw) or (th==fh and abs(tw-fw)==1):
                connectable[t].append(f)

    # 연결된 리스트
    connected = [-1 for _ in range(len(ft_list))]
    # 순회
    for idx in range(len(ft_list)):
        # 방문 목록
        visited = [False for _ in range(len(ft_list))]
        # 이분매칭
        bimatch(idx, connectable, connected, visited)

    # 매칭된 수
    matched = sum([1 for c in connected if c >= 0])
    # 남은 ft, tf 수
    left_ft = len(ft_list) - matched
    left_tf = len(tf_list) - matched
    # 남은 ft 를 모두 들고 남은 tf 의 수만큼 내려놓고
    print(matched + left_ft + left_tf)


# 입력
W, H = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(H)]
wish_board = [list(map(int, input().strip().split())) for _ in range(H)]

solution(W, H, board, wish_board)