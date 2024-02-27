#include <iostream>
#include <array>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	array<int, 100001> sum_arr;

	for (int i = 0; i < N; i++)
	{
		int temp_num;
		cin >> temp_num;
		sum_arr[i + 1] = temp_num;
	}

	for (int i = 0; i < N; i++)
	{
		sum_arr[i+1] += sum_arr[i];
	}

	for (int i = 0; i < M; i++)
	{
		int temp_i, temp_j;
		cin >> temp_i >> temp_j;

		cout << sum_arr[temp_j] - sum_arr[temp_i - 1] << "\n";
	}
}