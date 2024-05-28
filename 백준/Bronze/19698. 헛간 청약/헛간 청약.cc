#include <iostream>

using namespace std;

int main(void) {
    // 소들의 수 N, 헛간의 크기 W H를 나타내는 두 정수 W와 H, 그리고 소들에게 배정되는 공간의 크기 L이 순서대로 주어진다.
    int N, W, H, L;
    cin >> N >> W >> H >> L;

    W /= L;
    H /= L;

    cout << min(N, W * H);
}