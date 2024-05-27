#include <iostream>

using namespace std;

int main(void){
    // M학년이 뉴비라면 NEWBIE!를, 올드비라면 OLDBIE!를 TLE이라면 TLE!을 출력합니다.
    int N, M;
    cin>>N>>M;
    
    if (M == 1 or M == 2) cout<<"NEWBIE!";
    else if (M <= N) cout<<"OLDBIE!";
    else cout<<"TLE!";
}