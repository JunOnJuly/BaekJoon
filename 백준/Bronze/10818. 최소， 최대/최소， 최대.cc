#include <iostream>
#include <algorithm>

using namespace std;

int main(void)
{
    int N;
    cin >> N;

    int* data_list = new int[N];
    int max_num = -1000000;
    int min_num = 1000000;

    for (int i = 0; i < N; i++)
    {
        cin >> data_list[i];
    }

    for (int i = 0; i < N; i++)
    {
        max_num = max(data_list[i], max_num);
        min_num = min(data_list[i], min_num);
    }

    cout << min_num << " " << max_num << endl;
}