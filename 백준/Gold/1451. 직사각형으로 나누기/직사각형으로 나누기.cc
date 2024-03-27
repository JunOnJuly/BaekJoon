#include <iostream>
#include <array>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

/*
어차피 네 꼭짓점을 가졌기에 하나의 직사각형은 두개의 꼭짓점을 포함해야함
-> 하나의 직사각형은 큰 직사각형의 한 변을 포함하고 나머지를 두개로 쪼개는 방식
-> 가장 큰 직사각형을 픽스하고 두개를 쪼개면서 다 해보자
-> 네 방향 회전하면 다 해볼수 있겠다
*/

// 2차원 부분 합, 큰 직사각형에서 가로 세로로 잘라내고 두 번 잘라낸 부분 다시 더해주기
int sub_sum(array<array<int, 51>, 51> prefix_map, array<int, 2> start_idx, array<int, 2> end_idx) {
    return 
        prefix_map[end_idx[0] + 1][end_idx[1] + 1]
        - prefix_map[start_idx[0]][end_idx[1] + 1]
        - prefix_map[end_idx[0] + 1][start_idx[1]]
        + prefix_map[start_idx[0]][start_idx[1]];
}

// 한 변을 포함하는 직사각형을 제외한 나머지 사각형들의 합의 곱
long long int max_split_mul(array<array<int, 51>, 51> prefix_map, array<int, 2> start_idx, array<int, 2> end_idx) {
    // 최대 곱
    long long int max_mul = 0;
    // 현재 곱
    long long int mul = 1;
    // 가로로 잘라보기 -> 믐
    for (int i = start_idx[0]; i < end_idx[0]; i++) {
        // 위 직사각형
        // 인덱스
        array<int, 2> upper_start_idx = { start_idx[0],start_idx[1] };
        array<int, 2> upper_end_idx = { i, end_idx[1] };
        // 곱
        mul *= sub_sum(prefix_map, upper_start_idx, upper_end_idx);

        // 아래 직사각형
        // 인덱스
        array<int, 2> under_start_idx = { i + 1,start_idx[1] };
        array<int, 2> under_end_idx = { end_idx[0], end_idx[1]};
        // 곱
        mul *= sub_sum(prefix_map, under_start_idx, under_end_idx);

        // 최대 곱 최신화
        max_mul = max(max_mul, mul);
        // 현재 곱 초기화
        mul = 1;
        }

    // 세로로 잘라보기 -> ㅁ|ㅁ
    for (int i = start_idx[1]; i < end_idx[1]; i++) {
        // 왼쪽 직사각형
        // 인덱스
        array<int, 2> left_start_idx = { start_idx[0],start_idx[1] };
        array<int, 2> left_end_idx = { end_idx[0], i };
        // 곱
        mul *= sub_sum(prefix_map, left_start_idx, left_end_idx);
        
        // 오른쪽 직사각형
        // 인덱스
        array<int, 2> right_start_idx = { start_idx[0], i + 1 };
        array<int, 2> right_end_idx = { end_idx[0], end_idx[1] };
        // 곱
        mul *= sub_sum(prefix_map, right_start_idx, right_end_idx);

        // 최대 곱 최신화
        max_mul = max(max_mul, mul);

        // 현재 곱 초기화
        mul = 1;
    }

    return max_mul;
}

int main(void) {
    // 입력
    int N, M;
    cin >> N >> M;

    array<string, 50> num_map{};
    for (int i = 0; i < N; i++) {
        cin >> num_map[i];
    }
    
    // 2차원 누적 합
    array<array<int, 51>, 51> prefix_map{};
    // 누적합 인덱스
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            // 입력값 인덱스
            for (int k = 0; k <= i; k++) {
                for (int l = 0; l <= j; l++) {
                    prefix_map[i + 1][j + 1] += num_map[k][l] - '0';
                }
            }
        }
    }
    
    // 합의 곱 최댓값
    long long int max_mul{};

    // 가로로 길게 한 변 포함 -> 위에서
    for (int i = 0; i < N - 1; i++) {
        // 현재 합의 곱
        long long int mul = 1;
        // 위에서 자른 직사각형
        array<int, 2> start_idx = { 0, 0 };
        array<int, 2> end_idx = { i, M - 1 };
        mul *= sub_sum(prefix_map, start_idx, end_idx);

        // 나머지 부분 이등분 곱
        array<int, 2> sub_start_idx = { i + 1, 0 };
        array<int, 2> sub_end_idx = { N - 1, M - 1 };
        mul *= max_split_mul(prefix_map, sub_start_idx, sub_end_idx);

        // 최대 곱 최신화
        max_mul = max(max_mul, mul);

        // 현재 곱 초기화
        mul = 1;
    }

    // 가로로 길게 한 변 포함 -> 아래에서
    for (int i = N - 1; i > 0; i--) {
        // 현재 합의 곱
        long long int mul = 1;
        // 위에서 자른 직사각형
        array<int, 2> start_idx = { i, 0 };
        array<int, 2> end_idx = { N - 1, M - 1 };
        mul *= sub_sum(prefix_map, start_idx, end_idx);

        // 나머지 부분 이등분 곱
        array<int, 2> sub_start_idx = { 0, 0 };
        array<int, 2> sub_end_idx = { i - 1, M - 1 };
        mul *= max_split_mul(prefix_map, sub_start_idx, sub_end_idx);

        // 최대 곱 최신화
        max_mul = max(max_mul, mul);

        // 현재 곱 초기화
        mul = 1;
    }

    // 세로로 길게 한 변 포함 -> 왼쪽에서
    for (int i = 0; i <M; i++) {
        // 현재 합의 곱
        long long int mul = 1;
        // 위에서 자른 직사각형
        array<int, 2> start_idx = { 0, 0 };
        array<int, 2> end_idx = { N - 1, i };
        mul *= sub_sum(prefix_map, start_idx, end_idx);

        // 나머지 부분 이등분 곱
        array<int, 2> sub_start_idx = { 0, i + 1 };
        array<int, 2> sub_end_idx = { N - 1, M - 1 };
        mul *= max_split_mul(prefix_map, sub_start_idx, sub_end_idx);

        // 최대 곱 최신화
        max_mul = max(max_mul, mul);

        // 현재 곱 초기화
        mul = 1;
    }

    // 세로로 길게 한 변 포함 -> 오른쪽에서
    for (int i = M-1; i > 0; i--) {
        // 현재 합의 곱
        long long int mul = 1;
        // 위에서 자른 직사각형
        array<int, 2> start_idx = { 0, i };
        array<int, 2> end_idx = { N - 1, M - 1 };
        mul *= sub_sum(prefix_map, start_idx, end_idx);

        // 나머지 부분 이등분 곱
        array<int, 2> sub_start_idx = { 0, 0 };
        array<int, 2> sub_end_idx = { N - 1, i - 1 };
        mul *= max_split_mul(prefix_map, sub_start_idx, sub_end_idx);

        // 최대 곱 최신화
        max_mul = max(max_mul, mul);

        // 현재 곱 초기화
        mul = 1;
    }

    cout << max_mul;
}