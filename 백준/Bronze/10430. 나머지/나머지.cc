#include <iostream>

using namespace std;

int main(void){
    int A, B, C, D;
    cin>>A>>B>>C>>D;
    
    cout<<(A+B)%C<<"\n";
    cout<<((A%C) + (B%C))%C<<"\n";
    cout<<(A*B)%C<<"\n";
    cout<<((A%C) * (B%C))%C<<"\n";
}