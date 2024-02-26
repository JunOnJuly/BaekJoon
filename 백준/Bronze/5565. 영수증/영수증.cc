#include <iostream>
#include <array>

using namespace std;

int main(void)
{
	int sum_price;
	cin >> sum_price;

	for (int i = 0; i < 9; i++)
	{
		int temp_price = 0;
		cin >> temp_price;
		sum_price -= temp_price;
	}

	cout << sum_price;
}