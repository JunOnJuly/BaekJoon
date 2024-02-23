#include <iostream>
#include <string>
#include <array>

using namespace std;

int main(void)
{
	int n;
	cin >> n;

	array<string, 100> name_arr;
	array<int, 100> year_arr;
	array<int, 100> month_arr;
	array<int, 100> day_arr;

	for (int i = 0; i < n; i++)
	{
		cin >> name_arr[i] >> day_arr[i] >> month_arr[i] >> year_arr[i];
	}

	int max_arr = 0;
	int min_arr = 0;

	for (int i = 1; i < n; i++)
	{
		if (year_arr[i] < year_arr[max_arr])
		{
			max_arr = i;
		}
		else if (year_arr[i] == year_arr[max_arr])
		{
			if (month_arr[i] < month_arr[max_arr])
			{
				max_arr = i;
			}
			else if (month_arr[i] == month_arr[max_arr])
			{
				if (day_arr[i] < day_arr[max_arr])
				{
					max_arr = i;
				}
			}
		}

		if (year_arr[i] > year_arr[min_arr])
		{
			min_arr = i;
		}
		else if (year_arr[i] == year_arr[min_arr])
		{
			if (month_arr[i] > month_arr[min_arr])
			{
				min_arr = i;
			}
			else if (month_arr[i] == month_arr[min_arr])
			{
				if (day_arr[i] > day_arr[min_arr])
				{
					min_arr = i;
				}
			}
		}
	}

	cout << name_arr[min_arr] << "\n" << name_arr[max_arr];
}