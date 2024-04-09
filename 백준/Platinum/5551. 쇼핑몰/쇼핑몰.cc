#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <limits>
#include <deque>
#include <cmath>

using namespace std;

// 그래프에 속할 노드
struct Node {
	// 연결된 노드 정보
	vector<array<int, 2>> nodes;
	// 현재 노드까지 최단 거리
	int min_dist = numeric_limits<int>::max();
};

// 오름차순 정렬
bool sort_dijk(array<int, 2>& arr_1, array<int, 2>& arr_2) {
	return arr_1[0] > arr_2[0];
}

// 다익스트라
void dijkstra(array<Node, 3001>& graph, int start) {
	// 큐
	deque<array<int, 2>> hq = { {0, start} };
	graph[start].min_dist = 0;
	// 쇼핑몰 (start) 까지 최대 거리
	float max_dist = 0;
	// 순회
	while (!hq.empty()) {
		// 팝 준비
		pop_heap(hq.begin(), hq.end(), sort_dijk);
		// 현재 노드 번호
		int now_num = hq.back()[1];
		// 현재 거리
		int now_dist = hq.back()[0];
		// 현재 노드
		Node now_node = graph[now_num];
		// 팝
		hq.pop_back();
		// 현재 거리가 현재 노드까지 최단거리보다 길면 패스
		if (now_dist > now_node.min_dist) continue;
		// 현재 노드와 연결된 노드 순회
		for (auto node : now_node.nodes) {
			// 다음 노드 번호
			int next_num = node[0];
			// 다음 노드까지 거리
			int dist = node[1];
			// 다음 노드까지 총 거리
			int next_dist = now_dist + dist;
			// 다음 노드까지 총 거리가 다음 노드까지 최단거리보다 짧으면
			if (next_dist < graph[next_num].min_dist) {
				// 큐에 추가
				hq.push_back({ next_dist, next_num });
				push_heap(hq.begin(), hq.end(), sort_dijk);
				// 최단거리 최신화
				graph[next_num].min_dist = next_dist;
			}
		}
	}
}

int main(void) {
	// 입력
	int N, M, K;
	cin >> N >> M >> K;
	// 그래프
	array<Node, 3001> graph;
	for (int i = 0; i < M; i++) {
		int a, b, l;
		cin >> a >> b >> l;
		graph[a].nodes.push_back({ b, l });
		graph[b].nodes.push_back({ a, l });
	}
	// 쇼핑몰마다 다익스트라
	for (int i = 0; i < K; i++) {
		int k;
		cin >> k;
		// 다익스트라
		dijkstra(graph, k);
	}
	float max_dist = 0;
	// 최단거리가 갱신된 노드들을 순회하며 최대거리 갱신
	for (int i = 1; i < graph.size(); i++) {
		for (auto node : graph[i].nodes) {
			// 연결된 두 노드까지의 각 최단 거리, 그 사이 거리
			max_dist = max(max_dist, (static_cast<float>(graph[i].min_dist) + static_cast<float>(graph[node[0]].min_dist) + static_cast<float>(node[1])) / 2);
		}
	}
	cout << round(max_dist);
}