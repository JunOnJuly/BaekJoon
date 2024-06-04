#include <iostream>

using namespace std;

int main(void) {
    int N;
    cin >> N;

    int y = 0;
    int m = 0;

    for (int i = 0; i < N; i++) {
        int M;
        cin >> M;

        int num1;
        num1 = M / 30 + 1;

        y += num1 * 10;

        int num2;
        num2 = M / 60 + 1;

        m += num2 * 15;
    }

    if (y == m) cout << "Y M " << y;
    else if (y > m) cout << "M " << m;
    else cout << "Y " << y;
}