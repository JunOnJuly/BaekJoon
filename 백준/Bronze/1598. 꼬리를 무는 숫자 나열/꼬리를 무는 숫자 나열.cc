#include <iostream>

using namespace std;

int main(void){
    int A, B;
    cin>>A>>B;
    
    int A_x, A_y;
    A_x = (A-1) / 4;
    A_y = (A-1) % 4;
    
    int B_x, B_y;
    B_x = (B-1) / 4;
    B_y = (B-1) % 4;
    
    cout<<abs(A_x - B_x) + abs(A_y - B_y);
}