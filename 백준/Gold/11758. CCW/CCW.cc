#include <iostream>
#include <array>
#include <vector>
#include <algorithm>

using namespace std;

// ccw 알고리즘
int ccw(vector<int> points) {
    // 처음 포인트 뒤에 추가
    points.push_back(points[0]);
    points.push_back(points[1]);

    // 합
    long long int sum{};
    // 계산
    for (int i = 0; i < 3; i++) {
        sum += points[i * 2] * points[((i + 1) * 2 + 1)];
        sum -= points[(i + 1) * 2] * points[i * 2 + 1];
    }

    if (sum > 0) return 1;
    else if (sum == 0) return 0;
    else return -1;
}

int main(void) {
    // 입력
    vector<int> points;
    for (int i = 0; i < 3; i++) {
        int x, y;
        cin >> x >> y;
        points.push_back(x);
        points.push_back(y);
    }

    cout << ccw(points);
}