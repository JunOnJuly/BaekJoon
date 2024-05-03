
#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
#include <cmath>
#include <deque>

using namespace std;

// 노드 구조체
struct Node {
	// 연결된 노드 번호
	vector<int> nodes;
	// 연결된 노드 거리
	vector<int> dists;
	// 방문 여부
	bool visited = true;
};

// BFS
int BFS(vector<Node> tree, int& A, int& B) {
	// 데크
	deque<array<int, 2>> dq = { { A, 0 } };
	// BFS
	while (!dq.empty()) {
		// 현재 노드
		int now_node = dq.front()[0];
		//현재 거리
		int now_dist = dq.front()[1];
		// 방문 체크
		tree[now_node].visited = false;
		// 팝
		dq.pop_front();
		// 연결된 노드 순회
		for (int j = 0; j < tree[now_node].dists.size(); j++) {
			// 다음 후보 노드
			int next_node = tree[now_node].nodes[j];
			// 다음 후보 노드에 방문한적 없으면
			if (tree[next_node].visited) {
				// 다음 후보 노드까지 거리
				int dist = tree[now_node].dists[j];
				// 다음 후보 노드까지 총 거리
				int next_dist = now_dist + dist;
				// 다음 후보 노드가 목표 노드면
				if (next_node == B) return next_dist;
				// 아니면
				dq.push_back({ next_node, next_dist });
			}
		}
	}
	return 0;
}

int main(void) {
	// 입력
	int N, M;
	cin >> N >> M;
	// 노드를 저장할 트리
	vector<Node> tree(N + 1);
	for (int i = 0; i < N - 1; i++) {
		int A, B, D;
		cin >> A >> B >> D;
		tree[A].nodes.push_back(B);
		tree[A].dists.push_back(D);

		tree[B].nodes.push_back(A);
		tree[B].dists.push_back(D);
	}
	for (int i = 0; i < M; i++) {
		// 거리를 계산할 두 노드
		int A, B;
		cin >> A >> B;
		// BFS
		cout << BFS(tree, A, B) << "\n";
	}
}