#include <iostream>
//
#include <string>
//
#include <algorithm>

using namespace std;

int main(void)
{
	string word;
	cin >> word;

	string exp;
	cin >> exp;

	string stk;
	int idx{};
	while (idx<word.size())
	{
		stk += word[idx];
		if (stk.size() >= exp.size() and stk.back() == exp.back())
		{
			if (stk.substr(stk.length() - exp.length(), exp.length()) == exp)
			{
				stk.erase(stk.length() - exp.length(), exp.length());
			}
		}
		idx += 1;
	}

	if (stk.size() > 0)	cout << stk;
	else cout << "FRULA";
}	