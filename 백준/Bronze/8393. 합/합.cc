#include <iostream>

using namespace std;

int main(void)
{
    int n;
    cin>>n;
    
    int sum=0;
    
    for(int i=0; i<n; i++)
    {
        sum += i+1;
    }
    
    cout<<sum<<endl;
}