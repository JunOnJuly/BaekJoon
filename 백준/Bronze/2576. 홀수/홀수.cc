#include <iostream>

using namespace std;

int main(void) {
    int sum_num{};
    int min_num{ 100 };

    for (int i = 0; i < 7; i++) {
        int temp;
        cin >> temp;

        if (temp % 2) {
            if (temp < min_num) min_num = temp;
            sum_num += temp;
        }
    }
    if (min_num == 100) cout << -1;
    else cout << sum_num << "\n" << min_num;
}