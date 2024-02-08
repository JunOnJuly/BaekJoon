#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<string> split(string str, char Delimiter)
{
	istringstream iss(str);
	string buffer;

	vector<string> querys;

	while (getline(iss, buffer, Delimiter))
	{
		querys.push_back(buffer);
	}
	return querys;
}


int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	// 스택 선언
	stack<int> nums;
	// 입력 선언 및 초기화
	int N;
	cin >> N;
	// 공백문자 제거
	cin.ignore();
	// 입력 및 실행
	for (int i = 0; i < N; i++)
	{
		// 명령어 입력
		string str;
		std::getline(cin, str, '\n');
		// 명령어 분할
		vector<string> querys = split(str, ' ');
		// 1 명령이면
		if (querys[0] == "1")
		{
			// 스택에 추가
			nums.push(stoi(querys[1]));
		}
		else
		{
			if (querys[0] == "2")
			{
				if (nums.size() != 0)
				{
					// 맨 위 출력
					cout << nums.top() << "\n";
					// 맨 위 제거
					nums.pop();
				}
				else
				{
					cout << -1 << "\n";
				}
			}
			else if (querys[0] == "3")
			{
				// 정수의 개수 출력
				cout << nums.size() << "\n";
			}
			else if (querys[0] == "4")
			{
				if (nums.empty())
				{
					cout << 1 << "\n";
				}
				else
				{
					cout << 0 << "\n";
				}
			}
			else if (querys[0] == "5")
			{
				if (nums.size() != 0)
				{
					cout << nums.top() << "\n";
				}
				else
				{
					cout << -1 << "\n";
				}
			}
		}
	}
}