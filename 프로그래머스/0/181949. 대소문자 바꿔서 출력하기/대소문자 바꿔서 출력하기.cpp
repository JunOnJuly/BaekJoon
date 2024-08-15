#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    
    for (auto chr : str){
        if (islower(chr)) cout << static_cast<char>(toupper(chr));
        else cout << static_cast<char>(tolower(chr));
    }
}