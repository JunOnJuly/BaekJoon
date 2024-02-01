#include <iostream>

using namespace std;

int main(void)
{
    int A;
    int B;
    cin >> A >> B;

    if (A > B)
    {
        cout << ">" << endl;
    }
    else if (A < B)
    {
        cout << "<" << endl;
    }
    else
    {
        cout << "==" << endl;
    }
}