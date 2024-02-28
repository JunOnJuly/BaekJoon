#include <iostream>
#include <array>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

array<int, 20001> dijkstra(array<vector<array<int, 2>>, 20001> tree, int K, int V)
{
	const int max_num = 3000001;

	array<int, 20001> dist_arr;
	dist_arr.fill(max_num);
	dist_arr[K] = 0;

	deque<array<int, 2>> dq{ {0, K} };
	make_heap(dq.begin(), dq.end());

	while (!dq.empty())
	{
		int now_dist = -dq.front()[0];
		int now_node = dq.front()[1];

		dq.pop_front();

		if (now_dist > dist_arr[now_node]) continue;

		for (auto data : tree[now_node])
		{
			int next_node = data[0];
			int next_dist = data[1];

			if (now_dist + next_dist < dist_arr[next_node])
			{
				dq.push_back({ -(now_dist + next_dist), next_node });
				push_heap(dq.begin(), dq.end());
				dist_arr[next_node] = now_dist + next_dist;
			}
		}
	}

	return dist_arr;
}

int main(void)
{
	int V, E, K;
	cin >> V >> E >> K;

	array<vector<array<int, 2>>, 20001> tree;

	for (int i = 0; i < E; i++)
	{
		int u, v, w;
		cin >> u >> v >> w;

		tree[u].push_back({ v, w });
	}

	array<int, 20001> dist_arr = dijkstra(tree, K, V);
	for (int i = 0; i < V; i++)
	{
		if (dist_arr[i + 1] == 3000001) cout << "INF" << "\n";
		else cout << dist_arr[i + 1] << "\n";
	}
}