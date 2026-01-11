#include <iostream>
using namespace std;


// Example 1: Print 5 lines of 5 stars each
// Method 1: Without nested loop (hardcoded)
int main() {
    for(int i = 1; i <= 5; i++){
        int m = 7;
        for (int i = 1; i <= m; i++){
            cout<<"*";
        }
        cout<<endl;
    }
    return 0;
}