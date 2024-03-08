#include <iostream>
#include <map>

using namespace std;

int main(void)
{
	map<int, int> num_map;
	for (int i = 0; i < 10; i++)
	{
		int num{};
		cin >> num;
		num %= 42;

		auto iter = num_map.find(num);
		if (iter != num_map.end()) num_map[num] = 1;
		else num_map[num] += 1;

	}
	cout << num_map.size();
}