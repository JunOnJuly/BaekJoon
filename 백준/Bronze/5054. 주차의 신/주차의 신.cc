#include <iostream>
//
#include <vector>
//
#include <algorithm>

using namespace std;

int main(void)
{
	int t;
	cin >> t;
	for (int _ = 0; _ < t; _++)
	{
		int n;
		cin >> n;

		vector<int> xis;
		for (int i = 0; i < n; i++)
		{
			int num;
			cin >> num;

			xis.push_back(num);
		}
		
		auto minmax_vec = minmax_element(xis.begin(), xis.end());
		
		cout << (*minmax_vec.second - *minmax_vec.first) * 2 << "\n";
	}
}