import sys

input = sys.stdin.readline


## Union-Find
# Union
def Union(node1, node2, group_list):
    # 각 노드의 그룹
    group1 = Find(node1, group_list)
    group2 = Find(node2, group_list)
    # 두 그룹이 같으면
    if group1 == group2:
        # 병합하지 않음
        return False, group_list
    
    # 두 그룹이 다르면
    # 타겟 쪽으로 병합
    group_list[group1] = group2
    
    return True, group_list


# Find
def Find(node, group_list):
    # 그룹의 대표가 자신이 아니면
    if group_list[node] != node:
        # 재귀적으로 업데이트
        group_list[node] = Find(group_list[node], group_list)
    
    return group_list[node]


def solution(R, C, nums):
    # 이동 방향
    move_dirs = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
    # 그래프 / graph[i][j] = [i, j] 에서 이동할 위치
    graph = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            # 가장 작은 인덱스
            min_idx = []
            # 가장 작은 값
            min_num = nums[i][j]
            # 이동 방향 순회
            for x, y in move_dirs:
                # 타겟 위치
                ii = i+x
                jj = j+y
                # 인덱스 범위 내부면
                if (ii >= 0 and ii < R) and (jj >= 0 and jj < C):
                    # 가장 작은 값 / 인덱스 갱신
                    if nums[ii][jj] < min_num:
                        min_num = nums[ii][jj]
                        min_idx = [ii, jj]
            
            # 그래프 갱신
            graph[i][j] = min_idx
    
    # 그룹 리스트 
    group_list = list(range(R*C))
    # 그래프 따라서 병합
    for i in range(R):
        for j in range(C):
            # 타겟 인덱스
            # 존재하지 않으면 패스
            if not graph[i][j]:
                continue

            ti, tj = graph[i][j]
            state, group_list = Union(i*C + j, ti*C + tj, group_list)

    # 결과
    result = [[0 for _ in range(C)] for __ in range(R)]
    for g in group_list:
        # 그룹
        group = Find(g, group_list)
        # 인덱스
        i = group // C
        j = group % C
        # 결과 갱신
        result[i][j] += 1
    
    for r in result:
        print(*r)


# 입력
R, C = map(int, input().strip().split())
nums = [list(map(int, input().strip().split())) for _ in range(R)]

solution(R, C, nums)