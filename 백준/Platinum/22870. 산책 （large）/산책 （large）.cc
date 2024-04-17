#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>
#include <deque>

using namespace std;

// 노드 정보를 기록할 구조체
struct Node {
	// 이동 가능한 노드, 거리
	vector<array<int, 2>> nodes;
	// 현재 노드까지 최단 거리
	int min_dist = numeric_limits<int>::max();
	// 현재 노드까지 최단 거리로 도달할 때 직전 노드들
	int front_node;
};

// 오름차순 정렬 함수
bool sort_dijk(array<int, 2>& arr_1, array<int, 2>& arr_2) {
	return arr_1[0] > arr_2[0];
}

// 다익스트라
array<Node, 200001> dijkstra(array<Node, 200001> graph, int& S, int& E, const vector<int>& remove_nodes = {}) {
	// 시작 노드 정리
	graph[S].min_dist = 0;
	graph[S].front_node = 0;
	// 큐
	deque<array<int, 2>> hq = { {0, S} };
	// 순회
	while (!hq.empty()) {
		// 팝 준비
		pop_heap(hq.begin(), hq.end(), sort_dijk);
		// 현재 거리, 현재 노드 번호
		int now_dist = hq.back()[0];
		int now_num = hq.back()[1];
		// 현재 노드
		Node now_node = graph[now_num];
		// 팝
		hq.pop_back();
		// 현재 거리가 현재 노드까지의 최단거리보다 길면 패스
		if (now_dist > now_node.min_dist) continue;
		// 이동 가능 노드 순회
		for (auto node : now_node.nodes) {
			// 다음 노드 번호, 다음 노드까지 거리
			int next_num = node[0];
			int dist = node[1];
			// 다음 노드가 삭제된 노드에 포함되면 패스
			if (find(remove_nodes.begin(), remove_nodes.end(), next_num) != remove_nodes.end()) continue;
			// 다음 노드까지 총 거리
			int next_dist = now_dist + dist;
			// 다음 노드까지 거리가 다음 노드까지의 최단거리보다 짧으면
			if (next_dist < graph[next_num].min_dist) {
				// 다음 노드가 목적 노드가 아니면
				if (next_num != E) {
					// 큐에 추가
					hq.push_back({ next_dist, next_num });
				}
				// 최단거리 최신화
				graph[next_num].min_dist = next_dist;
				// 최단거리 직전노드 최신화
				graph[next_num].front_node = now_num;
			}
			// 다음 노드까지 거리가 다음 노드까지의 최단거리와 같으면
			else if (next_dist == graph[next_num].min_dist) {
				// 최단거리 직전노드 추가
				graph[next_num].front_node = min(now_num, graph[next_num].front_node);
			}
		}
	}
	return graph;
}

int main(void){
	// 입력
	int N, M;
	cin >> N >> M;
	// 노드 정보를 저장할 그래프
	array<Node, 200001> graph;
	for (int i = 0; i < M; i++) {
		int A, B, C;
		cin >> A >> B >> C;
		graph[A].nodes.push_back({ B, C });
		graph[B].nodes.push_back({ A, C });
	}
	int S, E;
	cin >> S >> E;
	// S -> E 다익스트라
	// S -> E 의 거리를 계산해야 하지만 우선 양방향 간선이므로 거리 차이는 없음
	// 사전순으로 가장 먼저 오는 것을 선택해야 하지만 S -> E 다익스트라를 사용하면
	// 현재 노드에서 보기에 사전적으로 가장 작은 노드가 아닌
	// 다음 노드에서 보기에 사전적으로 가장 작은 노드가 최단 거리에 기록됨
	// -> 현재 노드에서 최단거리를 기준으로 큰 노드에 접근하면 큰 노드에서는 현재 노드를 먼저 기록하기 때문
	// 때문에 E -> S 로 다익스트라를 사용하면 순서가 반전되기 때문에 S -> E 기준으로 현재 노드에서 보기에 사전적으로 가장 작은 노드가 기록됨
	array<Node, 200001> STOE = dijkstra(graph, E, S);
	// S -> E 거리
	int STOE_dist = STOE[S].min_dist;
	// 최단거리 탐색 및 삭제할 노드 기록
	// 삭제할 노드
	vector<int> remove_nodes;
	// 탐색 시작 노드
	int now_node = S;
	while (true) {
		// 다음 노드
		int next_node = STOE[now_node].front_node;
		// 다음 노드가 끝 노드면 끝
		if (next_node == E) break;
		// 삭제 노드 기록
		remove_nodes.push_back(next_node);
		// 다음 탐색 시작 노드
		now_node = next_node;
	}
	// E -> S 거리
	array<Node, 200001> ETOS = dijkstra(graph, E, S, remove_nodes);
	int ETOS_dist = ETOS[S].min_dist;

	cout << STOE_dist + ETOS_dist;
}