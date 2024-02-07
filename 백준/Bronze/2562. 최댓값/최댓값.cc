#include <iostream>
#include <algorithm>

using namespace std;

int find_max(int data_list[9], int &max_num, int &max_idx)
{
	for (int i = 0; i < 9; i++)
	{
		if (max_num < data_list[i])
		{
			max_num = data_list[i];
			max_idx = i;
		}
	}
	return 0;
}


int main(void)
{
	int data_list[9] = {};
	int max_num = 0;
	int max_idx = 0;

	for (int i = 0; i < 9; i++)
	{
		cin >> data_list[i];
	}

	find_max(data_list, max_num, max_idx);
	cout << max_num << endl << max_idx+1 << endl;
}