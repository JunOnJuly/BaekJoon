#include <iostream>

using namespace std;

int main(void){
    int N;
    cin>>N;
    
    int stack = 1;
    int score = 0;
    for (int i = 0; i < N; i++){
        int result;
        cin>>result;
        
        if (result == 1){
            score += stack;
            stack += 1;
        }
        else {
            stack = 1;
        }
    }
    cout<<score;
}