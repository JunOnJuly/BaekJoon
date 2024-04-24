#include <iostream>
#include <cmath>
#include <array>

using namespace std;

int main(void){
    array<int, 2> nums;
    for (int i = 0; i<5;i++){
        cin>>nums[i];
    }
    int sum{};
    for (int i = 0;i<5;i++){
        sum += pow(nums[i], 2);
    }
    cout<<sum%10;
}