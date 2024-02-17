#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		string word;
		cin >> word;

		cout << word.front() << word.back() << endl;
	}
}