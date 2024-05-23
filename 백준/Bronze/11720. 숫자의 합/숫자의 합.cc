#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int n;
    cin >> n;

    string nums;
    cin >> nums;

    int sum = 0;
    for (auto num : nums) {
        sum += num - '0';
    }
    cout << sum;
}