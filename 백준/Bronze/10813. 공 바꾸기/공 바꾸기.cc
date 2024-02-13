#include <iostream>
#include <array>

using namespace std;

int main(void)
{
    int N;
    int M;
    cin >> N >> M;

    array<int, 100> data_list = {};
    for (int num = 0; num < N; num++)
    {
        data_list[num] = num + 1;
    }

    for (int num = 0; num < M; num++)
    {
        int i;
        int j;
        cin >> i >> j;

        int temp;
        temp = data_list[i-1];
        data_list[i-1] = data_list[j-1];
        data_list[j-1] = temp;
    }

    for (int num = 0; num < N; num++)
    {
        cout << data_list[num] << " ";
    }
}