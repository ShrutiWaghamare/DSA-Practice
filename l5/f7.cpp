#include <iostream>
using namespace std;

void prime(int n){
    bool isPrime = true;
    if(n <= 1){
        cout << "Number is not prime";
        return;
    }
    
    for(int i = 2; i <= n-1; i++){
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