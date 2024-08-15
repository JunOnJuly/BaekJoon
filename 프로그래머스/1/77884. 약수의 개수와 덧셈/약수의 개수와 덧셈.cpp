#include <string>
#include <cmath>

using namespace std;

int solution(int left, int right) {
    int sum_nums = 0;
    
    for (int num=left; num<=right; num++){
        float sqr_num = sqrt(num);
        
        if (sqr_num == floor(sqr_num)) sum_nums -= num;
        else sum_nums += num;
    }
    
    return sum_nums;
}