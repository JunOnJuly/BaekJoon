#include <vector>
#include <cmath>

using namespace std;

bool is_unique(int num){
    for (int i = 2; i <= static_cast<int>(sqrt(num)); i++){
        if (num % i == 0) return false;
    }    
    return true;
}


int solution(vector<int> nums) {
    int answer = 0;
    
    for (int i = 0; i < nums.size()-2; i++){
        for (int j = i+1; j < nums.size()-1; j++){
            for (int k = j+1; k < nums.size(); k++){
                if (is_unique(nums[i]+nums[j]+nums[k])){
                    answer += 1;
                }
            }
        }
    }
    return answer;
}