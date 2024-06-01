#include <iostream>

using namespace std;

int main(void){
    int N;
    cin>>N;
    
    int A,B;
    cin>>A>>B;
    
    cout<<min(N, A/2+B);
}