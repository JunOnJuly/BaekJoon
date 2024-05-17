#include <iostream>

using namespace std;

int main(void){
    int K, N, M;
    cin>>K>>N>>M;
    
    cout<<max(0, K*N-M);
}