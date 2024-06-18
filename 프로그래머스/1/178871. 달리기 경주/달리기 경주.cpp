#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    // 순서 매핑
    unordered_map<string, int> line_str;
    unordered_map<int, string> line_int;
    
    for (int i = 0; i < players.size(); i++){
        line_str[players[i]] = i;
        line_int[i] = players[i];
    }
    // 불린 인덱스
    int called_idx = 0;
    // 순회
    while (called_idx < callings.size()){
        // 불린 이름
        string called_name = callings[called_idx];
        called_idx += 1;
        //// 검색
        // 몇 번째 인지
        int line_num = line_str[called_name];
        // 앞선 사람은 누구인지
        string line_name = line_int[line_num - 1];
        // 스왑
        int temp_int = line_str[line_name];        
        line_str[line_name] = line_str[called_name];
        line_str[called_name] = temp_int;
        
        string temp_str = line_int[line_num];
        line_int[line_num] = line_int[line_num - 1];
        line_int[line_num - 1] = temp_str;
    }
    // 리턴
    vector<string> result;
    for (int i = 0; i < players.size(); i++){
        result.push_back(line_int[i]);
    }
    
    return result;
}