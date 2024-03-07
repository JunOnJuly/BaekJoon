#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		int N;
		string str;
		cin >> N >> str;

		str.erase(N - 1, 1);

		cout << str << "\n";
	}
}