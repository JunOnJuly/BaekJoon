#include <iostream>
#include <array>

using namespace std;


int main(void)
{
	int N, M;
	cin >> N >> M;
	
	array<int, 100> ball_arr = {};

	for (int num = 0; num < M; num++)
	{
		int i, j, k;
		cin >> i >> j >> k;

		for (int idx = i-1; idx < j; idx++)
		{
			ball_arr[idx] = k;
		}
	}

	for (int num = 0; num < N; num++)
	{
		cout << ball_arr[num] << " ";
	}
}