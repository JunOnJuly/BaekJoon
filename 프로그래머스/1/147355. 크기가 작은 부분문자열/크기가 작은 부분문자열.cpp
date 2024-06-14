#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string t, string p) {
    // 카운트
    int cnt = 0;
    
    // t, p 길이
    int t_len = t.size();
    int p_len = p.size();
    
    // t 순회
    for (int i = 0; i <= t_len - p_len; i++){
        // t 의 부분 문자열
        string sub_str_t = t.substr(i, p_len);
        // 부분 문자열과 p 비교
        for (int j = 0; j < p_len; j++){
            if (sub_str_t[j] < p[j]){
                cnt += 1;
                break;
            }
            else if (sub_str_t[j] > p[j]){
                break;
            }
            else if (j == p_len - 1) cnt += 1;
        }
    }
    
    return cnt;
}