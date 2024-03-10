#include <iostream>
#include <array>

using namespace std;

int main(void)
{
	int A, B;
	cin >> A >> B;

	array<int, 1001> num_arr;
	int i = 0;
	int j = 0;
	int cnt = 0;
	while (cnt != 1001)
	{
		num_arr[cnt] = i;
		cnt += 1;
		
		if (i == j)
		{
			i += 1;
			j = 1;
		}
		else
		{
			j += 1;
		}
	}
	
	for (int i = 1; i < 1001; i++)
	{
		num_arr[i] += num_arr[i - 1];
	}

	cout << num_arr[B] - num_arr[A - 1];
}