#include <iostream>
#include <algorithm>

using namespace std;

int main(void){
    int sum{};
    
    for (int i = 0; i<5;i++){
        int temp;
        cin>>temp;
        
        sum += max(40, temp);
    }
    
    cout<<sum/5;
}