#include <iostream>
#include <string>

using namespace std;

int main(void){
    while (true){
        int cnt = 1;
        
        string num;
        cin>>num;
        
        if (num == "0") return 0;
        
        for (auto chr : num){
            if (chr == '1') cnt += 3;
            else if (chr == '0') cnt += 5;
            else cnt += 4;
        }
        
        cout<<cnt<<"\n";
    }
}