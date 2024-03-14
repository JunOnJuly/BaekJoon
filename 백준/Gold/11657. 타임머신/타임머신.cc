#include <iostream>
//
#include <array>
#include <vector>
//
#include <algorithm>

using namespace std;

// 벨만포드
array<long long, 501> bell_ford(vector<array<int, 3>> dist_vec, int N)
{
	// 시스템상 최댓값
	long long inf = 60000000;

	// 최솟값 거리 목록
	array<long long, 501> dists;
	dists.fill(inf);
	dists[1] = 0;

	// N 번 순회
	for (int i = 0; i < N; i++)
	{
		// dist_vec 데이터 순회
		for (auto data : dist_vec)
		{
			// 거쳐갈 노드
			int edge_node = data[0];
			// 목표 노드
			int next_node = data[1];
			// 이동 거리
			int move_cost = data[2];
			
			// 거쳐갈 노드가 도달할 수 있는 노드면
			if (dists[edge_node] != inf)
			{
				// 거쳐가는 거리가 최단 거리보다 짧으면
				if (dists[edge_node] + move_cost < dists[next_node])
				{
					// N-1 번째 순회에서도 최단거리가 최신화된다면 순환 존재
					if (i == N - 1) dists[0] = 0;
					// 최단거리 최신화
					dists[next_node] = dists[edge_node] + move_cost;
				}
			}
		}
	}

	return dists;
}

int main(void)
{
	int N, M;
	cin >> N >> M;

	// 시스템상 최댓값
	long long inf = 60000000;

	// 거리 데이터 목록
	vector<array<int, 3>> dist_vec;
	// 데이터 기록
	for (int i = 0; i < M; i++)
	{
		int A, B, C;
		cin >> A >> B >> C;

		dist_vec.push_back({ A, B, C });
	}

	// 벨만포드
	array<long long, 501> dists = bell_ford(dist_vec, N);
	
	if (dists[0] == 0)
	{
		cout << -1;
		return 0;
	}
	else
	{
		for (int i = 2; i < N + 1; i++)
		{
			if (dists[i] == inf) cout << -1 << "\n";
			else cout << dists[i] << "\n";
		}
		return 0;
	}
}	