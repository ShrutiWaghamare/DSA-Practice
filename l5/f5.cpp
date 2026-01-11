// Sum of digits of number
#include <iostream>
using namespace std;

void SumOfDigit(int num){
    int digitSum= 0;
    while(num>0){
        int lastDigit = num % 10;
        digitSum += lastDigit;
        num = num / 10;
    }
    cout<<digitSum;
}
int main() {
    SumOfDigit(11111);
    return 0;
}