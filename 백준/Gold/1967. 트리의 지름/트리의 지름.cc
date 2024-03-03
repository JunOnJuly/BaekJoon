#include <iostream>
#include <deque>
#include <vector>
#include <array>
#include <algorithm>

using namespace std;

// 다익스트라
array<int, 2> dijkstra(array<vector<array<int, 2>>, 10001> tree, int start, int n)
{
	// 최소힙
	deque<array<int, 2>> hq{ {0, start} };
	
	// 시스템상 최대 길이
	int max_dist = 1000001;

	// 최단 거리 리스트 생성 및 최대거리로 채우기
	array<int, 10001> dist_arr;
	dist_arr.fill(max_dist);
	dist_arr[start] = 0;
	dist_arr[0] = 0;

	// 힙이 비면 끝
	while (!hq.empty())
	{
		// 현재 거리, 현재 노드
		int now_dist = hq.front()[0];
		int now_node = hq.front()[1];

		// 최소 요소 제거
		pop_heap(hq.begin(), hq.end());
		hq.pop_back();

		// 현재 최단 거리보다 지금까지의 거리가 길면 패스
		if (now_dist > dist_arr[now_node]) continue;

		// 자식 순회
		for (auto node : tree[now_node])
		{
			// 자식 노드, 이동 거리
			int next_node = node[0];
			int dist = node[1];

			// 다음 노드까지 누적 거리
			int next_dist = now_dist + dist;

			// 다음 노드까지의 거리가 기록된 최단 거리보다 짧을때만
			if (next_dist < dist_arr[next_node])
			{
				// 힙에 삽입
				hq.push_back({ next_dist , next_node });

				// 최단 거리 리스트 최신화
				dist_arr[next_node] = next_dist;
			}
		}
	}

	// 가장 먼 노드까지 거리와 노드 번호
	int max = *max_element(dist_arr.begin() + 1, dist_arr.begin() + n + 1);
	int max_idx = max_element(dist_arr.begin() + 1, dist_arr.begin() + n + 1) - dist_arr.begin();

	return {max, max_idx};
}

int main(void)
{
	int n;
	cin >> n;

	// 트리
	array<vector<array<int, 2>>, 10001> tree;
	for (int i = 0; i < n - 1; i++)
	{
		int p, c, l;
		cin >> p >> c >> l;

		// 양방향 탐색을 위해 자식 부모에게 모두 정보 입력
		tree[p].push_back({ c, l });
		tree[c].push_back({ p, l });
	}

	// 1에서 가장 먼 노드와 거리
	array<int, 2> dijkstra_1 = dijkstra(tree, 1, n);
	// 에서 가장 먼 노드와 거리
	array<int, 2> dijkstra_2 = dijkstra(tree, dijkstra_1[1], n);
	// 거리 합
	cout << dijkstra_2[0];

	return 0;
}