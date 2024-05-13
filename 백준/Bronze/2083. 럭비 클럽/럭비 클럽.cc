#include <iostream>
#include <string>

using namespace std;

int main(void){
    while (true){
        string s, A;
        int a, w;
        
        cin>>s>>a>>w;
        if (s == "#") return 0;
        
        if (a > 17 or w >= 80) A = "Senior";
        else A = "Junior";
        
        cout<<s<<" "<<A<<"\n";
    }
}