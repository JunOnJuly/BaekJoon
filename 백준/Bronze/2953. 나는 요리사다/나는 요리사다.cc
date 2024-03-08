#include <iostream>
#include <array>
#include <algorithm>

using namespace std;

int main(void)
{
	array<int, 5> sum_arr{};

	for (int i = 0; i < 5; i++)
	{
		int sum_nums{};
		for (int j = 0; j < 4; j++)
		{
			int num{};
			cin >> num;

			sum_nums += num;
		}
		sum_arr[i] = sum_nums;
	}
	int max_idx = max_element(sum_arr.begin(), sum_arr.end()) - sum_arr.begin();
	int max_num = *max_element(sum_arr.begin(), sum_arr.end());

	cout << max_idx + 1 << " " << max_num;
}