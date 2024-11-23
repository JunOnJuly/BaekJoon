import sys
from collections import deque

input = sys.stdin.readline


# segment tree
class SegTree:
    def __init__(self, nums):
        # 세그먼트 트리
        self.seg_tree = [0 for _ in range(len(nums*4))]
        # 범위, 인덱스를 저장할 데크
        dq = deque([[1, 0, len(nums)-1]])
        # 순회하며 세그먼트 트리에 추가
        while dq:
            # 인덱스 / 범위
            idx, left, right = dq.popleft()
            # 해당 범위의 합 추가
            self.seg_tree[idx] = sum(nums[left:right+1])
            # 길이가 1 이하면 다음 범위는 추가하지 않음
            if right - left < 1:
                continue
            # 중간
            half = (left + right) // 2
            # 다음 범위 추가
            dq.append([idx*2, left, half])
            dq.append([idx*2 + 1, half+1, right])


    # 원소를 교체
    def change(self, idx, num, nums, left, right, node):
        # 완전히 범위 밖이면
        if idx < left or idx > right:
            # 탐색하지 않음
            return
        
        # 범위안에 인덱스가 포함되면
        else:
            # 값 갱신
            self.seg_tree[node] += num - nums[idx]
            # 길이가 1 이하면 다음 범위는 추가하지 않음
            if right - left < 1:
                return
            
            # 중간
            half = (left + right) // 2
            # 다음 범위 진행
            self.change(idx, num, nums, left, half, node*2)
            self.change(idx, num, nums, half+1, right, node*2 + 1)


    # 구간합 계산
    def subsum(self, idx, s_left, s_right, left, right):
        # 완전히 범위를 벗어났으면
        if (s_left > right or s_right < s_left):
            # 계산하지 않음
            return 0
    
        # 완전히 범위가 일치하면
        elif s_left == left and s_right == right:
            # 값 리턴
            return self.seg_tree[idx]
        
        # 범위를 포함하면
        else:
            # 중간
            half = (left + right) // 2
            # 중간을 포함하면
            if half <= s_right and half >= s_left:
                # 분할해서 합
                return self.subsum(idx*2, s_left, half, left, half) + \
                        self.subsum(idx*2 + 1, half+1, s_right, half+1, right)
            
            # 중간을 포함하지 않으면
            else:
                # 작으면
                if s_right < half:
                    # 작은 범위로 분할
                    return self.subsum(idx*2, s_left, s_right, left, half)

                # 크면
                else:
                    # 작은 범위로 분할
                    return self.subsum(idx*2 + 1, s_left, s_right, half+1, right)


def solution(N, M, K, nums, querys):
    # 세그먼트 트리
    seg_tree = SegTree(nums)
    # 쿼리 순회
    for a, b, c in querys:
        # 수 변경
        if a == 1:
            seg_tree.change(b-1, c, nums, 0, len(nums)-1, 1)
            nums[b-1] = c
        
        # 합 츌력
        else:
            print(seg_tree.subsum(1, b-1, c-1, 0, len(nums)-1))


# 입력
N, M, K = map(int, input().strip().split())
nums = [int(input().strip()) for _ in range(N)]
querys = [list(map(int, input().strip().split())) for _ in range(M+K)]

solution(N, M, K, nums, querys)