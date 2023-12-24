def solution(N, M, S, data_list):
    # 트라이
    trie = Trie()
    # 데이터 입력
    for string in S:
        # 트라이 insert 함수
        trie.insert(string)
    # 집합에 포함되는 데이터 수
    data_count = 0
    # 데이터 검색
    for data in data_list:
        # 트라이 search 함수
        if trie.search(data):
            # 카운트 + 1
            data_count += 1
    print(data_count)
    return


# 트라이에 들어갈 노드 클래스
class Node:
    # 초기화
    def __init__(self, key, value=None):
        # children 의 key-value 쌍에서의 key
        self.key = key
        # children 의 key-value 쌍에서의 value
        self.value = value
        # children
        self.children = {}


# 트라이 자료구조
class Trie:
    # 초기화
    def __init__(self):
        # 최상단 노드
        self.head = Node(None)
    

    # 입력 함수
    def insert(self, string):
        # 현재 비교하는 문자 노드
        current_node = self.head
        # 순회
        for char in string:
            # char 이 현재 노드의 자식에 속해잇지 않으면 삽입
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            # 노드 이동
            current_node = current_node.children[char]
        # 문자열을 모두 순회했으면 끝에 value 추가
        current_node.value = string
    

    # 검색 함수
    def search(self, string):
        # 현재 비교하는 문자 노드
        current_node = self.head
        # 순회
        for char in string:
            # char 이 현재 노드의 자식에 속해있지 않으면 해당 문자열은 없는 것
            if char not in current_node.children:
                return False
            # char 이 현재 노드의 자식에 속해있으면 다음 노드로 이동
            else:
                current_node = current_node.children[char]
        # 순회를 마쳤을 때 현재 노드에 value 가 존재하면 해당 문자열이 존재
        if current_node.value:
            return True
        # 순회를 마쳤을 때 현재 노드에 value 가 존재하지 않으면 해당 문자열이 존재하지 않음
        else:
            return False
    

    # starts_with 함수는 문제 해결에 필요없어서 구현하지 않았음
        

N, M = map(int, input().split())
S = [input() for _ in range(N)]
data_list = [input() for _ in range(M)]
solution(N, M, S, data_list)