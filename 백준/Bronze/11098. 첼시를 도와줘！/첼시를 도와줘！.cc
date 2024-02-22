#include <iostream>
#include <array>
#include <vector>
#include <string>

using namespace std;

int main(void)
{
	int n;
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		int p;
		cin >> p;

		vector<int> value;
		vector<string> name;

		for (int j = 0; j < p; j++)
		{
			int temp_value;
			string temp_name;

			cin >> temp_value >> temp_name;
			value.push_back(temp_value);
			name.push_back(temp_name);
		}

		int max_idx = 0;
		string max_name="";

		for (int j = 0; j < p; j++)
		{
			if (value[max_idx] <= value[j])
			{
				max_idx = j;
				max_name = name[j];
			}
		}

		cout << max_name << "\n";
	}
}