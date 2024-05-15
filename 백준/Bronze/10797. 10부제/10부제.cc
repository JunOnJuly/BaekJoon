#include <iostream>

using namespace std;

int main(void){
    int N;
    cin>>N;
    
    int cnt{};
    for (int i = 0; i<5;i++){
        int num;
        cin>>num;
        
        if (num == N) cnt += 1;
    }
    
    cout<<cnt;
}