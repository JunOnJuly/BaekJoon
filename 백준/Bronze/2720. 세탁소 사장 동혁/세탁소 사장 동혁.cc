#include <iostream>
#include <vector>

using namespace std;

int main(void){
    vector<int> nums;
    
    int t;
    cin>>t;
    
    for (int i = 0; i<t; i++){
        int money;
        cin>>money;
        
        nums.push_back(money/25);
        money %= 25;
        
        nums.push_back(money/10);
        money %= 10;
        
        nums.push_back(money/5);
        money %= 5;
        
        nums.push_back(money/1);
    }
    
    for (auto num : nums){
        cout<<num<<" ";
    }
    cout<<"\n";
}