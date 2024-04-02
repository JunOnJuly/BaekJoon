#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        string temp_input;
        cin >> temp_input;

        cout << static_cast<int>(temp_input[0]) + static_cast<int>(temp_input[2]) - 2 * static_cast<int>('0') << "\n";
    }
}