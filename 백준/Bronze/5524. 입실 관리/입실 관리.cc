#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int N;
    cin >> N;

    string str_change;

    for (int i = 0; i < N; i++) {
        string str;
        cin >> str;

        str_change = "";

        for (int j = 0; j < str.size(); j++) {
            str_change += tolower(str[j]);
        }
        cout << str_change<<"\n";
    }

}