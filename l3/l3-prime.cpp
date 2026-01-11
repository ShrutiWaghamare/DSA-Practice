#include <iostream>
using namespace std;

int main() {
    int n = 7;
    bool isPrime = true;
    for(int i = 2; i<= n; i++){
        if(n % i== 0){
            isPrime = false;
            break;
        }
    }

    if (isPrime){
        cout<<"Prime Number \n";
    }
    else{
        cout<<"Not a prime number\n";
    }
    return 0;
}