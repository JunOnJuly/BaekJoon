#include <iostream>
#include <array>

using namespace std;

unsigned long long int fib(int n, array<unsigned long long int, 91>& fib_arr)
{
	if (fib_arr[n] == -1)
	{
		fib_arr[n] = fib(n - 1, fib_arr) + fib(n - 2, fib_arr);
	}
	return fib_arr[n];
}

int main(void)
{
	array<unsigned long long int, 91> fib_arr;
	fib_arr.fill(-1);
	fib_arr[0] = 0;
	fib_arr[1] = 1;

	int n;
	cin >> n;
	cout << fib(n, fib_arr);
}