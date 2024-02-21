#include <iostream>
#include <array>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

int main(void)
{
	int N, M;
	cin >> N >> M;

	array<int, 101> sqr_arr;
	for (int i = 0; i < 101; i++)
	{
		sqr_arr[i] = pow(i, 2);
	}

	int left = 1;
	int right = 100;
	bool left_check = false;
	bool right_check = false;
	while (true)
	{
		if (left > right)
		{
			cout << -1;
			return 0;
		}
		if (right_check and left_check)
		{
			break;
		}
		if (!left_check)
		{
			if (sqr_arr[left] < N)
			{
				left++;
			}
			else
			{
				left_check = true;
			}
		}

		if (!right_check)
		{
			if (sqr_arr[right] > M)
			{
				right--;
			}
			else
			{
				right_check = true;
			}
		}
	}
	
	int sum_sqr = 0;
	for (int i = left; i <= right; i++)
	{
		sum_sqr += sqr_arr[i];
	}

	cout << sum_sqr << "\n" << sqr_arr[left];
}