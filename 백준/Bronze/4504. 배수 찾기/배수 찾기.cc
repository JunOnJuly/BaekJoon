#include <iostream>

using namespace std;

int main(void){
    int n;
    cin>>n;
    
    while (true){
        int num;
        cin>>num;
        
        if (num == 0) return 0;
        
        if (num % n) cout<<num<<" is NOT a multiple of "<<n<<".\n";
        else cout<<num<<" is a multiple of "<<n<<".\n";
    }
}