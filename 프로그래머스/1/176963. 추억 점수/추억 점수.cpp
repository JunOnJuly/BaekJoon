#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    // 이름 점수 매칭
    map<string, int> yearnings;
    for (int i = 0; i < yearning.size(); i++){
        yearnings[name[i]] = yearning[i];
    }
    // 결과
    vector<int> result;
    // 사진 순회
    for (auto vec : photo){
        // 저장할 점수
        int score = 0;
        // 이름 점수 매칭
        for (auto str : vec){
            if (yearnings.find(str) != yearnings.end()){
                score += yearnings[str];
            }
        }
        
        result.push_back(score);
    }
    
    return result;
}