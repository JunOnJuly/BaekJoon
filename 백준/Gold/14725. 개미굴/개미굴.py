def solution(N, data_list):
    # 트라이 자료구조
    trie = Trie()
    # 최상단 노드 리스트
    top_nodes = set()
    # 데이터 리스트 순회하며 데이터 삽입
    for data in data_list:
        # 최상단 노드 기록
        top_nodes.add(data[1])
        # 트라이 삽입 함수
        trie.insert(data[1:])
    # 트라이 탐색
    for node in sorted(list(top_nodes)):
        # starts_with 함수
        trie.starts_with([node])


# 트라이에 들어갈 노드 클래스
class Node(object):
    # 초기화
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        # 문제에서 DFS 쓸거라 추가
        self.visited = 1


# 트라이 자료구조 클래스
class Trie:
    # 초기화
    def __init__(self):
        # 최상위 노드는 빈 노드로 설정
        self.head = Node(None)
    

    # 삽입 함수, DFS 의 역과정이라고 생각하면 됨
    def insert(self, string_list):
        # head(최상위 노드) 먼저
        current_node = self.head
        # 문자열 리스트 순회
        for string in string_list:
            # 현재 노드의 자식(children) 에 해당 문자열이 없다면
            if string not in current_node.children:
                # 자식 노드 선언 및 추가
                # 아래에 하나의 문자열을 쌓아가는 과정
                current_node.children[string] = Node(string)
            # 다음 문자열에 해당하는 노드로 이동
            current_node = current_node.children[string]
        # 문자열 리스트 끝이라면 해당 문자열이 무슨 문자열인지 data 추가
        current_node.data = string_list
    

    # 검색 함수, DFS 와 비슷하다고 생각하면 됨
    def search(self, string_list):
        # head(최상위 노드) 먼저
        current_node = self.head
        # 문자열 리스트 순회
        for string in string_list:
            # 해당 문자열이 현재 노드의 자식중에 있으면
            if string in current_node.children:
                # 해당 노드로 이동
                current_node = current_node.children[string]
            # 없으면
            else:
                return False
        # 문자열 끝까지 탐색했고 문자열의 마지막 문자에 해당하는 노드에 데이터가 있으면
        if current_node.data:
            return True
        # 없으면
        else:
            return False
    

    # 임의의 문자열 리스트로 시작하는 문자열 리스트가 있는지 확인
    # 주어진 임의의 문자열 리스트 끝에서 DFS 의 방식으로 탐색
    # 원래 기본 값에서는 BFS 로 탐색, 문제에 맞춰서 변형
    def starts_with(self, string_list):
        # 데크
        from collections import deque

        # -----
        # # BFS 를 위한 큐
        # queue = deque([])
        # -----

        # DFS 를 위한 스택
        stack = []
        # 문자열을 저장할 리스트
        data_list = []
        # head(최상위 노드) 먼저
        current_node = self.head
        # 주어진 임의의 문자열 리스트 끝까지 이동
        for string in string_list:
            # 해당 문자열이 현재 노드의 자식중에 있으면
            if string in current_node.children:
                # 해당 노드로 이동
                current_node = current_node.children[string]
            # 없으면
            else:
                # 주어진 임의의 문자열 리스트로 시작하는 문자열 리스트 없음
                return None
        
        # -----
        # # 큐에 현재 노드 삽입
        # queue.append(current_node)
        # -----
        
        # 스택에 현재 노드 삽입
        stack.append([current_node, 1])
        # 주어진 임의의 문자열 리스트의 끝까지 왔으면 탐색 시작
        while True:
            # -----
            # # 큐가 비면 끝
            # if not queue:
            # -----
                
            # 스택이 비면 끝
            if not stack:
                return data_list
            
            # -----
            # 현재 노드
            #current_node = queue.popleft()
            # -----
            
            # 현재 노드, 노드 깊이
            current_node, node_depth = stack[-1]
            # 방문한 적 없으면 프린트
            if current_node.visited:
                print('-'*(node_depth-1)*2 + current_node.key)
            # 현재 노드 visited 체크
            current_node.visited = 0

            # -----
            # # 현재 노드에 데이터가 존재하면 문자열 리스트에 저장
            # if current_node.data:
            #     data_list.append(current_node.data)
            # -----

            # -----
            # # 현재 노드의 자식 노드들을 정렬해서 큐에 추가
            # queue.extend(current_node.children.values())
            # -----
            
            # 현재 노드의 자식 노드들이 존재하면 정렬해서 스택에 추가
            if current_node.children:
                for idx, node in enumerate(sorted(current_node.children.values(), key=lambda x: x.key)):
                    # 노드의 visited 가 체크가 안되어있다면
                    if node.visited:
                        # 노드의 visited 체크
                        stack.append([node, node_depth+1])
                        break
                    elif idx == len(current_node.children)-1:
                        stack.pop()
            # 없으면 팝
            else:
                stack.pop()


N = int(input())
data_list = [input().split() for _ in range(N)]
solution(N, data_list)