#include <iostream>

using namespace std;

int main(void){
    while (true){
        int A, B;
        cin>>A>>B;
    
        if (A==0 and B==0) return 0;
    
        if (A>B) cout<<"Yes\n";
        else cout<<"No\n";
    }
}