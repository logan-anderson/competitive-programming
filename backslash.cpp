#include <iostream>
#include <string>
using namespace std;

string doPass(string s);
bool isSpecial(char c);

int main() {
    int passes;
    string text; 
    while( cin >> passes ) {
        cin.ignore();
        getline(cin,text);
        for(int i=0; i<passes; i++){
            text = doPass(text);
        }
        cout << text + '\n';
    }
}
bool isSpecial(char c) {
    return ( '!' <= c && c <= '*') || ( '[' <= c && c <= ']');
}
string doPass(string s) {
    string new_string;
    for(int i=0; i<s.length(); i++){
        if(isSpecial(s.at(i))){
            new_string = new_string + '\\' + s.at(i);
        } else {
            new_string = new_string + s.at(i);
        }
    }
    return new_string;
}