#include <iostream>
using namespace std;

// void printHello(){
//     cout<<"Hello"<<endl;
// }

int printHello(){
    cout<<"Hello"<<endl;
    return 7;
}

int main() {
    int val = printHello();
    cout<<val<<endl;
    return 0;
}