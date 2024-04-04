#include <iostream>
#include <algorithm>
#include <vector>
#include <array>
#include <limits>
#include <map>
#include <set>
#include <deque>

using namespace std;

// 노드 정보
struct Node {
	// 연결된 노드, 거리
	vector<array<int, 2>> nodes;
	// 현재까지 최단 거리
	int min_dist = numeric_limits<int>::max();
	// 최단거리로 오는 직전 노드들
	vector<int> min_nodes;
};

// 오름차순 정렬 함수
bool sort_dijk(array<int, 2>& arr_1, array<int, 2>& arr_2) {
	return arr_1[0] > arr_2[1];
}

// 다익스트라
array<Node, 500> dijkstra(array<Node, 500> graph, int& S, int& D) {
	// 큐
	vector<array<int, 2>> hq = { { 0, S } };
	// 출발 노드 최단거리 설정
	graph[S].min_dist = 0;
	// 순회
	while (!hq.empty()) {
		// 팝 준비
		pop_heap(hq.begin(), hq.end(), sort_dijk);
		// 현재 거리, 현재 노드 번호
		int now_dist = hq.back()[0];
		int now_num = hq.back()[1];
		// 팝
		hq.pop_back();
		// 현재 노드
		Node now_node = graph[now_num];
		// 현재 거리가 현재 노드까지의 최단거리보다 길면 패스
		if (now_dist > now_node.min_dist) continue;
		// 연결된 노드 탐색
		for (auto arr : now_node.nodes) {
			// 다음 노드, 까지의 거리
			int next_num = arr[0];
			int dist = arr[1];
			// 다음 노드까지의 총 거리
			int next_dist = now_dist + dist;
			// 다음 노드
			Node next_node = graph[next_num];
			// 다음 노드까지의 총 거리가 다음 노드까지의 최단 거리보다 길면 패스
			if (next_dist > next_node.min_dist) continue;
			// 짧으면
			else if (next_dist < next_node.min_dist) {
				// 최단거리 갱신
				graph[next_num].min_dist = next_dist;
				// 최단 노드 벡터 갱신
				graph[next_num].min_nodes.clear();
				// 다음 노드가 목표 노드가 아니면
				if (next_num != D) {
					// 큐에 추가
					hq.push_back({ next_dist, next_num });
					push_heap(hq.begin(), hq.end(), sort_dijk);
				}
			}
			// 최단 노드 벡터 추가
			graph[next_num].min_nodes.push_back(now_num);
		}
	}
	return graph;
}

int main(void) {
	while (true) {
		// 입력
		int N, M;
		cin >> N >> M;

		if (N == 0 and M == 0) return 0;

		int S, D;
		cin >> S >> D;

		// 그래프
		array<Node, 500> graph;
		for (int i = 0; i < M; i++) {
			int U, V, P;
			cin >> U >> V >> P;

			graph[U].nodes.push_back({ V, P });
		}
		// 제거할 노드 업데이트를 위한 다익스트라
		array<Node, 500> pre_dijkstra = dijkstra(graph, S, D);

		/* 디버깅
		for (int i = 0; i < N; i++) {
			cout << "\nNode : " << i << "\n";

			cout << "noded : [ ";
			for (auto arr : pre_dijkstra[i].nodes) {
				cout << "{ " << arr[0] << " " << arr[1] << " } ";
			}
			cout << "]\n";

			cout << "min_dist : " << pre_dijkstra[i].min_dist << "\n";

			cout << "min_nodes : [ ";
			for (int num : pre_dijkstra[i].min_nodes) {
				cout << num << " ";
			}
			cout << "]\n";
		}
		*/

		// 방문 체크
		array<array<bool, 500>, 500> visited;
		for (int i = 0; i < 500; i++) visited[i].fill(true);
		// 데크
		deque<int> dq = { D };
		// 최단거리 순회하며 제거
		while (!dq.empty()) {
			// 현재 노드 번호
			int now_num = dq.front();
			// 팝
			dq.pop_front();
			// 최단 노드들 순회
			for (auto next_num : pre_dijkstra[now_num].min_nodes) {
				// 방문한적 없는 엣지면
				if (visited[next_num][now_num]) {
					// 데크에 추가
					dq.push_back(next_num);
					// 방문 기록
					visited[next_num][now_num] = false;
					// 그래프에서 노드 제거
					for (int i = 0; i < graph[next_num].nodes.size(); i++) {
						if (graph[next_num].nodes[i][0] == now_num){
							graph[next_num].nodes.erase(graph[next_num].nodes.begin() + i);
							break;
						}
					}
				}
			}
		}
		// 다익스트라
		array<Node, 500> result_dijkstra = dijkstra(graph, S, D);
		// 최단경로가 없으면
		if (result_dijkstra[D].min_dist == numeric_limits<int>::max()) cout << -1 << "\n";
		else cout << result_dijkstra[D].min_dist << "\n";
	}
}