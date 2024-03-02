#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	vector<long long int> min_heap;

	for (int i = 0; i < N; i++)
	{
		long long int num;
		cin >> num;

		if (num == 0) {
			if (min_heap.empty())
			{
				cout << 0 << "\n";
			}
			else
			{
				pop_heap(min_heap.begin(), min_heap.end());
				cout << -min_heap.back() << "\n";
				min_heap.pop_back();
			}
		}
		else
		{
			min_heap.push_back(-num);
			push_heap(min_heap.begin(), min_heap.end());
		}
	}
}