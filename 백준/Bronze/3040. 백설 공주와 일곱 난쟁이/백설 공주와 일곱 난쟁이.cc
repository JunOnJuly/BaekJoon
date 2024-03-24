#include <iostream>
#include <array>
#include <algorithm>
#include <numeric>

using namespace std;

int main(void) {
    array<int, 9> num_arr;
    for (int i = 0; i < 9; i++) {
        cin >> num_arr[i];
    }

    sort(num_arr.begin(), num_arr.end());

    do {
        int sum_seven = accumulate(num_arr.begin(), num_arr.begin() + 7, 0);
        if (sum_seven == 100) {
            for (int i = 0; i < 7; i++) {
                cout << num_arr[i] << "\n";
            }
            return 0;
        }
    } while (next_permutation(num_arr.begin(), num_arr.end()));
}