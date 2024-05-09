#include <iostream>

using namespace std;

int main(void){
    long long int sum_nums = 0;
    for (int i = 0; i<5; i++){
        long long int num;
        cin>>num;
        sum_nums += num;
    }
    cout<<sum_nums;
}