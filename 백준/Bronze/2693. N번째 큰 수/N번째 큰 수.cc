#include <iostream>
#include <array>
#include <algorithm>

using namespace std;

int main(void){
    int T;
    cin >> T;
    
    for (int _ = 0; _ < T; _++){
        array<int, 10> nums{};
        for (int i = 0; i < 10; i++){
            cin>>nums[i];
        }
        
        sort(nums.begin(), nums.end());
        
        cout<<nums[7]<<"\n";
    }
}