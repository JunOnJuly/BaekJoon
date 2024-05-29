#include <iostream>

using namespace std;

int main(void){
    int sum_num{};
    while(true){
        int temp;
        cin>>temp;
        
        if (temp == -1) break;
        sum_num += temp;
    }
    cout<<sum_num;
}