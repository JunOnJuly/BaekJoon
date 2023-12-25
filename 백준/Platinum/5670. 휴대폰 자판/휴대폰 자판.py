import sys


def solution(N, word_list):
    # 단어들의 버튼 클릭 횟수 총 합
    btn_cnt = 0
    # 트라이
    trie = Trie()
    # 단어 입력
    for word in word_list:
        # Trie 의 insert 메서드
        trie.insert(word)
    # 단어 버튼 클릿 횟수 카운팅
    for word in word_list:
        # Trie 의 count 메서드
        btn_cnt += trie.count(word)
    # 평균값 출력
    print(f'{round(btn_cnt/N, 2):.2f}')


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
    

    # 버튼 클릭 횟수 카운트 함수
    # 문제에 맞게 변형
    def count(self, string):
        # 버튼 클릿 횟수
        btn_cnt = 0
        # 현재 비교하는 문자 노드
        current_node = self.head
        # 순회
        for char in string:
            # 첫번째 문자는 추론하지 않음
            if not current_node.key:
                # 노드 이동
                current_node = current_node.children[char]
                # 버튼 클릭
                btn_cnt += 1
            # 두번째 문자부터
            else:
                # 자식의 수와 value의 수의 합이 1 이면
                if len(current_node.children) + bool(current_node.value) == 1:
                    # 노드 이동
                    current_node = current_node.children[char]
                # 자식이 하나가 아니면
                else:
                    # 노드 이동
                    current_node = current_node.children[char]
                    # 버튼 클릭
                    btn_cnt += 1
        return btn_cnt


    # starts_with 함수는 문제 해결에 필요없어서 구현하지 않았음
        

while True:
    try:
        N = int(sys.stdin.readline())
        word_list = [sys.stdin.readline().strip() for _ in range(N)]
        solution(N, word_list)
    except:
        break