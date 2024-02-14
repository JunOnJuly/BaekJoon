#include <iostream>
#include <sstream>

#include <vector>
#include <array>
#include <string>

using namespace std;

int main(void)
{
	int M, N;
	cin >> M >> N;

	array<array<int, 100>, 100> A = {};
	for (int i = 0; i < N; i++)
	{
		array<int, 100> temp_arr = {};
		for (int j = 0; j < M; j++)
		{
			cin >> temp_arr[j];
		}

		A[i] = temp_arr;
	}

	array<array<int, 100>, 100> B = {};
	for (int i = 0; i < N; i++)
	{
		array<int, 100> temp_arr = {};
		for (int j = 0; j < M; j++)
		{
			cin >> temp_arr[j];
		}

		B[i] = temp_arr;
	}
	
	array<array<int, 100>, 100> C = {};
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			C[i][j] = A[i][j] + B[i][j];
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (j < M - 1)
			{
				cout << C[i][j] << " ";
			}
			else
			{
				cout << C[i][j] << endl;
			}
		}
	}
}