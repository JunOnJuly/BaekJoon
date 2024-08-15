#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    int zero_cnt = count(lottos.begin(), lottos.end(), 0);
    
    int cor_cnt = 0;
    for (auto num : win_nums) {
        auto iter = find(lottos.begin(), lottos.end(), num);
        
        if (iter != lottos.end()) cor_cnt += 1;
    }
    
    return {min({7-(zero_cnt+cor_cnt), 6}), min({7-cor_cnt, 6})};
}