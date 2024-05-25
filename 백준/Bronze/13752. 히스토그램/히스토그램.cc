#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;

        string output;
        for (int j = 0; j < k; j++) {
            output.append("=");
        }
        cout << output << "\n";
    }
}