#include <string>
#include <vector>
#include <numeric>

using namespace std;

int solution(vector<int> numbers) {
    int sum_numbers = accumulate(numbers.begin(), numbers.end(), 0);
    return 45 - sum_numbers;
}