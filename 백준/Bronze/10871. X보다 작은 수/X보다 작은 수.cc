#include <iostream>
#include <array>

using namespace std;

int main(void)
{
    // 변수, 어레이 선언
    int N, X;
    array<int, 10000> data_array;

    // 변수, 어레이 입력 및 초기화
    cin >> N >> X;
    for (int i=0; i < N; i++)
    {
        cin >> data_array[i];
    }

    // 순회하며 대소 비교
    for (int i=0; i < N; i++)
    {
        if (data_array[i] < X)
        {
            cout << data_array[i] << " ";
        }
    }
}