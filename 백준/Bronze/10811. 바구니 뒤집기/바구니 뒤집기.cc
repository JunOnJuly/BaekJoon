#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int N, M;
	cin >> N >> M;
	
	vector<int> data_vec;
	for (int i = 0; i < N; i++)
	{
		data_vec.push_back(i + 1);
	}

	for (int cnt = 0; cnt < M; cnt++)
	{
		int i, j;
		cin >> i >> j;
		reverse(data_vec.begin() + i - 1, data_vec.begin() + j);
	}

	for (int cnt = 0; cnt < N; cnt++)
	{
		cout << data_vec[cnt] << " ";
	}
}