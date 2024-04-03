#include <iostream>
#include <algorithm>
#include <vector>
#include <array>
#include <limits>
#include <map>
#include <set>
#include <deque>

using namespace std;

// 노드
struct Node {
    // 연결된 노드들
    vector<int> nodes;
    // 연결된 노드까지의 거리들
    vector<int> dists;
    // 해당 노드까지 도달하는데 걸린 최단 거리
    int min_dist = numeric_limits<int>::max();
    // 최단 거리로 도달하는 직전 노드
    int min_node = 0;
};

// 오름차순 정렬을 위한 함수
bool sort_arr(array<int, 2>& arr_1, array<int, 2>& arr_2) {
    return arr_1[0] > arr_2[0];
}

// 다익스트라
array<Node, 1001> dijkstra(array<Node, 1001> graph, int& N, int& except_num_1, int& except_num_2) {
    // 큐
    vector<array<int, 2>> hq = { { 0, 1 } };
    // 순회
    while (!hq.empty()) {
        // 팝 준비
        pop_heap(hq.begin(), hq.end(), sort_arr);
        // 현재 노드까지의 거리, 현재 노드 번호
        int now_dist = hq.back()[0];
        int now_num = hq.back()[1];
        // 현재 노드
        Node now_node = graph[now_num];
        // 팝
        hq.pop_back();
        // 현재 노드까지의 거리가 현재 노드까지의 최단거리보다 크면 패스
        if (now_dist > graph[now_num].min_dist) continue;
        // 현재 노드와 이어진 노드들 순회
        for (int i = 0; i < now_node.dists.size();i++) {
            // 다음 노드 번호, 다음 노드까지 거리
            int next_num = now_node.nodes[i];
            int dist = now_node.dists[i];
            // 다음 노드까지의 총 거리
            int next_dist = now_dist + dist;
            // 현재 노드 , 다음 노드 쌍이 제외된 쌍이면 패스
            if ((now_num == except_num_1 and next_num == except_num_2) or
                (now_num == except_num_2 and next_num == except_num_1))
                continue;
            // 다음 노드까지의 총 거리가 다음 노드까지의 최단거리보다 짧으면
            if (next_dist < graph[next_num].min_dist) {
                // 최단 거리 갱신
                graph[next_num].min_dist = next_dist;
                // 최단 거리로 오는 직전 노드 갱신
                graph[next_num].min_node = now_num;

                // 다음 노드가 목표 노드가 아니면
                if (next_num != N) {
                    // 큐에 추가
                    hq.push_back({ next_dist, next_num });
                    push_heap(hq.begin(), hq.end(), sort_arr);
                }
            }
        }
    }
    return graph;
}  

int main(void) {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    // 입력
    int N, M;
    cin >> N >> M;

    // 그래프 입력
    array<Node, 1001> graph;
    graph[1].min_dist = 0;
    for (int i = 0; i < M; i++) {
        int node_1, node_2, dist;
        cin >> node_1 >> node_2 >> dist;

        graph[node_1].nodes.push_back(node_2);
        graph[node_1].dists.push_back(dist);

        graph[node_2].nodes.push_back(node_1);
        graph[node_2].dists.push_back(dist);
    }

    // 제외하지 않음
    int none_except{};
    // 다익스트라
    array<Node, 1001> fixed_graph = dijkstra(graph, N, none_except, none_except);
    // 제외할 엣지 정리하기
    set<array<int, 2>> except_set;
    // 경로
    vector<int> route = { N };
    // 순회
    while (true) {
        // 현재 노드
        int now_num = route.back();
        // 다음 노드
        int next_num = fixed_graph[now_num].min_node;
        // 다음 노드가 0 이면 끝
        if (next_num == 0) break;
        else route.push_back(next_num);
        // 셋에 추가
        except_set.insert({ next_num, now_num });
    }
    // 최소거리의 최댓값
    int max_min_dist{};
    // 셋에서 제외될 수 포함하며 다익스트라
    for (auto arr : except_set) {

        /*
        cout << "--------------------------\n";
        cout << "except nodes : [" << arr[0] << " " << arr[1] << " ]\n";
        */

        array<Node, 1001> except_dijkstra = dijkstra(graph, N, arr[0], arr[1]);
        
        /*
        for (int i = 1; i < N + 1; i++) {
            cout << i << " Node ------------\n";

            cout << "nodes : [ ";
            for (auto num : except_dijkstra[i].nodes) {
                cout << num << " ";
            }
            cout << "]\n";

            cout << "dists : [ ";
            for (auto num : except_dijkstra[i].dists) {
                cout << num << " ";
            }
            cout << "]\n";

            cout << "min_dist : " << except_dijkstra[i].min_dist << "\n";

            cout << "min_nodes : "<<except_dijkstra[i].min_node<<"\n";
        }
        */

        // 최대거리 최신화
        max_min_dist = max(max_min_dist, except_dijkstra[N].min_dist);
    }
    cout << max_min_dist;
}