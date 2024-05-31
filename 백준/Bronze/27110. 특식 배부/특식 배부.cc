#include <iostream>

using namespace std;

int main(void){
    int N;
    cin>>N;
    
    int A,B,C;
    cin>>A>>B>>C;
    
    int sum_num;
    sum_num += min(N, A);
    sum_num += min(N, B);
    sum_num += min(N, C);
    
    cout<<sum_num;
}