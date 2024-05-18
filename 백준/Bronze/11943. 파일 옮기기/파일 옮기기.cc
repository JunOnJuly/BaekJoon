#include <iostream>

using namespace std;

int main(void){
    int A, B;
    cin>>A>>B;
    
    int C, D;
    cin>>C>>D;
    
    cout<<min(A+D, B+C);
}