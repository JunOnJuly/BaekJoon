#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    set<int> answer_set;
    
    sort(numbers.begin(), numbers.end());
    for (int i = 0; i < numbers.size()-1; i++){
        for (int j = i+1; j < numbers.size(); j++){
            answer_set.insert(numbers[i] + numbers[j]);
        }
    }
    
    vector<int> answer(answer_set.begin(), answer_set.end());
    
    return answer;
}