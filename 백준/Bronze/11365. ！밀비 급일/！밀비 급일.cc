#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string ipt;
    while (getline(cin, ipt, '\n')) {
        if (ipt == "END") return 0;
        for (int i = ipt.size() - 1; i >= 0; i--) {
            cout << ipt[i];
        }
        cout << "\n";
    }
}