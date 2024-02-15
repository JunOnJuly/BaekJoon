#include <iostream>
#include <deque>
#include <array>

using namespace std;

int main(void)
{
    deque<array<int, 2>> dq;

    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        array<int, 2> temp_arr = {};
        temp_arr[0] = i + 1;
        cin >> temp_arr[1];
        dq.push_back(temp_arr);
    }

    for (int i = 0; i < N; i++)
    {
        array<int, 2> step = dq.front();
        cout << step[0] << " ";
        dq.pop_front();
        if (dq.size() == 0)
        {
            return 0;
        }

        if (step[1] < 0)
        {
            for (int j = 0; j < -step[1]; j++)
            {
                dq.push_front(dq.back());
                dq.pop_back();
            }
        }
        else
        {
            for (int j = 0; j < step[1] - 1; j++)
            {
                dq.push_back(dq.front());
                dq.pop_front();
            }
        }
    }
}