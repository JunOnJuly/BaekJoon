import sys

input = sys.stdin.readline


# 세그먼트 트리
class SegTree:
    def __init__(self, nums):
        # 정수 리스트
        self.nums = nums
        # 세그먼트 트리
        self.segtree = [[] for _ in range(len(nums)*4)]
        self.partision_segtree(1, 0, len(nums)-1)


    # 세그먼트 트리 생성
    def partision_segtree(self, idx, left, right):
        # 절반
        half = (left+right) // 2
        # 범위가 1 이면 쪼개지 않고 갱신
        if left == right:
            self.segtree[idx] = [self.nums[left], self.nums[left]]
        
        else:
            # 둘로 쪼개기
            min_l, max_l = self.partision_segtree(idx*2, left, half)
            min_r, max_r = self.partision_segtree(idx*2 + 1, half+1, right)
            # 트리 갱신
            self.segtree[idx] = [min(min_l, min_r), max(max_l, max_r)]

        return self.segtree[idx]


    # 검색
    def search_minmax(self, idx, left, right, a, b):
        # 중간
        half = (left+right) // 2
        # 범위가 완벽히 일치하면
        if left == a and right == b:
            return self.segtree[idx]
        
        # 중간을 포함하지 않으면
        if b <= half:
            return self.search_minmax(idx*2, left, half, a, b)

        elif a > half:
            return self.search_minmax(idx*2 + 1, half+1, right, a, b)

        # 중간을 포함하면 쪼개기
        else:
            # 왼쪽 오른쪽의 최대 최솟값
            min_l, max_l = self.search_minmax(idx*2, left, half, a, half)
            min_r, max_r = self.search_minmax(idx*2 + 1, half+1, right, half+1, b)
        
            return [min(min_r, min_l), max(max_l, max_r)]


def solution(N, M, nums, querys):
    # 세그먼트 트리
    seg_tree = SegTree(nums)
    # 쿼리 순회
    for a, b in querys:
        print(*seg_tree.search_minmax(1, 0, N-1, a-1, b-1))


# 입력
N, M = map(int, input().strip().split())
nums = [int(input()) for _ in range(N)]
querys = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, nums, querys)