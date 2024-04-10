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
	array<int, 2> min_dist = { numeric_limits<int>::max(), numeric_limits<int>::max() };
	// 최단거리로 오는 직전 노드, 남은 횟수 = 행
	array<int, 2> front_node = { 0, 0 };
};

// 오름차순 정렬
bool sort_dijk(array<int, 3>& arr_1, array<int, 3>& arr_2) {
	return arr_1[0] > arr_2[0];
}

// 다익스트라
void dijkstra(array<Node, 5001>& graph, int& s, int& t) {
	// 첫 노드 최단거리
	graph[s].min_dist = { 0, 0 };
	// 큐 / 현재까지 거리, 현재 노드, 남은 노드를 뺄 수 있는 횟수
	deque<array<int, 3>> hq = { {0, s, 1} };
	// 순회
	while (!hq.empty()) {
		// 팝 준비
		pop_heap(hq.begin(), hq.end(), sort_dijk);
		// 현재 거리, 현재 노드 번호, 잔여 횟수
		int now_dist = hq.back()[0];
		int now_num = hq.back()[1];
		int now_cnt = hq.back()[2];
		// 현재 노드
		Node now_node = graph[now_num];
		// 팝
		hq.pop_back();
		// 현재 거리가 현재 노드까지 최단거리보다 길면 패스
		if (now_dist > now_node.min_dist[now_cnt]) continue;
		// 연결된 노드 순회
		for (auto node : now_node.nodes) {
			// 다음 노드 번호, 다음 노드까지 거리
			int next_num = node[0];
			int dist = node[1];
			// 다음 노드까지의 총 거리
			int next_dist = now_dist + dist;
			// 다음 노드까지의 총 거리가 다음 노드까지 최단거리보다 짧으면
			if (next_dist < graph[next_num].min_dist[now_cnt]) {
				// 다음 노드가 목적 노드가 아니면
				if (next_num != t) {
					// 큐에 추가
					hq.push_back({ next_dist, next_num, now_cnt });
				}
				// 최단거리 최신화
				graph[next_num].min_dist[now_cnt] = next_dist;
				// 최단 노드 최신화
				graph[next_num].front_node[now_cnt] = now_num;
			}
			// 잔여 횟수가 남아있고 뺀 총 거리가 다음노드까지 최단거리보다 짧으면
			if (now_cnt > 0 and now_dist < graph[next_num].min_dist[now_cnt - 1]) {
				// 다음 노드가 목적 노드가 아니면
				if (next_num != t) {
					// 큐에 추가
					hq.push_back({ now_dist, next_num, now_cnt - 1 });
				}
				// 최단거리 최신화
				graph[next_num].min_dist[now_cnt - 1] = now_dist;
				// 최단 노드 최신화
				graph[next_num].front_node[now_cnt - 1] = now_num;
			}
		}
	}
}

int main(void) {
	// 입력
	int n, m;
	cin >> n >> m;
	// 그래프
	array<Node, 5001> graph;
	// 간선들의 가중치 합
	int sum_weights = 0;
	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;

		sum_weights += c;

		graph[a].nodes.push_back({ b, c });
		graph[b].nodes.push_back({ a, c });
	}
	int s, t;
	cin >> s >> t;

	// 다익스트라
	dijkstra(graph, s, t);

	cout << sum_weights - graph[t].min_dist[0];
}