#include <iostream>
#include <array>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int main(void) {
    // 입력
    int N, M;
    cin >> N >> M;

    // 자신의 자식 노드들을 기록
    array<vector<int>, 32001> children_arr;
    // 자신에게 들어오는 노드들의 수를 기록
    array<int, 32001> topol_arr{};
    // 입력
    for (int i = 0; i < M; i++) {
        int parent, child;
        cin >> parent >> child;

        children_arr[parent].push_back(child);
        topol_arr[child] += 1;
    }

    // 줄
    vector<int> line;
    // 방문 목록
    array<bool, 32001> visited;
    visited.fill(true);
    // 순회
    while (line.size() != N) {
        // 줄을 세울 목록 큐
        deque<int> line_dq;

        for (int i = 1; i < N+1; i++) {
            // 방문한적 없고 들어오는 노드가 없는 노드
            if (visited[i] and topol_arr[i] == 0) {
                // 목록 작성
                line_dq.push_back(i);
                // 방문기록
                visited[i] = false;
            }
        }

        // 실제로 줄 세우기
        for (auto num : line_dq) {
            line.push_back(num);
            // 줄 세운 노드가 들어가는 노드 
            for (auto child : children_arr[num]) {
                // 들어가는 수 -1
                topol_arr[child] -= 1;
            }
        }
    }

    for (auto num : line) {
        cout << num << " ";
    }
}