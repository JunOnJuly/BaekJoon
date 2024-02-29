#include <iostream>
#include <array>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int dijkstra(array<vector<array<int, 2>>, 801> tree, int N, int start, int end)
{
	int max_dist = 200000 * 1000 + 1;
	
	deque<array<int, 2>> hq{ {0, start} };
	make_heap(hq.begin(), hq.end());
	
	array<int, 801> dist_arr;
	dist_arr.fill(max_dist);
	dist_arr[start] = 0;

	while (!hq.empty())
	{
		pop_heap(hq.begin(), hq.end());

		int now_dist = -hq.back()[0];
		int now_node = hq.back()[1];

		hq.pop_back();

		if (now_dist > dist_arr[now_node]) continue;

		for (auto node : tree[now_node])
		{
			int dist = node[1];
			int next_node = node[0];
			int next_dist = now_dist + dist;

			if (next_dist < dist_arr[next_node])
			{
				hq.push_back({ -next_dist, next_node });
				push_heap(hq.begin(), hq.end());

				dist_arr[next_node] = next_dist;
			}
		}
	}

	return dist_arr[end];
}

int main(void)
{
	int max_dist = 200000 * 1000 + 1;

	int N, E;
	cin >> N >> E;

	array<vector<array<int, 2>>, 801> tree;
	for (int i = 0; i < E; i++)
	{
		int a, b, c;
		cin >> a >> b >> c;

		tree[a].push_back({ b, c });
		tree[b].push_back({ a, c });	
	}

	int V1, V2;
	cin >> V1 >> V2;

	int dist_1 = dijkstra(tree, N, 1, V1) + dijkstra(tree, N, V1, V2) + dijkstra(tree, N, V2, N);
	int dist_2 = dijkstra(tree, N, 1, V2) + dijkstra(tree, N, V2, V1) + dijkstra(tree, N, V1, N);

	if (dist_1 >= max_dist and dist_2 >= max_dist) cout << -1;
	else if (dist_1 > dist_2) cout << dist_2;
	else cout << dist_1;
}