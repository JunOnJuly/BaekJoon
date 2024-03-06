#include <iostream>
#include <map>

using namespace std;

int main(void)
{
	// 합 기록
	int sum{};
	// 파이썬의 딕셔너리와 비슷
	map<int, int> count_map;
	for (int i = 0; i < 10; i++)
	{
		// 입력
		int num{};
		cin >> num;
		// 합
		sum += num;

		// 딕셔너리에 기록, 이미 존재하면 +1 존재하지 않으면 1
		auto iter = count_map.find(num);
		if (iter == count_map.end()) count_map[num] = 1;
		else count_map[num] += 1;
	}

	// key, value 순회하며 최댓값 갱신
	int max_key{};
	int max_value{};
	for (auto iter = count_map.begin(); iter != count_map.end(); iter++)
	{
		if (iter->second > max_value)
		{
			max_key = iter->first;
			max_value = iter->second;
		}
	}

	cout << sum/10 << "\n" << max_key;
}