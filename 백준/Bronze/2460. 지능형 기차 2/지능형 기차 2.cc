#include <iostream>
#include <array>

using namespace std;

int main(void)
{
	int train_num{};
	int max_num{};

	for (int i = 0; i < 10; i++)
	{
		int out_num{};
		int in_num{};
		cin >> out_num >> in_num;

		train_num = max(0, train_num - out_num);
		train_num = min(10000, train_num + in_num);
		
		if (train_num > max_num)
		{
			max_num = train_num;
		}
	}

	cout << max_num;
}