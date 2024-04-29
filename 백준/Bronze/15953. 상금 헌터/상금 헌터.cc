#include <iostream>

using namespace std;

int main(void) {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int a, b;
        cin >> a >> b;

        int money_sum = 0;

        if (a == 0) money_sum += 0;
        else if (a == 1) money_sum += 5000000;
        else if (a <= 3) money_sum += 3000000;
        else if (a <= 6) money_sum += 2000000;
        else if (a <= 10) money_sum += 500000;
        else if (a <= 15) money_sum += 300000;
        else if (a <= 21) money_sum += 100000;

        if (b == 0) money_sum += 0;
        else if (b == 1) money_sum += 5120000;
        else if (b <= 3) money_sum += 2560000;
        else if (b <= 7) money_sum += 1280000;
        else if (b <= 15) money_sum += 640000;
        else if (b <= 31) money_sum += 320000;

        cout << money_sum << "\n";
    }
}