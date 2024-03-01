#include <iostream>
#include <string>
#include <array>

using namespace std;

int main(void)
{
	int A, B, C;
	cin >> A >> B >> C;

	int mul = A * B * C;
	string mul_string = to_string(mul);

	array<int, 10> num_arr{};

	for (auto chr : mul_string)
	{
		num_arr[chr-'0'] += 1;
	}

	for (auto num : num_arr)
	{
		cout << num << "\n";
	}
}