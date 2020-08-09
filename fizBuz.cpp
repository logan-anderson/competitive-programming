#include <iostream>
using namespace std;
int main() 
{
    int f,b,t;
    cin >> f >> b >>t;
    for(int i=1; i<=t; i++){
        bool fizz = i%f == 0;
        bool buzz = i%b == 0;
        if(buzz && fizz){
            cout << "FizzBuzz" << '\n';
        }
        else if(buzz){
            cout << "Buzz" << '\n';
        }
        else if(fizz) {
            cout << "Fizz"  << '\n';
        }
        else {
            cout << i << '\n';
        }
    }
}