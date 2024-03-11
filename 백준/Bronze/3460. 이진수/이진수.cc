#include <iostream>

#include <array>
#include <vector>
#include <string>
#include <bitset>

#include <algorithm>

using namespace std;

int main(void)
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int n;
		cin >> n;

		string bin_n = bitset<20>(n).to_string();
		reverse(bin_n.begin(), bin_n.end());

		vector<int> idx_vec;
		for (int i = 0; i < bin_n.size(); i++)
		{
			if (bin_n[i] == '1') idx_vec.push_back(i);
		}

		for (auto num : idx_vec) cout << num << " ";
	}
}