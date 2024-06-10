#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main(void) {
    long long int S, K;
    cin >> S >> K;

    vector<long long int> nums(K, S / K);

    int subnum = S - accumulate(nums.begin(), nums.end(), 0);

    for (int i = 0; i < subnum; i++) nums[i] += 1;

    long long int mul = 1;
    for (auto num : nums) mul *= num;

    cout << mul;
}