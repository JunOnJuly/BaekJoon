#include <iostream>
//
#include <array>
#include <vector>
//
#include <algorithm>

using namespace std;

// 각 노드의 루트를 저장
vector<int> root_vec;

// find
int find_func(int node) {
	// 자신의 루트가 자신이 아니면
	if (root_vec[node] != node){
		// 노드의 조상을 조상의 조상으로 변경하며 계속 탐색
		root_vec[node] = find_func(root_vec[node]);
	}
	return root_vec[node];
}

// union
void union_func(int node_1, int node_2) {
	// 각 노드의 조상
	int root_1 = find_func(node_1);
	int root_2 = find_func(node_2);
	
	// 두 노드의 조상이 다르면 하나의 조상으로 병합
	if (root_1 != root_2) {
		root_vec[root_1] = root_2;
	}

	return;
}

int main(void){
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n, m;
	cin >> n >> m;

	for (int i = 0; i < n+1; i++)
	{
		root_vec.push_back(i);
	}

	for (int i = 0; i < m; i++) {
		int q, a, b;
		cin >> q >> a >> b;

		if (q == 0)
		{
			union_func(a, b);
		}
		else {
			if (find_func(a) == find_func(b)) cout << "YES" << "\n";
			else cout << "NO" << "\n";
		}
	}
}	