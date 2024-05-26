#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(void) {
    map<string, int> unvs;

    int S, K, H;
    cin >> S >> K >> H;

    unvs.insert({ "Soongsil", S });
    unvs.insert({ "Korea", K });
    unvs.insert({ "Hanyang", H });

    if (S + K + H >= 100) cout << "OK";
    else {
        int min_unv = 100;
        string min_unv_str;

        for (auto iter : unvs) {
            if (iter.second < min_unv) {
                min_unv = iter.second;
                min_unv_str = iter.first;
            }
        }

        cout << min_unv_str;
    }
}