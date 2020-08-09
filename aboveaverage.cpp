#include <bits/stdc++.h>
using namespace std;

int main() {
    int total;
    cin >> total;
    // cin.ignore();
    for(int i; i<total; i++){
        cout << total;
        cout << " we are here \n";
        //read input
        int class_size;
        cin >> class_size;
        vector<float> v;
        for(int j; j<class_size;j++){
            float val;
            cout << val;
            cin >> val;
            v.push_back(val);
        }
        // cin.ignore();
        float average =  accumulate( v.begin(), v.end(), 0.0 ) / v.size();
        cout << average;
    }
}
