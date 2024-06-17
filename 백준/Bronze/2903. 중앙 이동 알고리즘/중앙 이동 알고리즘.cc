#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main(void) {
    int n;
    cin >> n;

    vector<long long int> guides = { 2 };

    for (int i = 0; i < 15; i++) {
        guides.push_back(guides.back() * 2 - 1);
    }

    cout << fixed;
    cout.precision(0);
    cout << pow(guides[n], 2);
}