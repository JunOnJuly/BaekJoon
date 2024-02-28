#include <iostream>
#include <vector>
#include <array>
#include <deque>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	array<vector<int>, 101> net_arr;

	for (int i = 0; i < M; i++)
	{
		int node_1, node_2;
		cin >> node_1 >> node_2;

		net_arr[node_1].push_back(node_2);
		net_arr[node_2].push_back(node_1);
	}

	array<int, 101> visited{ 1, 1 };
	deque<int> dq{ 1 };

	int num_infect = 0;
	while (!dq.empty())
	{
		int now_node = dq.front();
		dq.pop_front();

		for (int i = 0; i < net_arr[now_node].size(); i++)
		{
			int next_node = net_arr[now_node][i];

			if (visited[next_node] == 0)
			{
				dq.push_back(next_node);
				visited[next_node] = 1;
				num_infect++;
			}
		}
	}
	cout << num_infect;
}