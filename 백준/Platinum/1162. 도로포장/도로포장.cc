#include <iostream>
#include <array>
#include <vector>
#include <deque>
#include <limits>
#include <algorithm>

using namespace std;

// 최소힙을 위한 연산자 클래스
class Dijk_oper {
public:
    bool operator()(const array<long long int, 3> node_1, const array<long long int, 3> node_2) const {
        return node_1[0] > node_2[0];
    }
};

// 다익스트라
long long int dijkstra(array<vector<array<int, 2>>, 10001>& graph_arr, int pave, int target) {
    // 시스템상 최댓 값
    long long int max_dist = numeric_limits<long long int>::max();
    // 최단거리 어레이, [ 잔여 포장 횟수, 현재 노드 ]
    array<array<long long int, 10001>, 22> dist_arr{};
    for (int i = 0; i < 22; i++) {
        dist_arr[i].fill(max_dist);
    }

    // 힙, { 현재 거리, 현재 노드, 잔여 포장 횟수 }
    deque<array<long long int, 3>> hq = { { 0, 1, pave } };
    // 순회
    while (!hq.empty()) {

        /* ---DEBUG---
        cout << "{ ";
        for (auto datas : hq) {
            cout << "{ ";
            for (auto data : datas) {
                cout << data << " ";
            }
            cout << "} ";
        }
        cout << "}" << "\n";

        for (int i = 0; i < pave + 1; i++) {
            cout << "pave : " << i << "    { ";
            for (int j = 0; j < target; j++) {
                cout << dist_arr[i][j + 1] << " ";
            }
            cout << "}" << "\n";
        }
        cout << "\n";
        */

        // 팝 준비
        pop_heap(hq.begin(), hq.end(), Dijk_oper());
        // 현재 거리, 현재 노드, 잔여 포장 횟수
        long long int now_dist = hq.back()[0];
        int now_node = hq.back()[1];
        int now_pave = hq.back()[2];
        // 팝
        hq.pop_back();

        // 현재 거리가 같은 잔여 포장 횟수의 현재 노드까지 최단거리보다 길면 패스
        if (now_dist > dist_arr[now_pave][now_node]) continue;

        // 자식 순회
        for (auto child : graph_arr[now_node]) {
            // 거리, 다음 노드
            int dist = child[0];
            int next_node = child[1];
            // 다음 노드까지의 거리
            long long int next_dist = now_dist + dist;
            // 다음 노드까지의 거리가 같은 잔여 포장 횟수의 다음 노드까지의 최단거리보다 짧으면
            if (next_dist < dist_arr[now_pave][next_node]) {
                // 목적지가 아니면 큐에 추가
                if (next_node != target) {
                    hq.push_back({ next_dist, next_node, now_pave });
                    push_heap(hq.begin(), hq.end(), Dijk_oper());
                }
                // 최단거리 최신화
                dist_arr[now_pave][next_node] = next_dist;
            }
            // 도로 포장 횟수가 남아있고 현재 노드까지의 거리가 잔여 포장 횟수 - 1 의 다음 노드 까지의 최단거리보다 짧으면
            // -> 현재 도로를 포장했을 때 다음 노드까지의 최단거리보다 짧으면
            if (now_pave > 0 and now_dist < dist_arr[now_pave - 1][next_node]) {
                // 목적지가 아니면 큐에 추가
                if (next_node != target) {
                    hq.push_back({ now_dist, next_node, now_pave - 1 });
                    push_heap(hq.begin(), hq.end(), Dijk_oper());
                }
                // 최단거리 최신화
                dist_arr[now_pave - 1][next_node] = now_dist;
            }
        }
    }
    
    // 최솟값중 최솟값을 출력
    long long int min_dir = max_dist;
    for (int i = 0; i < pave; i++) {
        if (dist_arr[i][target] < min_dir) min_dir = dist_arr[i][target];
    }

    return min_dir;
}

int main(void) {
    // 선언
    int N, M, K;
    array<vector<array<int, 2>>, 10001> graph_arr;

    // 입력
    cin >> N >> M >> K;

    for (int i = 0; i < M; i++) {
        int node_1, node_2, dist;
        cin >> node_1 >> node_2 >> dist;

        graph_arr[node_1].push_back({ dist, node_2 });
        graph_arr[node_2].push_back({ dist, node_1 });
    }

    // 다익스트라
    cout << dijkstra(graph_arr, K, N);
}