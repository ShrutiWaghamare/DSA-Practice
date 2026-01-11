#include <iostream>
using namespace std;

void prime(int n){
    bool isPrime = true;
    for(int i = 2; i <= n; i++){
        if(n % i == 0){
            isPrime = false;
            break;
        }
    }
    
    if(isPrime){
        cout<<"Number is prime";
    }
    else{
        cout<<"Number is not prime";
    }
}
int main() {
    prime(3);
    return 0;
}