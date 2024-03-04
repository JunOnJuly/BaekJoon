#include <iostream>
#include <array>
#include <string>

using namespace std;

int main(void)
{
	float sum_grades{};
	float num_grades{};

	for (int i = 0; i < 20; i++)
	{
		string name;
		float num;
		string grade;

		cin >> name >> num >> grade;

		if (grade == "P") continue;
		else if (grade == "A+") { sum_grades += num * 4.5; num_grades += num; }
		else if (grade == "A0") { sum_grades += num * 4.0; num_grades += num; }
		else if (grade == "B+") { sum_grades += num * 3.5; num_grades += num; }
		else if (grade == "B0") { sum_grades += num * 3.0; num_grades += num; }
		else if (grade == "C+") { sum_grades += num * 2.5; num_grades += num; }
		else if (grade == "C0") { sum_grades += num * 2.0; num_grades += num; }
		else if (grade == "D+") { sum_grades += num * 1.5; num_grades += num; }
		else if (grade == "D0") { sum_grades += num * 1.0; num_grades += num; }
		else if (grade == "F") { num_grades += num; }
	}

	cout << sum_grades / num_grades;
}