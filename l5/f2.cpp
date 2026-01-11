#include <iostream>
using namespace std;


int sum(int a, int b){
    int s = a + b;
    return s;
}


int min(int a, int b){
    if(a < b){
        return a;
    }
    else{
        return b;
    }
}

int main() {
    // cout<< sum(1, 2);
    // cout<<endl;
    cout<<min(3, 4);
    return 0;
}